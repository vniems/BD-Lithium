import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt
#import seaborn as sns
import networkx as nx
import pandas as pd
import random
import string
import scipy.stats
import network_prop
import sys
#import visJS2jupyter.visJS_module
#import visJS2jupyter.visualizations

# for parallel processing
#from joblib import Parallel, delayed
#import multiprocessing

def main(num_reps=10, seed_gene_file='HC_genes/ASD_HC_no_shared_200114.tsv',int_file='../interactomes/G_PCnet.gpickle', out_name='ASD',rand_method = 'degree_binning',single_or_double='single',save_fnew_rand=False):
    '''
    
    Calculate z-scores for heat propagation
    
    python netprop_zscore.py 10 HC_genes/ASD_HC_no_shared_200114.tsv ../interactomes/G_PCnet.gpickle ASD degree_binning single False

    
    '''
    
    
    print('number of randomizations = '+str(num_reps))
    print('background interactome = ' + int_file)
    print('randomization method = ' + rand_method)
    print('single or double = ' + single_or_double)
    print('save Fnew rand = '+save_fnew_rand)
    
    num_reps = int(num_reps)
    # load interactome and select focal interactome
    Gint = nx.Graph()
    Gint = nx.read_gpickle(int_file)
    if 'None' in Gint.nodes():
        Gint.remove_node('None')


    # load HC genes
    HC_genes_temp = pd.read_csv(seed_gene_file,sep='\t',index_col='Unnamed: 0')
    seed_HC = [str(g[1:-1]).strip("'") for g in HC_genes_temp['seed_genes'].tolist()[0][1:-1].split(', ')]
  
    print(seed_gene_file+':')
    print(len(seed_HC))
    seed_HC = list(np.intersect1d(Gint.nodes(),seed_HC))
    print(len(seed_HC))
    
    # calculate the z-score
    # calc Wprime from Gint
    Wprime = network_prop.normalized_adj_matrix(Gint,conserve_heat=True)
    
    if single_or_double=='single': # calculate z-scores from a single set of seed genes

        print('calculating z-scores: '+seed_gene_file)
        z_seed,Fnew_rand_seed = calc_zscore_heat(Gint,Wprime,seed_HC,num_reps=num_reps,rand_method=rand_method)
        z_seed.to_csv('z_'+out_name+'_'+str(num_reps)+'_reps_'+rand_method+'.tsv',sep='\t')
        if save_fnew_rand=='True': # if true, save out the vector of randoms (this can be a large file)
            pd.DataFrame(Fnew_rand_seed).to_csv('Fnew_'+out_name+'_rand'+str(num_reps)+'_reps_'+rand_method+'.tsv',sep='\t')
        
       
    elif single_or_double=='double': # calculate z-scores from two sets of seed genes:
        
        # --- not currently functional ----
        
        print('calculating ASD-CHD z-scores')
        z_ASD_CHD,Fnew_rand_ASD_CHD = calc_zscore_heat_double(Gint,Wprime,ASD_HC,CHD_HC,num_reps=num_reps,rand_method = rand_method)
        z_ASD_CHD.to_csv('z_'+out_name+'_'+str(num_reps)+'_reps_'+rand_method+'.tsv',sep='\t')
    
    
def calc_zscore_heat(Gint,Wprime,genes_D1,num_reps=10,ks_sig = 0.3,rand_method = 'degree_binning'):
    '''
    Helper function to calculate the z-score of heat values from one input seet of genes
    
    rand_method = 'degree_ks_test', or 'degree_binning'.  select the type of randomization
    '''
    seed_D1 = list(np.intersect1d(list(genes_D1),Gint.nodes()))
    Fnew_D1 = network_prop.network_propagation(Gint,Wprime,seed_D1,alpha=.5,num_its=20)
    
    num_focal_edges=len(nx.subgraph(Gint,seed_D1).edges())
    
    Fnew_rand_D1 = np.zeros([num_reps,len(Fnew_D1)])
    if rand_method == 'degree_ks_test':
        for r in range(num_reps):
            if (r%50)==0:
                print(r)
            # UPDATE 8/23/17 -- replace with randomly selecting seed nodes, checking for degree distribution equivalence

            p=0
            # resample until degree distributions are not significantly different
            while p<ks_sig:
                seed_D1_random = Gint.nodes()
                np.random.shuffle(seed_D1_random)
                seed_D1_random = seed_D1_random[0:len(seed_D1)]
                ks_stat,p=scipy.stats.ks_2samp(pd.Series(Gint.degree(seed_D1)),pd.Series(Gint.degree(seed_D1_random)))


            Fnew_rand_tmp = network_prop.network_propagation(Gint,Wprime,seed_D1_random,alpha=.5,num_its=20)
            Fnew_rand_tmp.loc[seed_D1_random]=np.nan # set seeds to nan so they don't bias results
            Fnew_rand_D1[r] = Fnew_rand_tmp.loc[Fnew_D1.index.tolist()]

    elif rand_method == 'degree_binning':
        bins = get_degree_binning(Gint,10)
        min_degree, max_degree, genes_binned = zip(*bins)
        bin_df = pd.DataFrame({'min_degree':min_degree,'max_degree':max_degree,'genes_binned':genes_binned})
        # create a lookup table for degree and index
        actual_degree_to_bin_df_idx = {}
        for i in range(0, bin_df['max_degree'].max() + 1):
            idx_temp = bin_df[ (bin_df['min_degree'].lt(i + 1)) & (bin_df['max_degree'].gt(i - 1)) ].index.tolist()
            if len(idx_temp) > 0: # there are some degrees which aren't represented in the graph
                actual_degree_to_bin_df_idx[i] = idx_temp[0]
                
#        r_inputs = range(num_reps)
#        num_cores = multiprocessing.cpu_count()-1
#        Fnew_rand_D1 = Parallel(n_jobs=num_cores)(delayed(calc_Fnew_rand_deg_binning)(r,Gint,bin_df,seed_D1,actual_degree_to_bin_df_idx,Fnew_D1,num_focal_edges,Wprime) for r in r_inputs)
        for r in range(num_reps):
            if (r%50)==0:
                print(r)
            # UPDATE 1/30/18 -- sample from degree bins
            seed_D1_random = []
            for g in seed_D1:
                degree_temp = nx.degree(Gint,g)
                # find genes with similar degrees to focal gene degree
                genes_temp = bin_df.loc[actual_degree_to_bin_df_idx[degree_temp]]['genes_binned']
                
                np.random.shuffle(genes_temp) # shuffle them
                while genes_temp[0] in seed_D1_random: # make sure the gene isn't already in the list
                    np.random.shuffle(genes_temp) # shuffle them
                seed_D1_random.append(genes_temp[0]) # build the seed_D1_random list
                
#            # modify random seeds so that they have similar localization properties to input set
#            prev_num_edges = len(nx.subgraph(Gint,seed_D1_random).edges())
#            print(prev_num_edges)
#            # pick a gene at random and replace it, if the number of edges increases, keep it, otherwise, don't keep
#            counter=-1
#            while (prev_num_edges < num_focal_edges) and (counter < 3000):
#                counter+=1
#                if (counter%1000)==0:
#                    print(counter)
#                    print(prev_num_edges)
#                np.random.shuffle(seed_D1_random)
#                replace_gene = seed_D1_random[0]
#                deg_replace_gene = nx.degree(Gint,replace_gene)
#                replace_bin = actual_degree_to_bin_df_idx[deg_replace_gene]
#                genes_temp = bin_df.loc[replace_bin]['genes_binned'] # use the lookup table for speed
#                np.random.shuffle(genes_temp) # shuffle them
#                #print(seed_D1_random[0])
#                seed_random_new=seed_D1_random[:]
#                seed_random_new[0]=genes_temp[0]
#                #print(seed_random_new[0])
#                new_num_edges = len(nx.subgraph(Gint,seed_random_new).edges())
#                #print(new_num_edges)
#                if new_num_edges>prev_num_edges:
#                    prev_num_edges=new_num_edges
#                    seed_D1_random = seed_random_new[:]
                

            Fnew_rand_tmp = network_prop.network_propagation(Gint,Wprime,seed_D1_random,alpha=.5,num_its=20)
            Fnew_rand_tmp.loc[seed_D1_random]=np.nan # set seeds to nan so they don't bias results
            Fnew_rand_D1[r] = Fnew_rand_tmp.loc[Fnew_D1.index.tolist()]


    z_score_D1 = (np.log(Fnew_D1)-np.nanmean(np.log(Fnew_rand_D1),axis=0))/np.nanstd(np.log(Fnew_rand_D1),axis=0)
    
    return z_score_D1, Fnew_rand_D1

# Was for parallel processing, but have issues with memory errors
#def calc_Fnew_rand_deg_binning(r,Gint,bin_df,seed_D1,actual_degree_to_bin_df_idx,Fnew_D1,num_focal_edges,Wprime):
#    #if (r%50)==0: # print some progress
#        #print(r)
#    print('r = '+str(r))
#    np.random.seed(seed=r)
#    seed_D1_random = []
#    for g in seed_D1:
#        degree_temp = nx.degree(Gint,g)
#        # find genes with similar degrees to focal gene degree
#        genes_temp = bin_df.loc[actual_degree_to_bin_df_idx[degree_temp]]['genes_binned']
#        np.random.shuffle(genes_temp) # shuffle them
#        seed_D1_random.append(genes_temp[0]) # build the seed_D1_random list
#    # modify random seeds so that they have similar localization properties to input set
#    prev_num_edges = len(nx.subgraph(Gint,seed_D1_random).edges())
#    print(prev_num_edges)
#    # pick a gene at random and replace it, if the number of edges increases, keep it, otherwise, don't keep
#    counter=-1
#    while (prev_num_edges < num_focal_edges):
#        counter+=1
#        if (counter%1000)==0:
#            print(counter)
#            print(prev_num_edges)
#        np.random.shuffle(seed_D1_random)
#        replace_gene = seed_D1_random[0]
#        deg_replace_gene = nx.degree(Gint,replace_gene)
#        replace_bin = actual_degree_to_bin_df_idx[deg_replace_gene]
#        genes_temp = bin_df.loc[replace_bin]['genes_binned'] # use the lookup table for speed
#        np.random.shuffle(genes_temp) # shuffle them
#        #print(seed_D1_random[0])
#        seed_random_new=seed_D1_random[:]
#        seed_random_new[0]=genes_temp[0]
#        #print(seed_random_new[0])
#        new_num_edges = len(nx.subgraph(Gint,seed_random_new).edges())
#        #print(new_num_edges)
#        if new_num_edges>prev_num_edges:
#            prev_num_edges=new_num_edges
#            seed_D1_random = seed_random_new[:]
#    Fnew_rand_tmp = network_prop.network_propagation(Gint,Wprime,seed_D1_random,alpha=.5,num_its=20)
#    Fnew_rand_tmp.loc[seed_D1_random]=np.nan # set seeds to nan so they don't bias results
#    Fnew_rand_tmp = Fnew_rand_tmp.loc[Fnew_D1.index.tolist()]
#    return Fnew_rand_tmp

def calc_zscore_heat_double(Gint,Wprime,genes_D1,genes_D2,num_reps=10,ks_sig = 0.3,rand_method = 'degree_binning'):
    '''
    Helper function to calculate the z-score of heat values from two input sets of genes
    
    rand_method = 'degree_binning'.  (this is the only option for now 'degree_ks_test' is deprecated) 
    '''
    seed_D1 = list(np.intersect1d(list(genes_D1),Gint.nodes()))
    Fnew_D1 = network_prop.network_propagation(Gint,Wprime,seed_D1,alpha=.5,num_its=20)
    
    seed_D2 = list(np.intersect1d(list(genes_D2),Gint.nodes()))
    Fnew_D2 = network_prop.network_propagation(Gint,Wprime,seed_D2,alpha=.5,num_its=20)
    
    Fnew_both = Fnew_D1*Fnew_D2
    
    
    Fnew_rand_both = np.zeros([num_reps,len(Fnew_both)])
    if rand_method == 'degree_binning':
        bins = get_degree_binning(Gint,10)
        min_degree, max_degree, genes_binned = zip(*bins)
        bin_df = pd.DataFrame({'min_degree':min_degree,'max_degree':max_degree,'genes_binned':genes_binned})
        for r in range(num_reps):
            if (r%50)==0:
                print(r)
            # UPDATE 1/30/18 -- sample from degree bins
            seed_D1_random = []
            for g in seed_D1:
                degree_temp = nx.degree(Gint,g)
                # find genes with similar degrees to focal gene degree
                genes_temp = bin_df[(bin_df['min_degree']<=degree_temp)&(bin_df['max_degree']>=degree_temp)]['genes_binned'].tolist()[0]
                np.random.shuffle(genes_temp) # shuffle them
                seed_D1_random.append(genes_temp[0]) # build the seed_D1_random list

            seed_D2_random = []
            for g in seed_D2:
                degree_temp = nx.degree(Gint,g)
                # find genes with similar degrees to focal gene degree
                genes_temp = bin_df[(bin_df['min_degree']<=degree_temp)&(bin_df['max_degree']>=degree_temp)]['genes_binned'].tolist()[0]
                np.random.shuffle(genes_temp) # shuffle them
                seed_D2_random.append(genes_temp[0]) # build the seed_D1_random list
                

            Fnew_rand_1 = network_prop.network_propagation(Gint,Wprime,seed_D1_random,alpha=.5,num_its=20)
            Fnew_rand_1.loc[seed_D1_random]=np.nan # set seeds to nan so they don't bias results
            
            Fnew_rand_2 = network_prop.network_propagation(Gint,Wprime,seed_D2_random,alpha=.5,num_its=20)
            Fnew_rand_2.loc[seed_D2_random]=np.nan # set seeds to nan so they don't bias results
            
            Fnew_rand_both[r] = (Fnew_rand_1*Fnew_rand_2).loc[Fnew_D1.index.tolist()]


    z_score_both = (np.log(Fnew_both)-np.nanmean(np.log(Fnew_rand_both),axis=0))/np.nanstd(np.log(Fnew_rand_both),axis=0)
    
    return z_score_both, Fnew_rand_both

def get_degree_binning(g, bin_size, lengths=None):
    '''
    This function comes from network_utilities.py of emregtoobox.  
    '''
    degree_to_nodes = {}
    for node, degree in g.degree().iteritems():
        if lengths is not None and node not in lengths:
            continue
        degree_to_nodes.setdefault(degree, []).append(node)
    values = degree_to_nodes.keys()
    values.sort()
    bins = []
    i = 0
    while i < len(values):
        low = values[i]
        val = degree_to_nodes[values[i]]
        while len(val) < bin_size:
            i += 1
            if i == len(values):
                break
            val.extend(degree_to_nodes[values[i]])
        if i == len(values):
            i -= 1
        high = values[i]
        i += 1 
        #print low, high, len(val)
        if len(val) < bin_size:
            low_, high_, val_ = bins[-1]
            bins[-1] = (low_, high, val_ + val)
        else:
            bins.append((low, high, val))
    return bins



if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
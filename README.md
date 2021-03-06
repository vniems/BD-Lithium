<br><br>

<p align="center">
    <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/HEADER/BD_Lithium_project.png" width="770">
</p>

<br>
<h1 align="center">Bipolar Disorder and Lithium Response: Pharmacogenomic Study
<p>

![](https://img.shields.io/badge/Release-v1.1.0-orange?style=flat&logo=github&logoColor=orange)    ![](https://img.shields.io/badge/Release%20Date-19%20June%202022-red?style=flat&logo=github&logoColor=red)   ![](https://img.shields.io/badge/License-%20GPL--3.0--or--later-brightgreen?style=flat&logo=opensourceinitiative&logoColor=brightgreen)   ![](https://img.shields.io/badge/Platform-R%20|%20Python-blue?style=flat)</h1>


### This is the README for the project of “Bipolar Disorder and Lithium Response: Pharmacogenomic Study”.
### Note that this project is temporality under development, and coming soon. Some info is not completed.



## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Project_icon.svg" width="50px"> &nbsp;About Our Project
**The project** is a collection of source codes being used in the study that aimed to identify the genetic contribution into lithium response in patients with bipolar disorder (BD) using multi-omics analysis of integrated between genome-wide association study (GWAS) and RNA-sequencing (RNA-seq) data.

Here, we make available the analytic tools employed as part of the main study, of which the manuscript, entitled ***"Focal adhesion is associated with lithium response in bipolar disorder: evidence from a network-based multi-omics analysis"***, has been published in *Molecular Psychiatry*. [doi will be added after a paper is published] 

-----------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/TOC_icon.svg" width="50px"> &nbsp;Table of Contents
-   [About our project](https://github.com/vniems/BD-Lithium/edit/main/README.md#-about-our-project)
-   [Table of contents](https://github.com/vniems/BD-Lithium/edit/main/README.md#-table-of-contents)
-   [Project aim](https://github.com/vniems/BD-Lithium/edit/main/README.md#-project-aim)
-   [The project workflow and file descriptions](https://github.com/vniems/BD-Lithium/edit/main/README.md#-the-project-workflow-and-file-descriptions)
    - [Step I - Genome-wide association study of patients with BD](#step-i)
    - [Step II - Transcriptomic analysis of iPSC-derived neurons](#step-ii)
    - [Step III - Network and functional enrichment analyses](#step-iii)

-  [Feature guidance](https://github.com/vniems/BD-Lithium/edit/main/README.md#-feature-guidance)
-  [Contributing](https://github.com/vniems/BD-Lithium/edit/main/README.md#-contributing)
-  [License](https://github.com/vniems/BD-Lithium/edit/main/README.md#-license)
-  [Citation](https://github.com/vniems/BD-Lithium/edit/main/README.md#-citation)
-  [References](https://github.com/vniems/BD-Lithium/edit/main/README.md#-references)

------------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Aim_icon.svg" width="50px"> Project Aim

**The purpose** of the project is to distribute the tool (code development) that had been used in the multi-omics analysis of integrated data between BD GWAS and RNA-seq of patients-derived induced pluripotent stem cell (iPSC) neurons.

The study workflow including detailed methods can be found in 1) the **‘Method’** section in the main text and 2) the **‘Supplemental Methods’** of the manuscript [doi will be added after a paper is published].

------------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Workflow_icon.svg" width="50px"> The Project Workflow and File Descriptions
Source codes of this project can be found in a [<code>'DIRECTORIES'</code>](https://github.com/vniems/BD-Lithium/tree/main/DIRECTORIES) folder, containing **three subdirectories** based on the analytic steps as shown below. 
<p>Brief description is provided for each file, including additional/required data, which will be a useful resource for users.  

### Step I
<details open = "open">
    <summary><b>Genome-wide association study of patients with BD</b></summary>
    <br>
    <ul>
        <ul>
            <li><strong>Genome-wide association study (GWAS) analysis & imputation:</strong> we did not provide the code here. A summary is described as follows.</li>    
            <ul>
            <br>
                <li>DNA from 1106 subjects was genotyped on the Illumina PsychChip (https://sites.google.com/a/broadinstitute.org/psych-chip-resources/home).</li>
                <li>Genotype data was screened for low call rate, low genotyping rate, and Hardy-Weinberg equilibrium. Imputation was performed using IMPUTE2 (Howie et al. 2009). Association was tested by linear regression as implemented in PLINK (Purcell et al. 2007).</li>
            </ul>
            <br>
            <li><strong>Gene-based analysis:</strong> we used a Versatile Gene-based Association Test (VEGAS) (Mishra and Macgregor 2015), a web-based tool, https://vegas2.qimrberghofer.edu.au/.</li>
            <br>
            <li><strong>GWAS prioritizing analysis:</strong> the GWAS results were reprioritized by using network information and the algorithms implemented in <strong>genome-wide boosting analysis (GWAB)</strong> (Shim et al. 2017) and NetWAS (Greene et al. 2015) methods.</li>      
       </ul>
    </ul>
</details>
               
    
### Step II
<details open="open">
    <summary><b>Transcriptomic analysis of iPSC-derived neurons</b></summary>
    <br>
    <ul>
        <ul>
            <li><strong>Raw data of RNA-sequencing (RNA-seq)</strong> —stored in NCBI's Gene Expression Omnibus (Edgar et al. 2002) and are accessible through <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205422"><strong>GEO Series accession number GSE205422</strong></a>.</li>
            <br>
            <li><strong>RNA-seq analysis:</strong></li>
            <ul>
                <br>
                    <li><strong>Differential expression analysis:</strong> the functions are used for RNA-seq differential expression analysis and downstream analysis.</li>
                    <li><strong>RNA-seq input files:</strong></li>
                         <ul>
                            <br>
                                <di>▫︎ <strong>Data #1:</strong> Phenotypic data - <code>kelsoe_metadata_111.csv</code>.</di>
                                <p><di>▫︎ <strong>Data #2:</strong> Transcriptomic data from the RNA-seq raw data after quality control and alignment processes - <code>all_genes_results_111.txt</code>. <em>Note</em> that data #2 was not stored in this project, read more detail <a href="https://github.com/vniems/BD-Lithium/tree/main/DIRECTORIES/STEP2-RNASeq/RNASeq_input/RNASeq_input_info.html"><u>here</u></a>.</di>
                         </ul>
            </ul>
         </ul>
     </ul>
</details>           
            

### Step III
<details open="open">
    <summary><b>Network and functional enrichment analyses</b></summary>
    <br>
    <ul>
        <ul>
            <li><strong>Network propagation analysis</strong></li>
            <br>
            <li><strong>Cluster analysis</strong></li>
            <br>
            <li><strong>KEGG pathway analysis</strong></li>
            <br>
            <li><strong>Pathview creation</strong></li>
            <br>
            <li><strong>Network input files:</strong></li>
            <ul>
                <br> 
                    <li><strong>Data #3:</strong> A list of significantly differentially expressed (DE) genes in Li responders vs Li non-responders (LR vs NR), <em>n</em> = 41 genes - <code>DE_Genes_Li and CTRL_LRvsNR.xlsx</code>.</li>
                    <li><strong>Data #4:</strong>  A list of the top 5% prioritized genes obtained from VEGAS, GWAB, and NetWAS - <code>prioritized_genes_boosting_methods_5percent_190708.xlsx</code>.</li>
            </ul>
        </ul>
     </ul>
</details>

------------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Files_icon.svg" width="50px"> &nbsp;&nbsp;Feature Guidance

All source codes shown here can be found in this GitHub project:<p>

| Features                     |<img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/LANGUAGES/R_language.svg" width="49px">|<img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/LANGUAGES/Python_language.svg" width="49px">|Additional software required|
|------------------------------|:--------:|:--------:|:------------------------:|
| NetWAS analysis              |          |     √    |                          |
| RNA-seq analysis             |    √     |          |                          |
| Network propagation analysis |          |     √    |          Cytoscape       |
| Cluster analysis             |          |          |                          |
| KEGG pathway analysis        |          |          |                          |
| Pathview creation            |          |     √    |                          |

------------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Contributing_icon.svg" width="50px"> &nbsp;Contributing

Contributions for this project are:

-   **Code development team:**
   
    - Kathleen M. Fisch, PhD
    - Sara Brin Rosenthal, PhD
    
-   **Executive manager and sponsor:**

    - John R. Kelsoe, MD
    
-   **Administrator:**
 
    - Vipavee Niemsiri, MD, PhD

------------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Licenses_icon.svg" width="50px"> &nbsp;License

**Copyright © 2022**<br>
    
Contents in this project are under [licenses](https://github.com/vniems/BD-Lithium/tree/main/LICENSES) as follows:

- **Source codes:** ![](https://img.shields.io/badge/License-%20GPL--3.0--or--later-brightgreen?style=flat&logo=opensourceinitiative&logoColor=brightgreen)<p>**The source codes in this project** is *free* to be used and/or modify *under the terms of* **the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version**. Please see the policy and term of use <u>[here](https://github.com/vniems/BD-Lithium/blob/main/LICENSES/License_GLP3.0_later.md)</u>.
<br>

- **Other materials except the source codes:** ![](https://img.shields.io/badge/License-CC--BY--4.0-yellow?style=flat&logo=creativecommons&logoColor=white)<p>Other contents, such as input data, are part of the study published in the manuscript entitled, “Focal adhesion is associated with lithium response in bipolar disorder: evidence from a network-based multi-omics analysis", which are *under the term of* [**a CC BY license (Creative Commons Attribution 4.0 International License)**](https://github.com/vniems/BD-Lithium/blob/main/LICENSES/License_CC_by_4.0.md).
<br><br>
  
> **Artwork:** <img src = "https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/LICENSE/cc_by_nc_sa_purple.svg" width="100px"> <p>Copyright © 2022 by Vipavee N. The artwork in this project is licensed *under the term of* [<b>a CC BY-NC-SA 4.0 license (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License)</b>](https://github.com/vniems/BD-Lithium/blob/main/LICENSES/License_CC_by_nc_sa_4.0.md).
    
------------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Citation_icon.svg" width="50px"> Citation

 If you use the code from this project, please cite with the data from the `CITATION.cff` file (see [<u>here</u>](https://github.com/vniems/BD-Lithium/blob/main/CITATION/CITATION_v110_2022_06_19.cff)) or from **the Council of Science Editors (CSE)** citation styles as shown below.
    <br>
    <p>
   ><b>CSE Bibliography Format:</b>
        <p>
    Niemsiri V, Rosenthal SB, Fisch KM, and Kelsoe JR. 2022. Bipolar Disorder and Lithium Response: Pharmacogenomic Study. San Francisco (CA): GitHub; [accessed 2022 Jun 19]. https://github.com/vniems/BD-Lithium.

------------------------------------------------------------------------

## <img src="https://github.com/vniems/BD-Lithium/blob/main/IMAGES/ICONS/SECTIONS/Reference_icon.svg" width="50px"> &nbsp;References

<p>Edgar R, Domrachev M, Lash AE. 2002. Gene Expression Omnibus: NCBI gene expression and hybridization array data repository. Nucleic Acids Res. 30(1):207-210.

<p>Greene CS, Krishnan A, Wong AK, Ricciotti E, Zelaya RA, Himmelstein DS, Zhang R, Hartmann BM, Zaslavsky E, Sealfon SC et al. 2015. Understanding multicellular function and disease with human tissue-specific networks. Nat Genet. 47(6):569-576.

<p>Howie BN, Donnelly P, Marchini J. 2009. A flexible and accurate genotype imputation method for the next generation of genome-wide association studies. PLoS Genet. 5(6):e1000529.

<p>Mishra A, Macgregor S. 2015. VEGAS2: Software for more flexible gene-based testing. Twin Res Hum Genet. 18(1):86-91.

<p>Purcell S, Neale B, Todd-Brown K, Thomas L, Ferreira MA, Bender D, Maller J, Sklar P, de Bakker PI, Daly MJ et al. 2007. PLINK: A tool set for whole-genome association and population-based linkage analyses. Am J Hum Genet. 81(3):559-575.

<p>Shim JE, Bang C, Yang S, Lee T, Hwang S, Kim CY, Singh-Blom UM, Marcotte EM, Lee I. 2017. GWAB: A web server for the network-based boosting of human genome-wide association data. Nucleic Acids Res. 45(W1):W154-W161.
<br>

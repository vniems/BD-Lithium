<h1 align="center">Bipolar Disorder and Lithium Response: Pharmacogenomic Study

![](https://img.shields.io/badge/Release%20Date-June%202022-red?style=flat&logo=github&logoColor=red)      ![](https://img.shields.io/badge/Release-v1.1.0-orange?style=flat&logo=github&logoColor=orange) ![](https://img.shields.io/badge/License-%20GPL--3.0--or--later-brightgreen?style=flat&logo=opensourceinitiative&logoColor=brightgreen) ![](https://img.shields.io/badge/Platform-R%20|%20Python-blue?style=flat)</h1>


### This is the README for the project of “Bipolar Disorder and Lithium Response: Pharmacogenomic  Study”.
### Note that this project is temporality under development, and coming soon.



## About Our Project
**The aim** of the project is to identify the genetic contribution into lithium response in patients with bipolar disorder (BD) using multi-omics analysis of integrated between genome-wide association (GWAS) and RNA-sequencing (RNA-seq) data.

Here, we make available the analytic tools employed as part of the main study, of which the manuscript, entitled ***"Focal adhesion is associated with lithium response in bipolar disorder: evidence from a network-based multi-omics analysis"***, has been published in *Molecular Psychiatry*. [doi will be added after a paper is published] 

-----------------------------------------------------------------------

## Table of Contents
-   [About our project](#About-Our-Project)   
-   [Project aim](#Project-Aim)
-   [The project workflow and file descriptions](#The-Project-Workflow-and-File-Descriptions)
    - [Genome-wide association study of patients with BD](https://github.com/vniems/BD-Lithium/blob/main/README.md#step-i)
    - [Transcriptomic analysis of iPSC-derived neurons](https://github.com/vniems/BD-Lithium/blob/main/README.md#step-ii)
    - [Network and functional enrichment analyses](https://github.com/vniems/BD-Lithium/blob/main/README.md#step-iii)

-  [Feature guidance](#Feature-guidance)
-  [Contributing](#Contributing)
-  [License](#License)
-  [Citation](#Citation)
-  [References](#References)

------------------------------------------------------------------------

## Project Aim 

**The purpose** of the project is to distribute the tool (code development) that had been used in the multi-omics analysis of integrated data between BD GWAS and RNA-seq of patients-derived induced pluripotent stem cell (iPSC) neurons.

The study workflow including detailed methods can be found in 1) the **‘Method’** section in the main text and 2) the **‘Supplemental Methods’** of the manuscript [doi will be added after a paper is published].

------------------------------------------------------------------------

## The Project Workflow and File Descriptions
This project includes **three subdirectories** based on the analytic steps as shown below. 
<p>Brief description is provided for each file, including additional/required data, which will be a useful resource for users.  

### Step I
<details open="open">
    <summary><b>Genome-wide association study of patients with BD</b></summary>
    <br>
    <ul>
        <ul>
            <li><strong>Genome-wide association study (GWAS) analysis & imputation:</strong> we did not provide the code here. A summary is described as follows.</li>    
            <ul>
            <br>
                <li>DNA from 1106 subjects was genotyped on the Illumina PsychChip (https://sites.google.com/a/broadinstitute.org/psych-chip-resources/home).</li>
                <li>Genotype data was screened for low call rate, low genotyping rate, and Hardy-Weinberg equilibrium. Imputation was performed using IMPUTE2. Association was tested by linear regression as implemented in PLINK.</li>
            </ul>
            <br>
            <li><strong>Gene-based analysis:</strong> we used a Versatile Gene-based Association Test (VEGAS), a web-based tool, https://vegas2.qimrberghofer.edu.au/.</li>
            <br>
            <li><strong>GWAS prioritizing analysis:</strong> the GWAS results were reprioritized by using network information and the algorithms implemented in <strong>genome-wide boosing analysis (GWAB)</strong> and NetWAS methods.</li>      
       </ul>
    </ul>
</details>
               
    
### Step II
<details open="open">
    <summary><b>Transcriptomic analysis of iPSC-derived neurons</b></summary>
    <br>
    <ul>
        <ul>
            <li><strong>Raw data of RNA-sequencing (RNA-seq)</strong> —stored in NCBI's Gene Expression Omnibus (Edgar et al., 2002) and are accessible through <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205422"><strong>GEO Series accession number GSE205422</strong></a>.</li>
            <br>
            <li><strong>RNA-seq analysis:</strong></li>
            <ul>
                <br>
                    <li><strong>Differential expression analysis:</strong> the functions are used for RNA-seq differential expression analysis and downstream analysis.</li>
                    <li><strong>Input files:</strong></li>
                        <ul>
                            ▸ Data #1: Phenotype data, kelsoe_metadata_111.csv
                            <p>▸ Data #2: Gene expression data, all_genes_results_111s.txt
                        </ul>
            </ul>
         </ul>
     </ul>
</details>           
            

### Step III
<details open="open">
    <summary><b>Network and functional enrichment analyses</b></summary>
  <ol>

-   **Network propagation analysis**

-   **Cluster analysis**

-   **KEGG pathway analysis**

-   **Pathview creation**

-   **Input files:**
    -   Data #3: DE_Genes_Li and CTRL_LRvsNR_for_Katie.xlsx
    -   Data #4: prioritized_genes_boosting_methods_5percent_190708.xlsx
</ol>
</details>

------------------------------------------------------------------------

## Feature Guidance

All source code shown here can be found in this GitHub project: 

| Features                     |<img src="https://github.com/SommaiGH/master-readme/blob/main/img/R-GitHub.svg" width="50px">|<img src="https://github.com/SommaiGH/master-readme/blob/main/img/Python-GItHub.svg" width="50px">|Additional software required|
|------------------------------|:--------:|:--------:|:------------------------:|
| NetWAS analysis              |          |     √    |                          |
| RNA-seq analysis             |    √     |          |                          |
| Network propagation analysis |          |     √    |          Cytoscape       |
| Cluster analysis             |          |          |                          |
| KEGG pathway analysis        |          |          |                          |
| Pathview creation            |          |     √    |                          |

------------------------------------------------------------------------

## Contributing

Contributions for this project are:

-   **Code development team:**
   
    - Kathleen M. Fisch, PhD
    - Sara Brin Rosenthal, PhD
    
-   **Executive manager and sponsor:**

    - John R. Kelsoe, MD
    
-   **Administrator:**
 
    - Vipavee Niemsiri, MD, PhD

------------------------------------------------------------------------

## License

**Copyright © 2022**
    
The content in this project are under licenses as follows:

- **Source code:** ![](https://img.shields.io/badge/License-%20GPL--3.0--or--later-brightgreen?style=flat&logo=opensourceinitiative&logoColor=brightgreen)

**The source code in this project** is *free* to be used and/or modify *under the terms of* **the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version**. Please see the policy and term of use <u>[here](https://github.com/SommaiGH/master-readme/blob/main/license.md)</u>.
<br>

- **Other files except the source code:** ![](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0%20-yellow?style=flat&logo=creativecommons&logoColor=white)

Other files, such as input files, are part of the study published in the manuscript entitled, “Focal adhesion is associated with lithium response in bipolar disorder: evidence from a network-based multi-omics analysis", which are *under* [**a CC BY license (Creative Commons Attribution 4.0 International License)**](https://creativecommons.org/licenses/by/4.0/legalcode).
<br>

> **Artwork:** ![](https://user-images.githubusercontent.com/107134586/174465149-2d248174-2da8-43eb-89b5-1cba7459f722.svg) <p>Copyright © 2022 by Vipavee N. The artwork in this project is licensed under the term of [<b>a CC BY-NC-SA 4.0 license (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License)</b>](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
    
------------------------------------------------------------------------

## Citation

If you use the code from this project, please cite with <b>the CITATION.cff</b> format (see our `CITATION.cff` file <u>here</u>) or **the Council of Science Editors (CSE)** citation styles as an example below.

    CSE Bibliography Format:   
    
    Niemsiri V, Rosenthal SB, Fisch KM, and Kelsoe JR. 2022. Bipolar Disorder and Lithium Response. San Francisco (CA): GitHub; [accessed 2022 Jun 6]. https://github.com/vniems/BD-Lithium.

------------------------------------------------------------------------

## References

<p>Edgar R, Domrachev M, Lash AE. 2002. Gene Expression Omnibus: NCBI gene expression and hybridization array data repository. Nucleic Acids Res. 30(1):207-210.

<p>Greene CS, Krishnan A, Wong AK, Ricciotti E, Zelaya RA, Himmelstein DS, Zhang R, Hartmann BM, Zaslavsky E, Sealfon SC et al. 2015. Understanding multicellular function and disease with human tissue-specific networks. Nat Genet. 47(6):569-576.

<p>Howie BN, Donnelly P, Marchini J. 2009. A flexible and accurate genotype imputation method for the next generation of genome-wide association studies. PLoS Genet. 5(6):e1000529.

<p>Mishra A, Macgregor S. 2015. VEGAS2: Software for more flexible gene-based testing. Twin Res Hum Genet. 18(1):86-91.

<p>Purcell S, Neale B, Todd-Brown K, Thomas L, Ferreira MA, Bender D, Maller J, Sklar P, de Bakker PI, Daly MJ et al. 2007. PLINK: A tool set for whole-genome association and population-based linkage analyses. Am J Hum Genet. 81(3):559-575.

<p>Shim JE, Bang C, Yang S, Lee T, Hwang S, Kim CY, Singh-Blom UM, Marcotte EM, Lee I. 2017. GWAB: A web server for the network-based boosting of human genome-wide association data. Nucleic Acids Res. 45(W1):W154-W161.
    
    
 

    

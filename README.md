<h1 align="center">Bipolar Disorder and Lithium Response: Pharmacogenomic Study

![](https://img.shields.io/badge/Release%20Date-June%202022-red?style=flat&logo=github&logoColor=red)      ![](https://img.shields.io/badge/Release-v1.1.0-orange?style=flat&logo=github&logoColor=orange) ![](https://img.shields.io/badge/License-%20GPL--3.0--or--later-brightgreen?style=flat&logo=opensourceinitiative&logoColor=brightgreen)</h1>


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
    - [Genome-wide association study of patients with BD](#Genome-wide association study of patients with BD)
    - [Transcriptomic analysis of iPSC-derived neurons](#Transcriptomic analysis of iPSC-derived neurons)
    - [Network and functional enrichment analysis](#Network-and-functional-enrichment-analysis)

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
This project includes **3 subdirectories** based on the analytic steps as shown below. 
Brief description is provided for each file, including additional/required data, which will be a useful resource for users.  

### Step I
<details>
    <summary><b>Genome-wide association study of patients with BD</b></summary>
    <br>
    <ul>
        <li><strong>Genome-wide association study (GWAS) analysis & imputation:</strong> we did not provide the code here. A summary is described as follows.</li>
        </li>
        <li>
            <ul>
                <li>- DNA from 1106 subjects was genotyped on the Illumina PsychChip (https://sites.google.com/a/broadinstitute.org/psych-chip-resources/home).</li>
            </ul>
    </li>

         -   Genotype data was screened for low call rate, low genotyping rate, and Hardy-Weinberg equilibrium. Imputation was performed using IMPUTE2. Association was tested by linear regression as implemented in PLINK.

  <details>
  <summary><b>Genome-wide association study of patients with BD</b></summary>
  <br>
    <ul>
  <li>
      
- **Genome-wide association study (GWAS) analysis & imputation:** we did not provide the code here. A summary is described as follows.
    -   DNA from 1106 subjects was genotyped on the Illumina PsychChip (https://sites.google.com/a/broadinstitute.org/psych-chip-resources/home).
    -   Genotype data was screened for low call rate, low genotyping rate, and Hardy-Weinberg equilibrium. Imputation was performed using IMPUTE2. Association was tested by linear regression as implemented in PLINK.

- **Gene-based analysis:** we used a Versatile Gene-based Association Test (VEGAS), a web-based tool, https://vegas2.qimrberghofer.edu.au/.

- **GWAS prioritizing analysis:** the GWAS results were reprioritized by using network information and the algorithms implemented in **genome-wide boosing analysis (GWAB)** and NetWAS methods.
  </ol>
</details>
    
### Step II
<details open="open">
    <summary><b>Transcriptomic analysis of iPSC-derived neurons</b></summary>
  <ol>

-   **Raw data of RNA-sequencing (RNA-seq)** — stored in NCBI's Gene Expression Omnibus (Edgar et al., 2002) and are accessible through [**GEO Series accession number GSE205422**](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205422).

-   **RNA-seq analysis:**

    -   Differential expression analysis: the functions are used for RNA-seq differential expression analysis and downstream analysis.
    -   Input files:
        -   Data #1: Phenotype data, kelsoe_metadata_111.csv
        -   Data #2: Gene expression data, all_genes_results_111s.txt
  </ol>
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
| NetWas analysis              |          |     √    |                          |
| RNA-seq analysis             |    √     |          |                          |
| Network propagation analysis |          |     √    |          Cytoscape       |
| Cluster analysis             |          |          |                          |
| KEGG pathway analysis        |          |          |                          |
| Pathview creation            |          |     √    |                          |

------------------------------------------------------------------------

## Contributing

Contributions for this project are:

-   **Code development team:**
   
    - Kathleen M. Fisch, Ph.D.
    - Sara Brin Rosenthal, Ph.D.
    
-   **Executive manager and sponsor:**

    - John R. Kelsoe, M.D.
    
-   **Administrator:**
 
    - Vipavee Niemsiri, M.D., Ph.D.

------------------------------------------------------------------------

## License

**Copyright © 2022**

**The code in this project** is *free* to be used and/or modify *under the terms of* **the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version**. Please see the policy and term of use <u>[here](https://github.com/SommaiGH/master-readme/blob/main/license.md)</u>.

**Note that** all other files such as input data files, as part of the manuscript entitled, *“Focal adhesion is associated with lithium response in bipolar disorder: evidence from a network-based multi-omics analysis"* published in MolecularPsychiatry [doi will be added] are under **a CC BY 4.0 license (Creative Commons Attribution 4.0 International license)**.
 

------------------------------------------------------------------------

## Citation

If you use the code from this project, please cite with **the Council of Science Editors (CSE)** citation styles as an example below.

    CSE Bibliography Format:   
    
    Niemsiri V, Rosenthal SB, Fisch KM, and Kelsoe JR. 2022. Bipolar Disorder and Lithium Response. San Francisco (CA): GitHub; [accessed 2022 Jun 6]. https://github.com/vniems/BD-Lithium.

------------------------------------------------------------------------

## References

*Will be provided.*



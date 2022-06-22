---
title: "R Notebook"
output:
  html_document:
    toc: true
    toc_depth: 5
    toc_float: true
    df_print: kable
    theme: spacelab
  pdf_document:
    toc: true
    toc_depth: 5
  html_notebook:
    toc: true
    toc_depth: 5
    toc_float: true
---

```{r include=FALSE}
setwd("~/Documents/Bar Plot_R/RNA-seq_reanalysis_May2022/Test")
```

```{r include=FALSE}
install.packages("R.utils", repos = "http://cran.us.r-project.org")
```

```{r include=FALSE}
install.packages("gplots", repos = "http://cran.us.r-project.org",dependencies = T)
```

```{r include=FALSE}
install.packages("dplyr", repos = "http://cran.us.r-project.org",dependencies = T, force = T)
```

```{r include=FALSE}
install.packages("gdata", repos = "http://cran.us.r-project.org",dependencies = T, force =T)
```

```{r include=FALSE}
install.packages('knitr', repos = "http://cran.us.r-project.org")
install.packages("kableExtra", repos = "http://cran.us.r-project.org")
install.packages('rmarkdown', repos = "http://cran.us.r-project.org")
install.packages('htmltools', repo = "http://cran.us.r-project.org")
```

```{r include=FALSE}
library(knitr)
library(kableExtra)
library(rmarkdown)
library(htmltools)
```

```{r include=FALSE}
options(knitr.table.format = "html")
```

```{r include=FALSE}
#set global option to get html table format!!!
```

# Data for RNA-Seq Differential Expression Analysis of iPSC-Derived Neurons
<br>

Here, we described the data that had been used for the "RNA-Seq Differential expression analysis" created by Kathleen Fisch, Ph.D. (CCBB), as shown [<u>here</u>](https://github.com/vniems/BD-Lithium/tree/main/DIRECTORIES/STEP2-RNASeq).

Detailed study workflow and methodology were described in the *'Method section'* and *'Supplemental Methods'* of the manuscript.

<br>


### 1. Metadata

-   The Metadata represents phenotypic data of samples.

-   *Samples* are referred to induced pluripotent stem cells (iPSC)-derived neurons obtained from patients with bipolar disorders (BD) and controls. These iPSC-derived neurons were characterized into "3 groups": *Li responders (LR)*, *Li non-responders (NR)* (based on the response to lithium treatment in BD patients), and *controls (CT)*.

-   *Conditions* are defined as "*in vitro* exposure" (treatment) to either lithium (Li) or valproate (VPA) and "no exposure" (no treatment [CTRL]).

-   File name: `kelsoe_metadata_111.csv` can be found in [<strong><u>the RNASeq input subdirectory</u></strong>](https://github.com/vniems/BD-Lithium/upload/main/DIRECTORIES/STEP2-RNASeq).

-   In addition, **the Metadata** was also deposited in [**GEO Series accession number GSE205422**](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205422).

<br>
<!-- -->

```{r}
#Read in metadata
meta <- read.csv("kelsoe_metadata_111.csv", stringsAsFactors=FALSE)
```

```{r include=FALSE}
#Show table header
head(meta)
```

``` r
#Show table header
head(meta)
```

```{r include=FALSE}
#Table S3
S3 <- head(meta)
write.table(S3, file = "S3_head_meta.csv")

#install.packages("kableExtra")
#library(kableExtra)
```

```{r include=FALSE}
options(knitr.table.format = "html")
S3 %>%
  kbl(format = "html") %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed","responsive")) %>%
  scroll_box(height = "500px") %>%
  save_kable(file = "S3_head_meta.html", self_contained = T)
```

```{r eval=FALSE, include=FALSE}
head(meta)
```

```{r echo=FALSE}
kbl(S3, format = "html",self_contained = T) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed","responsive")) %>%
  scroll_box( width = "800px")
```

<br>

### 2. Transcriptomic data

-   The transcriptomic data was the data after the quality controls and alignment process.

-   File name: `all_genes_results_111.txt`.

-   Note that we <u>did not</u> stored **the transcriptomic file** <u>here</u>, however the raw data can be found in [**GEO Series accession number GSE205422**](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205422), same as the Metadata.

-   The transcriptomic input file format was extracted and described below.

<br>
<!-- -->

```{r}
#Read in all_gene_results
genes_rsem_new <- read.csv("all_genes_results_111.txt", sep="\t", stringsAsFactors=FALSE)
```

```{r include=FALSE}
#Table S1
S1 <- head(genes_rsem_new)
write.table(S1, file = "S1_genes_rsem_new.csv")

#install.packages("kableExtra")
#library(kableExtra)
```

```{r include=FALSE}
options(knitr.table.format = "html")
S1 %>%
  kbl(format = "html") %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed","responsive")) %>%
  scroll_box(width = "800px", height = "500px") %>%
  save_kable(file = "S1_genes_rsem_new.html", self_contained = T)
```

``` r
#Show table header
head(genes_rsem_new)
```

```{r eval=FALSE, include=FALSE}
head(genes_rsem_new)
```

```{r echo=FALSE}
kbl(S1, format = "html",self_contained = T) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed","responsive")) %>%
  scroll_box(width = "800px")
```
<p> <p>
<!-- -->

<!-- -->

```{r include=FALSE}
#The columns of (genes_rsem_new) showed gene id and transcriptomic data for each of the samples
#Example: 
colnames(head(genes_rsem_new)[1:20])
```
```{r echo=TRUE}
ncol(genes_rsem_new)
```


``` r
#The columns of (genes_rsem_new) showed gene id and transcriptomic data for each of the samples
#Example: 
colnames(head(genes_rsem_new))
```
```{r include=FALSE}
colnames(head(genes_rsem_new))
```

```{r include=FALSE}
#Table S2
S2 <- colnames(head(genes_rsem_new))
write.table(S2, file = "S2_colnames_head_genes_rsem_new.csv")

#install.packages("kableExtra")
#library(kableExtra)
```

```{r include=FALSE}
options(knitr.table.format = "html")
S2 %>%
  kbl(format = "html") %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed","responsive")) %>%
  scroll_box(width = "800px", height = "500px") %>%
  save_kable(file = "S1_genes_rsem_new.html", self_contained = T)
```

```{r eval=FALSE, include=FALSE}
kbl(S2[1:20], format = "html", self_contained = T) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed","responsive")) %>%
  scroll_box(width = "800px", height = "500px")
```
```{r echo=FALSE}
kbl(S2, format = "html", self_contained = T) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed","responsive")) %>%
  scroll_box(width = "800px", height = "500px")
```

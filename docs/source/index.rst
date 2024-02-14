Welcome to SCALT's documentation!
=================================

**SCALT** provides a collection of python utilities that can be used to:

1. **classify** individual cells from single cell RNA seq experiments at **single cell** resolution level taking the advantage of a **maximum likelihood-based** approach and a collection of pre-compiled cell type specific lists of genes constructed by extensive re-analysis of comprehensive and expert curated catalogues; 
2. build cell type specific **lists of genes** starting from a **count matrix** and the correspoding **annotation** for each cell in a **deterministic** fashion;
3. build cell type specific **lists of genes** starting from a **count matrix** and a a gathering of **user-defined** cell type specific lists of genes making the use of an **hypergeometric** test.

SCALT is composed of 3(+1) utilities each corresponding to a different workflow previously mentioned. The application requires files to be formatted in the formats required by SCALT.

If needed, **format2TSV.py** can convert single cell RNA sequencing data files from either **.rds**, **.RData** or **.h5ad** to **.tsv**. Then, each service can be executed with just few commands:

1. **SCALT.py** to annotate single cell RNA sequencing data;
2. **SCALT_AnnotationListsBuilder.py** to generate the cell type specific lists of genes from annotated data;
3. **SCALT_NaiveListsBuilder.py** to generate the cell type specific lists of genes from user-defined lists of genes.

Please see the manual for point to point instructions and tips for the execution of SCALT.

.. toctree::
   :maxdepth: 2
   :caption: SCALT in brief
   
   intro.rst

.. toctree::
   :maxdepth: 2
   :caption: SCALT workflows
   
   workflows.rst


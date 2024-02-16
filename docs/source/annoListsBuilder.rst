Inputs formats
==============

SCALT_AnnotaionListsBuilder.py demands two inputs:

1. a scRNA seq row counts matrix. The matrix must be in .**tsv** extension pesenting;
2. a table having **one column** in which the annotation of each cell present in the counts is reported.

The counts matrix must present genes on the rows and cells on the columns. The first row of the matrix must contain the ids of each cell while the first column must provide the gene ids written either as **gene symbol** or **ensembl id**. To see an example of the table, see the section **SCALT: CLASSIFICATION - Inputs & Outputs** of this manual.

An example of the annotation table is reported here:

.. list-table:: 
   :align: center
   :widths: 80 
   :header-rows: 1

   * - annotation
   * - acinar
   * - beta
   * - beta
   * - alpha
   * - alpha
   * - alpha

Parameters
==========

Run SCALT_AnnotaionListsBuilder.py
==================================

Outputs
=======

Workflow
========

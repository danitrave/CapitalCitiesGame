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

SCALT_AnnotaionListsBuilder.py takes the advantage of a collection of both arguments and parameters that can visualized typing the following command:

:: 

  python3 SCALT_AnnotaionListsBuilder.py -h

The documentation should appear as follows:

::

   usage: SCALT_AnnotaionListsBuilder.py [-h] [-Boo --Boostraps] [-Cells --Cells]
                                      [-Genes --Genes] [-Notation --Notation]
                                      [-CPUs --CPUs]
                                      Sample Annotation

Run SCALT_AnnotaionListsBuilder.py
==================================

Outputs
=======

Workflow
========

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


1. **Sample** is the first positional argument and addresses the name of the counts matrix;
2. **Annotation** is the second positional argument and refers to the name of the annotation table;
3. **-Boo** or **--Boostraps** indicates the number of boostrap samples to generate. The default number is **100**;
4. **-Cells** or **--Cells** specifies the number of cells to pick randomly per each cell type during the probability inference process. By default, the number is set to **100**;
5. **-Genes** or **--Genes** refers to the number of genes that the final cel type lists of genes must contain at the end. The default number is **100**;
6. **-Notation** is used to underline the kind of gene notation present in the counts. The user can choose between **gene_symbol** or **ensembl_id**. By default, ensembl_id is set;
7. **-CPUs** or **--CPUs** indicates the number of processors to use. By default, **1** is used.


Run SCALT_AnnotaionListsBuilder.py
==================================

Outputs
=======

Workflow
========

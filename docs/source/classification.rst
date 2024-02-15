Inputs & Outputs
================

SCALT.py requires a scRNA seq row counts matrix as input data. The matrix must be in **.tsv** extension pesenting:

1. genes on the rows;
2. cells on the columns.

The first row of the matrix must contain the ids of each cell while the first column must provide the gene ids expressed either in **gene symbol** or **ensembl id**. 

An example of the input file is reported below.

.. list-table::  
   :widths: 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
   :header-rows: 1

   * - genes/cells
     - 1 
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 10
     - 1
     - 0
     - 11
     - 7
     - 0
     - 0
     - 0
     - 1
     - 1
     - 1
   * - ENSG00000160072
     - 0
     - 0
     - 1
     - 5
     - 7
     - 0
     - 0
     - 1
     - 9
     - 0 
     - 10
     - 1
     - 0
     - 11
     - 2
     - 0
     - 0
     - 0
     - 1
     - 1
   * - ENSG00000142611
     - 4
     - 10
     - 0
     - 0
     - 0
     - 0
     - 1
     - 3
     - 1
     - 12
     - 10
     - 1
     - 0
     - 9
     - 7
     - 0
     - 0
     - 0
     - 0
     - 4
   * - ENSG00000157911
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0 
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
   * - ENSG00000142655
     - 0
     - 0
     - 0
     - 0
     - 16
     - 14
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
     - 20
     - 0
     - 0
     - 0
     - 0
     - 0
     - 0
   * - ENSG00000149527
     - 1
     - 1
     - 3
     - 2
     - 1
     - 2
     - 0
     - 1
     - 0
     - 5
     - 1
     - 1
     - 0
     - 2
     - 3
     - 1
     - 0
     - 5
     - 1
     - 1

SCALT parameters
================

The list of arguments and paramenters can be visualized typing the following command:

:: 

  python3 SCALT.py -h

The visualized documentation should appear as follows:

::

  usage: SCALT.py [-h] [-Min --Threshold] [-Notation --Notation]
                [-Types --Types] [-CPUs --CPUs]
                Sample

1. **Sample** is the only positional argument of the tool. It represents the name of the counts matrix;
2. **-Min** or **--Threshold** is the minimum number of genes that a cell must express to be classified. The **default** value is **250**;
3. **-Notation** or **--Notation** is the type of gene notation to use. The defaul is **ensembl id**. Instead, write **gene_symbol** to switch to gene symbol notation;
4. **-Types** or **--Types** is the directory name containg the lists of the cell types to use in the likelihood test. By default, only the pre-compiled lists (DISCO, HPA) are used. To use only the custom lists generated from annotation, insert **custom**. Finally, to utilize only the custom lists generated from the user-defined lists, insert **naive**;
5. **-CPUs** or **--CPUs** is number of processors employed. The default is **1**;
6. **-h** or **--help** shows the documentation.

Run SCALT
=========

Report
======

For impatient people
====================

The tool must be executed on a Conda envirnoment which can be installed following the steps reported in the **prerequisites** section of this manual.

SCALT requires a scRNA counts matrix in **.tsv** format reporting genes on the rows and cells ids on the columns and the program to be excecuted is called **SCALT.py** 

SCALT classifies each cell to one of the 471 cell types available using the followinmg command:

::

   python3 SCALT.py read_counts.tsv 

The outpus are:

1. a **REPORT.html** file reporting a collection of plots that summarize the results of the experiment;
2. a directory called **results_directory** which contains all the metadata originated from the analysis. 

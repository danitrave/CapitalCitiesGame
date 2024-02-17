Advanced use cases
==================

SCALT is quite versative since it allows to mix the different utilities depending on the needs of the user.
The following instructions refer to advanced strategies which go behyond classifying cells or generate cell type specific list of genes.

Use custom lists in SCALT.py
----------------------------

Suppose that the pipeline of **SCALT_AnnotaionListsBuilder.py** was exploit to generate the cell type specific lists of genes from an annotation file. The idea is to use these lists of genes for classification. Therefore, the directory of lists of SCALT.py must be changed. 

This can be achieved adjusting a parameter of the classifier in this way:

::

  `python3 SCALT.py new_read_counts.tsv -Types custom -Notation gene_symbol -Min 300 -CPUs 2`

Or

::

  `python3 SCALT.py new_read_counts.tsv --Types custom --Notation gene_symbol --Threshold 300 --CPUs 2`

Changin the paratemter value of **Types** to **custom** forces SCALT.py to use the lists of genes originated from the annotation file as reference lists for classification.

:: note

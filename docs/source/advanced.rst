Advanced utilities
==================

SCALT presents other utilities behyond single cell classification:

1. the tool makes use of a scRNA seq read counts matrix and the corresponding **cells annotation** to build series of equally-sized cell type specific lists of genes, one per each cell type present in the annotation, in a deterministic fashion. This method is free of any human interpretation bias and relies on the ground concept on which SCALT is build which is that *each cell type has its own probability of expressing a gene*;
2. the application is able to build a series of equally-sized cell type specific lists of genes in a deterministic fashio starting from a scRNA seq read counts matrix and a collection of **user-defined lists of genes**, one per each hypothetical cell type. In first place, this method employes the counts matrix and the lists of genes proposed in the input in an **hypergeometric test** to produce a first layer of annotation. The so-called **naive** annotaion and the original counts matrix are subsequently utilized as inputs for utility described in the previous point.

Plese, follow the next sections of the manual for instructions and tips.

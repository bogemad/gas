# GAS (Genbank Annotation Statistics)
Basic annotation statistics for eukaryotic genomes using Genbank files.

## Statistics currently calculated:

```
Total predicted genes
Total predicted mRNA
Total predicted tRNA
Total predicted rRNA
Total predicted CDS
Percentage coding  
Total sequence length  
Percentage GC  
Longest gene  
Shortest gene  
Total gene length  
Average gene length  
Average gene CDS length  
Gene density (genes/Mb)  
Percentage coding genes with introns  
Total exon length  
Total number of exons 
Longest exon  
Shortest exon  
Average exon length  
Exon percentage GC  
Total intron length  
Total number of introns  
Longest intron  
Shortest intron  
Average intron length  
Average introns per gene  
Intron percent GC  
Total intergenic length  
Total intergenic regions  
Longest intergenic region  
Shortest intergenic region  
Average intergenic length  
Intergenic percent GC  
```

## Usage:

```
usage: gas [-h] [-o OUT] [-g GBKS [GBKS ...]]  

GAS (Genbank Annotation Statistics): Basic annotation statistics for eukaryotic genomes from Genbank files.  

options:  
  -h, --help          show this help message and exit  
  -o OUT              Output file  
  -g GBKS [GBKS ...]  GenBank files for annotation stats. As many as you like.  
```

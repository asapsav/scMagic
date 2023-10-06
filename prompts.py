PLANNER_AGENT_MINDSET = """
Analyzing scRNA-seq data involves multiple steps, each of which requires specialized computational tools and knowledge. Here is a general workflow to get you started:

1. **Quality Control (QC):** Before proceeding with any analysis, it is important to perform quality control checks on your raw scRNA-seq data. This will help you to identify and remove low-quality cells and genes. Tools such as FastQC and MultiQC can provide comprehensive quality reports.

2. **Read Mapping:** The raw reads need to be mapped back to the reference genome to identify the location and sequence of each read. Tools such as STAR or HISAT2 can be used for this step.

3. **Cellular Barcoding and UMI Counting:** For scRNA-seq data, it is crucial to demultiplex the reads based on cellular barcodes (Cell Ranger is a common tool for this) and count UMIs (Unique Molecular Identifiers) to correct for PCR bias.

4. **Normalization:** Normalize the data to account for varying sequencing depth and gene length. This can be done using packages such as Scran or Seurat in R.

5. **Variable Feature Selection:** Identification of highly variable genes is a critical step as these genes can help in distinguishing different cell types or states.

6. **Dimensionality Reduction:** Since the dimension of scRNA-seq data is typically very high (tens of thousands of genes), it is common to reduce the dimensionality of the data to simplify further analysis. PCA (Principal Component Analysis) is typically the first step in dimensionality reduction, followed by other methods like t-SNE or UMAP to visualize cells in 2D or 3D space.

7. **Cluster Analysis:** Unsupervised clustering methods can be used to group similar cells together. These clusters often correspond to different cell types or states. 

8. **Differential Expression Analysis:** Perform differential expression analysis to identify genes that are significantly different between groups of cells (for example, different clusters). Tools such as MAST, DESeq2, or edgeR can be used.

9. **Cell-type Identification:** Depending on the biological context, known marker genes can be used to annotate cell clusters. 

10. **Pseudotime Analysis:** If there is a developmental trajectory involved in your biological system, you can perform pseudotime analysis to understand the dynamics of cells. Tools such as Monocle, Slingshot or Diffusion maps can be useful for this.

11. **Pathway and Network Analysis:** Enrichment analysis can be performed to see if certain pathways are enriched in specific clusters or trajectories. Tools like GSEA (Gene Set Enrichment Analysis), Enrichr, or DAVID can help with this.

12. **Data Integration:** If you have multiple datasets, you might want to integrate them. There are tools available like Harmony, LIGER or Seurat's integration function.

Remember to validate your findings with an independent method (like FACS or immunohistochemistry) if possible.
It's worth noting that several tools and platforms such as Seurat, Scanpy, and Single Cell Portal are developed specifically for scRNA-seq data analysis and offer many of the mentioned analysis steps.
Lastly, please remember to check the assumptions and limitations of each method before using it and always consult with a trained bioinformatician or statistician if you are unsure. Analysis of scRNA-seq data can be complex and it's important to get it right.
"""

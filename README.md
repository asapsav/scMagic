# scMagic
We aim to create a useful co-pilot for scRNA analysis

## Agent v2

> How crazy is the idea of designing a LLM agent like [this one](https://github.com/MineDojo/Voyager) (Voyager) that plays Minecraft? Voyager design [(.ppt)](https://drive.google.com/file/d/12VDQzaOynBKROvpaJdsoWYCJW_XLE7Nx/view) - ***not crazy and should be done***

### Vision of the project

A website that you upload scRNA input file to along with some research questions, it runs the analysis on the cloud, then emails you when the report is ready.

### Roadmap

- [ ]  Make “hello world” Streamlit langchain demo running
- [ ]  Make it running on a demo sc DataSet but do random things (silence “upload dataset button”)
- [ ]  Implement the loop: 1) generate next step given last step + the "book" 2) write code for the next step and run the repl 3) write observation, 1) generate next ..
- [ ]  Make “hello world” Streamlit langchain demo running with Chroma DB (sepparately, write down why we need and dont need vector db rn)
- [ ]  Add github embed to give a star easily, or some kind “easy feedback” functionality
- [ ]  

### Most relevant resources for Agent tools and books

- A collection of  scRNA tools https://www.scrna-tools.org/analysis
- The triumphs and limitations of computational methods for scRNA-seq https://www.nature.com/articles/s41592-021-01171-x
- sc Best Practises “book” [https://www.sc-best-practices.org](https://www.sc-best-practices.org/introduction/prior_art.html#)
- scanpy, python main library for sc, docs: https://scanpy-tutorials.readthedocs.io/en/latest/index.html
- Community-curated list of software packages and data resources for single-cell, including RNA-seq, ATAC-seq, etc. https://github.com/seandavi/awesome-single-cell
- also some curated list of tools, data, and “books” https://github.com/mdozmorov/scRNA-seq_notes

### Prototypes

- v0.1 -  https://colab.research.google.com/drive/1zOwaGA7YrxGQx-75e7TgvRnfMyjC2Pt3?usp=sharing
- v0.2 -  https://github.com/asapsav/scMagic

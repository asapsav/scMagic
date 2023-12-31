# scMagic
AI co-pilot for scRNA-seq analysis. Serves as valuable tool that can handle computational and data-driven tasks, leaving researchers more time for conceptual work.
> This repository is, I cannot stress this enough, very experimental. Do not use it as a dependency.

## Who?
- Savelii K - B.S. Physics MIPT, M.S CS Duke, xMcKinsey
- Evgenii K - M.S. Physics MIPT, PhD Harvard Medical School

## What?
### v0.3 vision
1) Upload scRNA-seq data, research background, research questions, things to try and things to be aware of.
2) LLM agent-based AI runs the analysis on the cloud, then emails you when the report is ready.
Manifesto:
* usefull AI <=> 1) reliable 2) result-interpretable

## Why?
To advance AI alingment we want to learn how to solve complex planning and design problems. scRNA-seq analyis is one of those problems, that this team happens to have exposure to.

### Roadmap

- [x]  Make “hello world” Streamlit langchain demo running
- [ ]  Make it running on a demo sc data but do random things (silence “upload dataset button”)
- [ ]  Implement the loop: 1) generate next step given last step + the "book" 2) write code for the next step and run the repl 3) write observation, 1) generate next ..
- [ ]  Make “hello world” Streamlit langchain demo running with Chroma DB (sepparately, write down why we need and dont need vector db rn)
- [ ]  Add functionality “easy feedback” 
- [x]  OD on cheap coffee and twix chocoalte bars and come up with a new general problem-solver architecture
- [ ] Make a completely open source version using Llama v2 functions calling API by Ed
- [ ] Expand agents tools to include scRNA-seq foundational models
- [ ] Expand agents tools to include writing and excecuding Python code (REPL)
- [ ] Expand agents tools to include wrtie and excecude R code
- [ ] Expand agetns tools to include read and write "ToT" = tree of though
- [ ] Expand agents tools to include planning tool
- [ ] Expand agents tools to predict complexity of the question (incorporate system 1 and 2 thinking)
- [ ] Expand agents tools to include "setting up dev environments"
- [ ] Incorporate "exploration" or balance "horisontal vs vertical research strategy"
- [ ] Redundancy (Shuttle computers)
- [ ] 1) Optimise chain
- [ ] 2) Optimise prompts
- [ ] 3) Optimise models (PERF / RL)
- [ ] 4) Attempt cost saving meaures (smaller models, smaller prompts, smaller chain loops, remove unnessesary chain loops (sepparate startup lol))

### Some relevant resources for agents to use

- A collection of  scRNA tools https://www.scrna-tools.org/analysis
- The triumphs and limitations of computational methods for scRNA-seq https://www.nature.com/articles/s41592-021-01171-x
- sc Best Practises “book” [https://www.sc-best-practices.org](https://www.sc-best-practices.org/introduction/prior_art.html#)
- scanpy, python main library for sc, docs: https://scanpy-tutorials.readthedocs.io/en/latest/index.html
- Community-curated list of software packages and data resources for single-cell, including RNA-seq, ATAC-seq, etc. https://github.com/seandavi/awesome-single-cell
- also some curated list of tools, data, and “books” https://github.com/mdozmorov/scRNA-seq_notes
- A collection of sc studies with input data and papers https://singlecell.broadinstitute.org/single_cell
- BioTuring database of scRNA-seq and notebooks https://datascience.bioturing.com/notebook

### Prototypes

- v0.1 -  https://colab.research.google.com/drive/1zOwaGA7YrxGQx-75e7TgvRnfMyjC2Pt3?usp=sharing
- v0.2 -  https://github.com/asapsav/scMagic

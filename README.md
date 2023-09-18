# scMagic
We aim to create a useful co-pilot for scRNA-seq analysis
> This repository is, I cannot stress this enough, very experimental. Do not use it as a dependency.

## Who?
- Savelii K - B.S. Physics MIPT, M.S CS Duke, xMcKinsey
- Evgenii K - M.S. Physics MIPT, PhD Harvard Medical School

## What?
### v0.2 vision

1) Upload scRNA-seq inputs along with some research questions
2) LLM agent-based AI runs the analysis on the cloud, then emails you when the report is ready.

## Why?
To advance alinged AI we want to train it to solve complex planning and creativity problems. scRNA-seq analyis is one of those problems, that we feel competitive advantage in.

### Roadmap

- [x]  Make “hello world” Streamlit langchain demo running
- [ ]  Make it running on a demo sc data but do random things (silence “upload dataset button”)
- [ ]  Implement the loop: 1) generate next step given last step + the "book" 2) write code for the next step and run the repl 3) write observation, 1) generate next ..
- [ ]  Make “hello world” Streamlit langchain demo running with Chroma DB (sepparately, write down why we need and dont need vector db rn)
- [ ]  Add github embed to give a star easily, or some kind “easy feedback” functionality
- [x]  OD on cheap coffee and twix chocoalte bars and come up with a new general problem-solver architecture
- [ ] Make a completely open source version using Llama v2 functions calling API by Ed

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

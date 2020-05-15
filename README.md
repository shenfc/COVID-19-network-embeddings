# covid-19-network-embeddings

We constructed network embeddings for COVID-19 by applying the node2vec model over a co-occurrence network derived from the CORD-19-on-FHIR datasets.

## Table of Contents
- [Visualization](#visualization)
- [Developers](#developers)

## Visualization

The network is visualized using [Bokeh](https://bokeh.org/) and is available
[here: https://www.davidoniani.com/covid-19-network](https://www.davidoniani.com/covid-19-network).

## Developers

Dr. Feichen Shen's COVID-19 research team: David Oniani and [Dr. Feichen Shen](https://www.mayo.edu/research/faculty/shen-feichen-ph-d/bio-20238745).

## Collaborators

Dr. Guoqian Jiang and Dr. Hongfang Liu

__Code References__

1. Original node2vec: Aditya Grover and Jure Leskovec. https://github.com/aditya-grover/node2vec

2. Implementation of node2vec: https://github.com/lucashu1/link-prediction

@misc{lucas_hu_2018_1408472,
   author       = {Lucas Hu and
                   Thomas Kipf and
                   Gökçen Eraslan},
   title        = {{lucashu1/link-prediction: v0.1: FB and Twitter 
                    Networks}},
   month        = sep,
   year         = 2018,
   doi          = {10.5281/zenodo.1408472},
   url          = {https://doi.org/10.5281/zenodo.1408472}
}


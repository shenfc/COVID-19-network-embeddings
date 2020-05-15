# covid-19-network-embeddings

We constructed network embeddings for COVID-19 by applying the node2vec model over a co-occurrence network derived from the CORD-19-on-FHIR datasets.

## Table of Contents
- [Quickstart](#quickstart)
- [Visualization](#visualization)
- [Developers](#developers)

## Quickstart

```sh
# Install dependencies
python3 -m pip install -r requirements.txt

# Generate data, in preprocessing folder
python3 generate_graph_data.py
python3 generate_edges_features_data.py

# Generate graph
python3 generate_graph.py

# Link prediction
python3 predict_links.py
```

## Visualization

The network is visualized using [Bokeh](https://bokeh.org/) and is available
[here: https://www.davidoniani.com/covid-19-network](https://www.davidoniani.com/covid-19-network).

## Developers

Dr. Feichen Shen's COVID-19 research team: David Oniani and [Dr. Feichen Shen](https://www.mayo.edu/research/faculty/shen-feichen-ph-d/bio-20238745).

# encoding: UTF-8

"""
Author:   David Oniani, Feichen Shen

Description:
    Build edges and features data files to then create a matrix.
"""

import os
import csv

import pandas as pd

from typing import Dict, List

DATA_DIR: str = "data"
DATA_FILE: str = "Combined-coronaVirusGraph.txt"

EDGES_DATA: str = "Combine_edges.csv"
FEATS_DATA: str = "Combine_features.csv"



def main() -> None:

    f_dict = open("/Users/m102853/Documents/pyWorkSpace/Covid19GraphMining/data/Combined_Dict.txt", "w+")

    """The main function. Data extraction is done here."""

    # Read the data
    graphDir = 'data/Combined-coronaVirusGraph.txt'
    graphfile = open(graphDir, 'r')
    lines = graphfile.readlines()
    nodes = []
    parents = []
    for l in lines:
        n1 = l.split(';')[0]
        n2 = l.split(';')[1]
        nodes.append(n1)
        parents.append(n2)

    # Create node encoding
    temp = list(nodes)
    temp.extend(parents)

    # NOTE: `all_nodes` defines the order in which the features data is built
    all_nodes: List[str] = []
    for item in temp:
        if item not in all_nodes:
            all_nodes.append(item)


    node_encoding: Dict[str, int] = {
        node: idx for idx, node in enumerate(all_nodes)
    }

    for k, v in node_encoding.items():
        results = str(k).strip() + ';' + str(v)
        f_dict.write(results+'\n')

    # Create edges file
    with open(os.path.join(DATA_DIR, EDGES_DATA), "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        # writer.writerow(["source_idx", "target_idx"])  # Header
        for node, parent in zip(nodes, parents):
            writer.writerow([node_encoding[node], node_encoding[parent]])
            #writer.writerow([node_encoding[parent], node_encoding[node]])

    # Creates features file
    with open(os.path.join(DATA_DIR, FEATS_DATA), "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(["idx", "source_idx", "feature"])  # Header
        for idx, node in enumerate(all_nodes):
            writer.writerow([idx, node_encoding[node], 0])


if __name__ == "__main__":
    main()

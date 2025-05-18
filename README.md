# Correlation Graph Visualization (GraphLation)

This repository presents a Python-based approach to construct and visualize correlation graphs using numerical variables. Pairwise Pearson correlation coefficients are used to weight the edges, and the resulting network is rendered using NetworkX and Matplotlib.

## Purpose

To facilitate exploratory analysis by representing linear associations between variables as a weighted undirected graph. This allows immediate identification of key variables and their interaction structure.

## Example: Synthetic Dataset

The dataset used in the example is synthetically generated to emulate variables with varying degrees of correlation. Each pair was manually defined to exhibit moderate to strong linear relationships.

### Graph 1: Main Connected Component

<img src="https://github.com/user-attachments/assets/5986e636-ead7-4d83-8dbe-bfba005c9f53" width="650" height="550">

- **Node border color** is determined by node degree (i.e., the number of edges connected to the variable).
- **Edge transparency (alpha)** reflects the absolute value of the Pearson correlation coefficient.
- **Correlation values** are printed at the center of each edge for interpretability.

The variable with the **highest degree** is placed centrally in the layout.

### Graph 2: Tertiary Structure

<img src="https://github.com/user-attachments/assets/6015c5e5-acdc-4ad9-a25a-bb25e2aa6a65" width="550" height="450">

An example of a minimal network with three nodes, where the most connected node appears centrally.

### Graph 3: Component with Only Two Variables

<img src="https://github.com/user-attachments/assets/0042bb7a-6bad-47bd-9883-7b6f8169aa7f" width="500" height="400">

When the graph contains only two variables, **no colorbar is rendered**, as degree-based visual scaling is not applicable.



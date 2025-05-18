# Correlation Graph Visualization (GraphLation)

This repository presents a Python-based approach to construct and visualize correlation graphs using numerical variables. Pairwise Pearson correlation coefficients are used to weight the edges, and the resulting network is rendered using NetworkX and Matplotlib.

## Purpose

To facilitate exploratory analysis by representing linear associations between variables as a weighted undirected graph. This allows immediate identification of key variables and their interaction structure.

## Example: Synthetic Dataset

The dataset used in the example is synthetically generated to emulate variables with varying degrees of correlation. Each pair was manually defined to exhibit moderate to strong linear relationships.

### Graph 1: Main Connected Component

![Main component](./8db52ca2-35dc-4ef5-b408-84b6822bd572.png)

- **Node border color** is determined by node degree (i.e., the number of edges connected to the variable).
- **Edge transparency (alpha)** reflects the absolute value of the Pearson correlation coefficient.
- **Correlation values** are printed at the center of each edge for interpretability.

The variable with the **highest degree** is placed centrally in the layout.

### Graph 2: Component with Only Two Variables

![Second component](./c3dab194-7655-4b7a-9a81-420afbd6f8bc.png)

When the graph contains only two variables, **no colorbar is rendered**, as degree-based visual scaling is not applicable.

### Graph 3: Tertiary Structure

![Third component](./d39e38df-f1c9-4d61-aad0-4257c20bd83a.png)

An example of a minimal network with three nodes, where the most connected node appears centrally.


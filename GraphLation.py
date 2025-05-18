import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.ticker import MaxNLocator
import networkx as nx

def GraphLation(df_all, l):
    vars_in_l = sorted(set([item for sublist in l for item in sublist]))
    df_sub = df_all[vars_in_l].copy()
    df_corr = df_sub.corr()

    G = nx.Graph()
    for u, v in l:
        if u in df_corr.columns and v in df_corr.columns:
            corr = df_corr.loc[u, v]
            G.add_edge(u, v, weight=round(corr, 2))
        else:
            G.add_edge(u, v)

    components = list(nx.connected_components(G))

    for i, comp in enumerate(components):
        G_sub = G.subgraph(comp).copy()

        degrees = dict(G_sub.degree())
        max_degree = max(degrees.values())
        central_nodes = [n for n, d in degrees.items() if d == max_degree]
        shells = [central_nodes, [n for n in G_sub.nodes if n not in central_nodes]]
        pos = nx.shell_layout(G_sub, nlist=shells)

        # Gradiente contínuo + normalização
        node_cmap = cm.get_cmap('viridis')
        node_norm = mcolors.Normalize(vmin=min(degrees.values()), vmax=max(degrees.values()))
        border_colors = [node_cmap(node_norm(degrees[n])) for n in G_sub.nodes]

        edge_weights = nx.get_edge_attributes(G_sub, 'weight')
        abs_corrs = [abs(w) for w in edge_weights.values()]
        min_corr = min(abs_corrs) if abs_corrs else 0
        max_corr = max(abs_corrs) if abs_corrs else 1
        alpha_range = (0.2, 1.0)

        def map_corr_to_alpha(corr):
            scaled = (abs(corr) - min_corr) / (max_corr - min_corr) if max_corr > min_corr else 1
            return alpha_range[0] + scaled * (alpha_range[1] - alpha_range[0])

        fig, ax = plt.subplots(figsize=(10, 8))

        for (u, v), weight in edge_weights.items():
            alpha = map_corr_to_alpha(weight)
            nx.draw_networkx_edges(
                G_sub, pos,
                edgelist=[(u, v)],
                ax=ax,
                edge_color='black',
                alpha=alpha,
                width=2
            )

        nx.draw_networkx_nodes(
            G_sub, pos,
            node_size=3000,
            node_color='white',
            edgecolors=border_colors,
            linewidths=4,
            ax=ax
        )

        nx.draw_networkx_labels(
            G_sub, pos,
            font_size=8,
            font_color='black',
            verticalalignment='center',
            horizontalalignment='center',
            ax=ax
        )

        edge_labels_fmt = {k: f"{v:.2f}" for k, v in edge_weights.items()}
        nx.draw_networkx_edge_labels(G_sub, pos, edge_labels=edge_labels_fmt, font_size=8, ax=ax)

        # Mostrar colorbar contínuo com apenas inteiros como ticks
        if max_degree > 1:
            sm1 = cm.ScalarMappable(cmap=node_cmap, norm=node_norm)
            sm1.set_array([])
            cbar1 = plt.colorbar(sm1, ax=ax, orientation='vertical', fraction=0.046, pad=0.02)
            cbar1.set_label('Number of Connected Vertices', rotation=270, labelpad=20)
            cbar1.locator = MaxNLocator(integer=True)
            cbar1.update_ticks()

        plt.axis('off')
        plt.tight_layout()
        plt.show()

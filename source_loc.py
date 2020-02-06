import networkx as nx
import numpy as np
import sys

import GLAD_MODIFIED.source_estimation as se
import operator

from multiprocessing import Pool
from termcolor import colored

### Compute a batch in parallel
def glad_modified(graph, obs_time, distribution) :
    mu = distribution.mean()
    sigma = distribution.std()
    obs = np.array(list(obs_time.keys()))


    path_lengths = {}
    paths = {}
    for o in obs:
        path_lengths[o], paths[o] = nx.single_source_dijkstra(graph, o)
    ### Run the estimation
    s_est, scores = se.ml_estimate(graph, obs_time, sigma, mu, paths,
        path_lengths)

    return (s_est, scores)

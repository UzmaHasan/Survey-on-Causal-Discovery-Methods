# coding=utf-8
# Copyright (C) 2021. Huawei Technologies Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This demo script aim to demonstrate
how to use MCSL algorithm in `castle` package for causal inference.

If you want to plot causal graph, please make sure you have already install
`networkx` package, then like the following import method.

Warnings: This script is used only for demonstration and cannot be directly
          imported.
"""
import pandas as pd
import numpy as np
from castle.common import GraphDAG
from castle.metrics import MetricsDAG
from castle.datasets import DAG, IIDSimulation
from castle.algorithms import MCSL


df = pd.read_csv("Asia.csv")
true_dag = np.load('Asia_TrueData.npy') # ground-truth, should be a numpy array

# mcsl learn
mc = MCSL(model_type='nn',
          iter_step=100,
          rho_thresh=1e20,
          init_rho=1e-5,
          rho_multiply=10,
          graph_thresh=0.5,
          l1_graph_penalty=2e-3)
mc.learn(df, pns_mask=true_dag)


# calculate accuracy
met = MetricsDAG(mc.causal_matrix, true_dag)
print(met.metrics)

# plot est_dag and true_dag
GraphDAG(mc.causal_matrix, true_dag)

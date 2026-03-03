# A Survey on Causal Discovery Methods for I.I.D. and Time Series Data

### Uzma Hasan, Emam Hossain, Md Osman Gani
Published in Transactions on Machine Learning Research (09/2023)

### Experimental Overview

The survey benchmarks causal discovery algorithms in two settings:

1. I.I.D. Data
2. Time-Series Data

Evaluation metrics reported in the paper:
- SHD (Structural Hamming Distance)
- TPR (True Positive Rate)
- FDR (False Discovery Rate)

### I.I.D. benchmarking (Section 7.1)
**Datasets:** ASIA, CHILD, ALARM, HEPAR2. Source: https://github.com/py-why/causal-learn (includes dataset csv files and ground-truth DAGs)

**Methods:** PC, GES, LiNGAM, Direct-LiNGAM, NOTEARS, DAG-GNN, GraN-DAG, GOLEM, MCSL.    

The implementations of the above benchmarked algorithms have been adopted from the **gCastle** repository. 

**Implementation source:**

Repository Link: https://github.com/huawei-noah/trustworthyAI/tree/master/gcastle

Code run:

1. PIP installation: `pip install gcastle==1.0.4rc1`
2. To test an algorithm (for example PC) run: `python pc_demo.py`

### Time-series benchmarking (Section 7.2)
**Datasets:** Syn-6 (lag=2), fMRI (lag=1). 

**Methods:** PCMCI, PCMCI+, VarLiNGAM, DyNOTEARS, TCDF.

The implementation of the above benchmarked algorithms have been adopted from the following respective repositories. The step-by-step instructions to run the algorithms are available in those repositories.

**Implementation sources:**

PCMCI and PCMCI+:      https://github.com/jakobrunge/tigramite

VarLiNGAM and DyNOTEARS:      https://github.com/ckassaad/causal_discovery_for_time_series 

TCDF:      https://github.com/M-Nauta/TCDF

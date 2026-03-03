# A Survey on Causal Discovery Methods for I.I.D. and Time Series Data

This repository compiles and organizes the code needed to reproduce the **experiment section (Section 7)** from:

**Uzma Hasan, Emam Hossain, Md Osman Gani.**  
*A Survey on Causal Discovery Methods for I.I.D. and Time Series Data.* (TMLR, 09/2023).

## What’s included

### I.I.D. benchmarking (Section 7.1)
**Datasets:** ASIA, CHILD, ALARM, HEPAR2. The CSV version of the datasets and their corresponding ground-truths are available in the **causallearn repository**: https://github.com/py-why/causal-learn

**Methods:** PC, GES, LiNGAM, Direct-LiNGAM, NOTEARS, DAG-GNN, GraN-DAG, GOLEM, MCSL.    

### Time-series benchmarking (Section 7.2)
**Datasets:** Syn-6 (lag=2), fMRI (lag=1). 

**Methods:** PCMCI, PCMCI+, VarLiNGAM, DyNOTEARS, TCDF.


## Quickstart

### I.I.D. experiments

The implementations of the following benchmarked algorithms (PC, GES, LiNGAM, Direct-LiNGAM, NOTEARS, DAG-GNN,GraN-DAG, GOLEM, and MCSL) have been adopted from the **gCastle** repository. 

**Implementation source:**

Repository Link: https://github.com/huawei-noah/trustworthyAI/tree/master/gcastle

1. PIP installation: pip install gcastle==1.0.4rc1
2. To test an algorithm (for example PC) run: python pc_demo.py

### Time-series experiments

The implementation of the baseline algorithms (PCMCI, PCMCI+, VarLiNGAM, DyNOTEARS, TCDF) have been adopted from the following respective repositories. The instructions to run the algorithms are available in those repositories.

**Implementation sources:**

PCMCI and PCMCI+:      https://github.com/jakobrunge/tigramite

VarLiNGAM and DyNOTEARS:      https://github.com/ckassaad/causal_discovery_for_time_series 

TCDF:      https://github.com/M-Nauta/TCDF

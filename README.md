# A Survey on Causal Discovery Methods for I.I.D. and Time Series Data

This repository compiles and organizes the code needed to reproduce the **experiment section (Section 7)** from:

**Uzma Hasan, Emam Hossain, Md Osman Gani.**  
*A Survey on Causal Discovery Methods for I.I.D. and Time Series Data.* (TMLR, 09/2023).  :contentReference[oaicite:20]{index=20}

## What’s included

### I.I.D. benchmarking (Section 7.1)
**Datasets:** ASIA, CHILD, ALARM, HEPAR2 (with ground-truth). :contentReference[oaicite:21]{index=21}  
**Methods:** PC, GES, LiNGAM, Direct-LiNGAM, NOTEARS, DAG-GNN, GraN-DAG, GOLEM, MCSL. :contentReference[oaicite:22]{index=22}  
**Implementation source:** adopted from **gCastle** (Huawei TrustworthyAI).   

### Time-series benchmarking (Section 7.2)
**Datasets:** Syn-6 (lag=2), fMRI (lag=1). :contentReference[oaicite:24]{index=24}  
**Methods:** PCMCI, PCMCI+, VarLiNGAM, DyNOTEARS, TCDF. :contentReference[oaicite:25]{index=25}  
**Implementation sources:**
- Tigramite (PCMCI / PCMCI+): https://github.com/jakobrunge/tigramite :contentReference[oaicite:26]{index=26}  
- causal_discovery_for_time_series (VarLiNGAM / DyNOTEARS): https://github.com/ckassaad/causal_discovery_for_time_series :contentReference[oaicite:27]{index=27}  
- TCDF: https://github.com/M-Nauta/TCDF :contentReference[oaicite:28]{index=28}  

## Quickstart

### 1) Create environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

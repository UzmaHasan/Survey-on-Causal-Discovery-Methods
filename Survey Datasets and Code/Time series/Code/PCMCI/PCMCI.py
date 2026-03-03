# Imports
import numpy as np
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
#%matplotlib inline     
## use `%matplotlib notebook` for interactive figures
# plt.style.use('ggplot')
import sklearn

import tigramite
from tigramite import data_processing as pp
#from tigramite.toymodels import structural_causal_processes as toys

from tigramite import plotting as tp
from tigramite.pcmci import PCMCI
from tigramite.independence_tests import ParCorr, GPDC, CMIknn, CMIsymb

df1 = pd.read_csv('Dataset_x6.csv')

data = np.array(df1)
#var_names=['wind_10m', 'specific_humidity', 'LW_down', 'SW_down', 'rainfall', 'snowfall', 'sosaline', 'sst', 't2m', 'surface_pressure', 'sea_ice_extent']
var_names=['v1', 'v2', 'v3', 'v4', 'v5', 'v6']							

dataframe = pp.DataFrame(data, 
                         datatime = {0:np.arange(len(data))}, 
                         var_names=var_names)
max_lag = 2
parcorr = ParCorr(significance='analytic')
pcmci = PCMCI(
    dataframe=dataframe, 
    cond_ind_test=parcorr,
    verbosity=1)

pcmci.verbosity = 1
results = pcmci.run_pcmci(tau_max=2, pc_alpha=None, alpha_level=0.01) #tau_max = maximum lag 

print(results)

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:07:11 2019

@author: ThinkPad
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import scipy.stats as stats# t-test 

path_p = r'I:\环渤海\未来气象\analysis'

#database
dt_ac_tmin = pd.read_csv(path_p + '\\' + 'ac_45_tmin.csv',engine='python')
dt_cn_tmin = pd.read_csv(path_p + '\\' + 'cn_45_tmin.csv',engine='python')
dt_gf_tmin = pd.read_csv(path_p + '\\' + 'gf_45_tmin.csv',engine='python')
dt_gi_tmin = pd.read_csv(path_p + '\\' + 'gi_45_tmin.csv',engine='python')
dt_mp_tmin = pd.read_csv(path_p + '\\' + 'mp_45_tmin.csv',engine='python')

p_tmin_1, p_tmin_2, p_tmin_3, p_tmin_4, p_tmin_5, p_tmin_6, p_tmin_7, p_tmin_8, p_tmin_9, p_tmin_10,  p_tmin_11, p_tmin_12 = [],[],[],[],[],[],[],[],[],[],[],[],
##loop
for i in range(76):
    _, p_tmin1 = stats.ttest_ind([dt_ac_tmin.tasmin0801[i],dt_cn_tmin.tasmin0801[i],dt_gf_tmin.tasmin0801[i],dt_gi_tmin.tasmin0801[i],dt_mp_tmin.tasmin0801[i]],
                               [dt_ac_tmin.tasmin210001[i],dt_cn_tmin.tasmin210001[i],dt_gf_tmin.tasmin210001[i],dt_gi_tmin.tasmin210001[i],dt_mp_tmin.tasmin210001[i]])
    _, p_tmin2 = stats.ttest_ind([dt_ac_tmin.tasmin0802[i],dt_cn_tmin.tasmin0802[i],dt_gf_tmin.tasmin0802[i],dt_gi_tmin.tasmin0802[i],dt_mp_tmin.tasmin0802[i]],
                               [dt_ac_tmin.tasmin210002[i],dt_cn_tmin.tasmin210002[i],dt_gf_tmin.tasmin210002[i],dt_gi_tmin.tasmin210002[i],dt_mp_tmin.tasmin210002[i]])
    _, p_tmin3 = stats.ttest_ind([dt_ac_tmin.tasmin0803[i],dt_cn_tmin.tasmin0803[i],dt_gf_tmin.tasmin0803[i],dt_gi_tmin.tasmin0803[i],dt_mp_tmin.tasmin0803[i]],
                               [dt_ac_tmin.tasmin210003[i],dt_cn_tmin.tasmin210003[i],dt_gf_tmin.tasmin210003[i],dt_gi_tmin.tasmin210003[i],dt_mp_tmin.tasmin210003[i]])
    _, p_tmin4 = stats.ttest_ind([dt_ac_tmin.tasmin0804[i],dt_cn_tmin.tasmin0804[i],dt_gf_tmin.tasmin0804[i],dt_gi_tmin.tasmin0804[i],dt_mp_tmin.tasmin0804[i]],
                               [dt_ac_tmin.tasmin210004[i],dt_cn_tmin.tasmin210004[i],dt_gf_tmin.tasmin210004[i],dt_gi_tmin.tasmin210004[i],dt_mp_tmin.tasmin210004[i]])
    _, p_tmin5 = stats.ttest_ind([dt_ac_tmin.tasmin0805[i],dt_cn_tmin.tasmin0805[i],dt_gf_tmin.tasmin0805[i],dt_gi_tmin.tasmin0805[i],dt_mp_tmin.tasmin0805[i]],
                               [dt_ac_tmin.tasmin210005[i],dt_cn_tmin.tasmin210005[i],dt_gf_tmin.tasmin210005[i],dt_gi_tmin.tasmin210005[i],dt_mp_tmin.tasmin210005[i]])
    _, p_tmin6 = stats.ttest_ind([dt_ac_tmin.tasmin0806[i],dt_cn_tmin.tasmin0806[i],dt_gf_tmin.tasmin0806[i],dt_gi_tmin.tasmin0806[i],dt_mp_tmin.tasmin0806[i]],
                               [dt_ac_tmin.tasmin210006[i],dt_cn_tmin.tasmin210006[i],dt_gf_tmin.tasmin210006[i],dt_gi_tmin.tasmin210006[i],dt_mp_tmin.tasmin210006[i]])
    _, p_tmin7 = stats.ttest_ind([dt_ac_tmin.tasmin0807[i],dt_cn_tmin.tasmin0807[i],dt_gf_tmin.tasmin0807[i],dt_gi_tmin.tasmin0807[i],dt_mp_tmin.tasmin0807[i]],
                               [dt_ac_tmin.tasmin210007[i],dt_cn_tmin.tasmin210007[i],dt_gf_tmin.tasmin210007[i],dt_gi_tmin.tasmin210007[i],dt_mp_tmin.tasmin210007[i]])
    _, p_tmin8 = stats.ttest_ind([dt_ac_tmin.tasmin0808[i],dt_cn_tmin.tasmin0808[i],dt_gf_tmin.tasmin0808[i],dt_gi_tmin.tasmin0808[i],dt_mp_tmin.tasmin0808[i]],
                               [dt_ac_tmin.tasmin210008[i],dt_cn_tmin.tasmin210008[i],dt_gf_tmin.tasmin210008[i],dt_gi_tmin.tasmin210008[i],dt_mp_tmin.tasmin210008[i]])
    _, p_tmin9 = stats.ttest_ind([dt_ac_tmin.tasmin0809[i],dt_cn_tmin.tasmin0809[i],dt_gf_tmin.tasmin0809[i],dt_gi_tmin.tasmin0809[i],dt_mp_tmin.tasmin0809[i]],
                               [dt_ac_tmin.tasmin210009[i],dt_cn_tmin.tasmin210009[i],dt_gf_tmin.tasmin210009[i],dt_gi_tmin.tasmin210009[i],dt_mp_tmin.tasmin210009[i]])
    _, p_tmin10 = stats.ttest_ind([dt_ac_tmin.tasmin0810[i],dt_cn_tmin.tasmin0810[i],dt_gf_tmin.tasmin0810[i],dt_gi_tmin.tasmin0810[i],dt_mp_tmin.tasmin0810[i]],
                                [dt_ac_tmin.tasmin210010[i],dt_cn_tmin.tasmin210010[i],dt_gf_tmin.tasmin210010[i],dt_gi_tmin.tasmin210010[i],dt_mp_tmin.tasmin210010[i]])
    _, p_tmin11 = stats.ttest_ind([dt_ac_tmin.tasmin0811[i],dt_cn_tmin.tasmin0811[i],dt_gf_tmin.tasmin0811[i],dt_gi_tmin.tasmin0811[i],dt_mp_tmin.tasmin0811[i]],
                                [dt_ac_tmin.tasmin210011[i],dt_cn_tmin.tasmin210011[i],dt_gf_tmin.tasmin210011[i],dt_gi_tmin.tasmin210011[i],dt_mp_tmin.tasmin210011[i]])
    _, p_tmin12 = stats.ttest_ind([dt_ac_tmin.tasmin0812[i],dt_cn_tmin.tasmin0812[i],dt_gf_tmin.tasmin0812[i],dt_gi_tmin.tasmin0812[i],dt_mp_tmin.tasmin0812[i]],
                                [dt_ac_tmin.tasmin210012[i],dt_cn_tmin.tasmin210012[i],dt_gf_tmin.tasmin210012[i],dt_gi_tmin.tasmin210012[i],dt_mp_tmin.tasmin210012[i]])

    p_tmin_1.append(p_tmin1),p_tmin_2.append(p_tmin2),p_tmin_3.append(p_tmin3),p_tmin_4.append(p_tmin4),p_tmin_5.append(p_tmin5), p_tmin_6.append(p_tmin6)
    p_tmin_7.append(p_tmin7),p_tmin_8.append(p_tmin8),p_tmin_9.append(p_tmin9),p_tmin_10.append(p_tmin10),p_tmin_11.append(p_tmin11),p_tmin_12.append(p_tmin12)

##new database
data_p_mon = pd.DataFrame()
data_p_mon['id'] = dt_cn_tmin.id
data_p_mon['p_tmin01']= p_tmin_1
data_p_mon['p_tmin02'] = p_tmin_2
data_p_mon['p_tmin03']=  p_tmin_3
data_p_mon['p_tmin04']= p_tmin_4
data_p_mon['p_tmin05']= p_tmin_5
data_p_mon['p_tmin06']=  p_tmin_6
data_p_mon['p_tmin07']= p_tmin_7
data_p_mon['p_tmin08']= p_tmin_8
data_p_mon['p_tmin09']= p_tmin_9
data_p_mon['p_tmin10']= p_tmin_10
data_p_mon['p_tmin11']= p_tmin_11
data_p_mon['p_tmin12'] =  p_tmin_12

data_p_mon.to_csv(r'I:\环渤海\未来气象\analysis\二次分析\p_tmin_mon_45.csv',index=None)
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:05:06 2019

@author: ThinkPad
"""

import os
import numpy as np
import pandas as pd
import sklearn 
from sklearn import datasets, linear_model

path = r'I:\环渤海\未来气象\ACCESS1-0_8.5'

pr = []
tasmax = []
tasmin = []
for i in os.listdir(path):
    for j in os.listdir(path+'\\'+i):
        df = pd.read_csv(path +'\\'+ i+ '\\' + j,engine='python')
#        print(path +'\\'+ i+ '\\' + j)
        pr.append(df.pr.sum()*10)
        tasmax.append(df.tasmax.mean())
        tasmin.append(df.tasmin.mean())

ac_85 = pd.DataFrame()
ac_85['pr'] = pr
ac_85['tasmax'] = tasmax
ac_85['tasmin'] = tasmin

#2008和2100年年值，及各月值
path_an08 = r'I:\环渤海\未来气象\ACCESS1-0_8.5\2008'
path_an2100 = r'I:\环渤海\未来气象\ACCESS1-0_8.5\2100'
pr_ann = []
tasmax_ann = []
tasmin_ann = []
pr_an2100 = []
tasmax_an2100 = []
tasmin_an2100 = []

for i in os.listdir(path_an08):
    df_ann = pd.read_csv(path_an08 +'\\'+ i,engine='python')
    pr_ann.append(df_ann.pr.sum()*10)
    tasmax_ann.append(df_ann.tasmax.mean())
    tasmin_ann.append(df_ann.tasmin.mean())
for i in os.listdir(path_an2100):
    df_an2100 = pd.read_csv(path_an2100 +'\\'+ i,engine='python')
    pr_an2100.append(df_an2100.pr.sum()*10)
    tasmax_an2100.append(df_an2100.tasmax.mean())
    tasmin_an2100.append(df_an2100.tasmin.mean())

#2008和2100年年值，及各月值
pr_0801,pr_0802,pr_0803,pr_0804,pr_0805,pr_0806,pr_0807,pr_0808,pr_0809,pr_0810,\
pr_0811,pr_0812 = [],[],[],[],[],[],[],[],[],[],[],[]
tasmax_0801,tasmax_0802,tasmax_0803,tasmax_0804,tasmax_0805,tasmax_0806,\
tasmax_0807,tasmax_0808,tasmax_0809,tasmax_0810,tasmax_0811,tasmax_0812 = [],[],[],[],[],[],[],[],[],[],[],[]
tasmin_0801,tasmin_0802,tasmin_0803,tasmin_0804,tasmin_0805,tasmin_0806,\
tasmin_0807,tasmin_0808,tasmin_0809,tasmin_0810,tasmin_0811,tasmin_0812 = [],[],[],[],[],[],[],[],[],[],[],[]

pr_210001,pr_210002,pr_210003,pr_210004,pr_210005,pr_210006,\
pr_210007,pr_210008,pr_210009,pr_210010,pr_210011,pr_210012 = [],[],[],[],[],[],[],[],[],[],[],[]
tasmax_210001,tasmax_210002,tasmax_210003,tasmax_210004,tasmax_210005,tasmax_210006,\
tasmax_210007,tasmax_210008,tasmax_210009,tasmax_210010,tasmax_210011,tasmax_210012 = [],[],[],[],[],[],[],[],[],[],[],[]
tasmin_210001,tasmin_210002,tasmin_210003,tasmin_210004,tasmin_210005,tasmin_210006,\
tasmin_210007,tasmin_210008,tasmin_210009,tasmin_210010,tasmin_210011,tasmin_210012 = [],[],[],[],[],[],[],[],[],[],[],[]


for i in os.listdir(path_an08):
    df_ann = pd.read_csv(path_an08 +'\\'+ i,engine='python')
    pr_0801.append(df_ann.pr[:31].sum()*10)
    pr_0802.append(df_ann.pr[31:59].sum()*10)
    pr_0803.append(df_ann.pr[59:90].sum()*10)
    pr_0804.append(df_ann.pr[90:120].sum()*10)
    pr_0805.append(df_ann.pr[120:151].sum()*10)
    pr_0806.append(df_ann.pr[151:181].sum()*10)
    pr_0807.append(df_ann.pr[181:212].sum()*10)
    pr_0808.append(df_ann.pr[212:243].sum()*10)
    pr_0809.append(df_ann.pr[243:273].sum()*10)
    pr_0810.append(df_ann.pr[273:304].sum()*10)
    pr_0811.append(df_ann.pr[304:334].sum()*10)
    pr_0812.append(df_ann.pr[334:365].sum()*10)
    tasmax_0801.append(df_ann.tasmax[:31].mean())
    tasmax_0802.append(df_ann.tasmax[31:59].mean())
    tasmax_0803.append(df_ann.tasmax[59:90].mean())
    tasmax_0804.append(df_ann.tasmax[90:120].mean())
    tasmax_0805.append(df_ann.tasmax[120:151].mean())
    tasmax_0806.append(df_ann.tasmax[151:181].mean())
    tasmax_0807.append(df_ann.tasmax[181:212].mean())
    tasmax_0808.append(df_ann.tasmax[212:243].mean())
    tasmax_0809.append(df_ann.tasmax[243:273].mean())
    tasmax_0810.append(df_ann.tasmax[273:304].mean())
    tasmax_0811.append(df_ann.tasmax[304:334].mean())
    tasmax_0812.append(df_ann.tasmax[334:365].mean())
    tasmin_0801.append(df_ann.tasmin[:31].mean())
    tasmin_0802.append(df_ann.tasmin[31:59].mean())
    tasmin_0803.append(df_ann.tasmin[59:90].mean())
    tasmin_0804.append(df_ann.tasmin[90:120].mean())
    tasmin_0805.append(df_ann.tasmin[120:151].mean())
    tasmin_0806.append(df_ann.tasmin[151:181].mean())
    tasmin_0807.append(df_ann.tasmin[181:212].mean())
    tasmin_0808.append(df_ann.tasmin[212:243].mean())
    tasmin_0809.append(df_ann.tasmin[243:273].mean())
    tasmin_0810.append(df_ann.tasmin[273:304].mean())
    tasmin_0811.append(df_ann.tasmin[304:334].mean())
    tasmin_0812.append(df_ann.tasmin[334:365].mean())
for i in os.listdir(path_an2100):
    df_an2100 = pd.read_csv(path_an2100 +'\\'+ i,engine='python')
    pr_210001.append(df_an2100.pr[:31].sum()*10)
    pr_210002.append(df_an2100.pr[31:59].sum()*10)
    pr_210003.append(df_an2100.pr[59:90].sum()*10)
    pr_210004.append(df_an2100.pr[90:120].sum()*10)
    pr_210005.append(df_an2100.pr[120:151].sum()*10)
    pr_210006.append(df_an2100.pr[151:181].sum()*10)
    pr_210007.append(df_an2100.pr[181:212].sum()*10)
    pr_210008.append(df_an2100.pr[212:243].sum()*10)
    pr_210009.append(df_an2100.pr[243:273].sum()*10)
    pr_210010.append(df_an2100.pr[273:304].sum()*10)
    pr_210011.append(df_an2100.pr[304:334].sum()*10)
    pr_210012.append(df_an2100.pr[334:365].sum()*10)
    tasmax_210001.append(df_an2100.tasmax[:31].mean())
    tasmax_210002.append(df_an2100.tasmax[31:59].mean())
    tasmax_210003.append(df_an2100.tasmax[59:90].mean())
    tasmax_210004.append(df_an2100.tasmax[90:120].mean())
    tasmax_210005.append(df_an2100.tasmax[120:151].mean())
    tasmax_210006.append(df_an2100.tasmax[151:181].mean())
    tasmax_210007.append(df_an2100.tasmax[181:212].mean())
    tasmax_210008.append(df_an2100.tasmax[212:243].mean())
    tasmax_210009.append(df_an2100.tasmax[243:273].mean())
    tasmax_210010.append(df_an2100.tasmax[273:304].mean())
    tasmax_210011.append(df_an2100.tasmax[304:334].mean())
    tasmax_210012.append(df_an2100.tasmax[334:365].mean())
    tasmin_210001.append(df_an2100.tasmin[:31].mean())
    tasmin_210002.append(df_an2100.tasmin[31:59].mean())
    tasmin_210003.append(df_an2100.tasmin[59:90].mean())
    tasmin_210004.append(df_an2100.tasmin[90:120].mean())
    tasmin_210005.append(df_an2100.tasmin[120:151].mean())
    tasmin_210006.append(df_an2100.tasmin[151:181].mean())
    tasmin_210007.append(df_an2100.tasmin[181:212].mean())
    tasmin_210008.append(df_an2100.tasmin[212:243].mean())
    tasmin_210009.append(df_an2100.tasmin[243:273].mean())
    tasmin_210010.append(df_an2100.tasmin[273:304].mean())
    tasmin_210011.append(df_an2100.tasmin[304:334].mean())
    tasmin_210012.append(df_an2100.tasmin[334:365].mean())

################################################
    new_data_pr = pd.DataFrame()
new_data_tasmax = pd.DataFrame()
new_data_tasmin = pd.DataFrame()

new_data_pr['id'] = [int(i[:5]) for i in os.listdir(path_an08)]
new_data_tasmax['id'] = [int(i[:5]) for i in os.listdir(path_an08)]
new_data_tasmin['id'] = [int(i[:5]) for i in os.listdir(path_an08)]


new_data_pr['pr0801'] = pr_0801
new_data_pr['pr0802'] = pr_0802
new_data_pr['pr0803'] = pr_0803
new_data_pr['pr0804'] = pr_0804
new_data_pr['pr0805'] = pr_0805
new_data_pr['pr0806'] = pr_0806
new_data_pr['pr0807'] = pr_0807
new_data_pr['pr0808'] = pr_0808
new_data_pr['pr0809'] = pr_0809
new_data_pr['pr0810'] = pr_0810
new_data_pr['pr0811'] = pr_0811
new_data_pr['pr0812'] = pr_0812

new_data_tasmax['tasmax0801'] = tasmax_0801
new_data_tasmax['tasmax0802'] = tasmax_0802
new_data_tasmax['tasmax0803'] = tasmax_0803
new_data_tasmax['tasmax0804'] = tasmax_0804
new_data_tasmax['tasmax0805'] = tasmax_0805
new_data_tasmax['tasmax0806'] = tasmax_0806
new_data_tasmax['tasmax0807'] = tasmax_0807
new_data_tasmax['tasmax0808'] = tasmax_0808
new_data_tasmax['tasmax0809'] = tasmax_0809
new_data_tasmax['tasmax0810'] = tasmax_0810
new_data_tasmax['tasmax0811'] = tasmax_0811
new_data_tasmax['tasmax0812'] = tasmax_0812

new_data_tasmin['tasmin0801'] = tasmin_0801
new_data_tasmin['tasmin0802'] = tasmin_0802
new_data_tasmin['tasmin0803'] = tasmin_0803
new_data_tasmin['tasmin0804'] = tasmin_0804
new_data_tasmin['tasmin0805'] = tasmin_0805
new_data_tasmin['tasmin0806'] = tasmin_0806
new_data_tasmin['tasmin0807'] = tasmin_0807
new_data_tasmin['tasmin0808'] = tasmin_0808
new_data_tasmin['tasmin0809'] = tasmin_0809
new_data_tasmin['tasmin0810'] = tasmin_0810
new_data_tasmin['tasmin0811'] = tasmin_0811
new_data_tasmin['tasmin0812'] = tasmin_0812

new_data_pr['pr210001'] = pr_210001
new_data_pr['pr210002'] = pr_210002
new_data_pr['pr210003'] = pr_210003
new_data_pr['pr210004'] = pr_210004
new_data_pr['pr210005'] = pr_210005
new_data_pr['pr210006'] = pr_210006
new_data_pr['pr210007'] = pr_210007
new_data_pr['pr210008'] = pr_210008
new_data_pr['pr210009'] = pr_210009
new_data_pr['pr210010'] = pr_210010
new_data_pr['pr210011'] = pr_210011
new_data_pr['pr210012'] = pr_210012

new_data_tasmax['tasmax210001'] = tasmax_210001
new_data_tasmax['tasmax210002'] = tasmax_210002
new_data_tasmax['tasmax210003'] = tasmax_210003
new_data_tasmax['tasmax210004'] = tasmax_210004
new_data_tasmax['tasmax210005'] = tasmax_210005
new_data_tasmax['tasmax210006'] = tasmax_210006
new_data_tasmax['tasmax210007'] = tasmax_210007
new_data_tasmax['tasmax210008'] = tasmax_210008
new_data_tasmax['tasmax210009'] = tasmax_210009
new_data_tasmax['tasmax210010'] = tasmax_210010
new_data_tasmax['tasmax210011'] = tasmax_210011
new_data_tasmax['tasmax210012'] = tasmax_210012

new_data_tasmin['tasmin210001'] = tasmin_210001
new_data_tasmin['tasmin210002'] = tasmin_210002
new_data_tasmin['tasmin210003'] = tasmin_210003
new_data_tasmin['tasmin210004'] = tasmin_210004
new_data_tasmin['tasmin210005'] = tasmin_210005
new_data_tasmin['tasmin210006'] = tasmin_210006
new_data_tasmin['tasmin210007'] = tasmin_210007
new_data_tasmin['tasmin210008'] = tasmin_210008
new_data_tasmin['tasmin210009'] = tasmin_210009
new_data_tasmin['tasmin210010'] = tasmin_210010
new_data_tasmin['tasmin210011'] = tasmin_210011
new_data_tasmin['tasmin210012'] = tasmin_210012

new_data_pr.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_pr.csv',index=False,)
new_data_tasmax.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_tmax.csv',index=False,)
new_data_tasmin.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_tmin.csv',index=False,)
###################
new_data_ann = pd.DataFrame()

new_data_ann['id'] = [int(i[:5]) for i in os.listdir(path_an08)]
new_data_ann['pr_08'] = pr_ann
new_data_ann['tmax_08'] = tasmax_ann
new_data_ann['tmin_08'] = tasmin_ann
new_data_ann['pr_2100'] = pr_an2100
new_data_ann['tmax_2100'] = tasmax_an2100
new_data_ann['tmin_2100'] = tasmin_an2100

new_data_ann.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_ann.csv',index=False,)
#################
#整年的斜率
from sklearn import datasets, linear_model
year = [i for i in range(2006,2101,1)]
year = np.array(year).reshape(95,1)# year = 95

def slope_(arr):
    regr = linear_model.LinearRegression()
    regr.fit(year,arr) 
    return regr.coef_
slope_pr = []
slope_tmax = []
slope_tmin = []
for i in range(76):
    slope_pr.append(float(slope_(ac_85.pr[i::76])))
    slope_tmax.append(float(slope_(ac_85.tasmax[i::76])))
    slope_tmin.append(float(slope_(ac_85.tasmin[i::76])))

new_data = pd.DataFrame()

new_data['id'] = [int(i[:5]) for i in os.listdir(path+'\\'+'2009')]
new_data['pr_slp'] = slope_pr
new_data['tmax_slp'] = slope_tmax
new_data['tmin_slp'] = slope_tmin

new_data.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_slope.csv',index=False,)
###################################################################
#分月份斜率
pr_slp1,pr_slp2,pr_slp3,pr_slp4,pr_slp5,pr_slp6,pr_slp7,pr_slp8,pr_slp9,pr_slp10,pr_slp11,pr_slp12 = [],[],[],\
[],[],[],[],[],[],[],[],[]
tasmax_slp1,tasmax_slp2,tasmax_slp3,tasmax_slp4,tasmax_slp5,tasmax_slp6,tasmax_slp7,tasmax_slp8,tasmax_slp9,\
tasmax_slp10,tasmax_slp11,tasmax_slp12 = [],[],[],[],[],[],[],[],[],[],[],[]
tasmin_slp1,tasmin_slp2,tasmin_slp3,tasmin_slp4,tasmin_slp5,tasmin_slp6,tasmin_slp7,tasmin_slp8,tasmin_slp9,\
tasmin_slp10,tasmin_slp11,tasmin_slp12 = [],[],[],[],[],[],[],[],[],[],[],[]

for i in os.listdir(path):
    for j in os.listdir(path+'\\'+i):
        df = pd.read_csv(path +'\\'+ i+ '\\' + j,engine='python')
        
        pr_slp1.append(df.pr[1]*10),pr_slp2.append(df.pr[32]*10),pr_slp3.append(df.pr[62]*10),\
        pr_slp4.append(df.pr[93]*10),pr_slp5.append(df.pr[124]*10),pr_slp6.append(df.pr[155]*10),\
        pr_slp7.append(df.pr[185]*10),pr_slp8.append(df.pr[216]*10),pr_slp9.append(df.pr[247]*10),\
        pr_slp10.append(df.pr[277]*10),pr_slp11.append(df.pr[308]*10),pr_slp12.append(df.pr[363]*10)
        
        tasmax_slp1.append(df.tasmax[1]*10),tasmax_slp2.append(df.tasmax[32]*10),tasmax_slp3.append(df.tasmax[62]*10),\
        tasmax_slp4.append(df.tasmax[93]*10),tasmax_slp5.append(df.tasmax[124]*10),tasmax_slp6.append(df.tasmax[155]*10),\
        tasmax_slp7.append(df.tasmax[185]*10),tasmax_slp8.append(df.tasmax[216]*10),tasmax_slp9.append(df.tasmax[247]*10),\
        tasmax_slp10.append(df.tasmax[277]*10),tasmax_slp11.append(df.tasmax[308]*10),tasmax_slp12.append(df.tasmax[363]*10)
        
        tasmin_slp1.append(df.tasmin[1]),tasmin_slp2.append(df.tasmin[32]),tasmin_slp3.append(df.tasmin[62]),\
        tasmin_slp4.append(df.tasmin[93]),tasmin_slp5.append(df.tasmin[124]),tasmin_slp6.append(df.tasmin[155]),\
        tasmin_slp7.append(df.tasmin[185]),tasmin_slp8.append(df.tasmin[216]),tasmin_slp9.append(df.tasmin[247]),\
        tasmin_slp10.append(df.tasmin[277]),tasmin_slp11.append(df.tasmin[308]),tasmin_slp12.append(df.tasmin[363])

pr_r1,pr_r2,pr_r3,pr_r4,pr_r5,pr_r6,pr_r7,pr_r8,pr_r9,pr_r10,pr_r11,pr_r12 = [],[],[],[],[],[],[],[],[],[],[],[]
tasmax_r1,tasmax_r2,tasmax_r3,tasmax_r4,tasmax_r5,tasmax_r6,tasmax_r7,tasmax_r8,tasmax_r9,tasmax_r10,tasmax_r11,\
tasmax_r12 = [],[],[],[],[],[],[],[],[],[],[],[]
tasmin_r1,tasmin_r2,tasmin_r3,tasmin_r4,tasmin_r5,tasmin_r6,tasmin_r7,tasmin_r8,tasmin_r9,tasmin_r10,tasmin_r11,\
tasmin_r12 = [],[],[],[],[],[],[],[],[],[],[],[]
for i in range(76):
    pr_r1.append(float(slope_(pr_slp1[i::76]))),pr_r2.append(float(slope_(pr_slp2[i::76]))),pr_r3.append(float(slope_(pr_slp3[i::76]))),\
    pr_r4.append(float(slope_(pr_slp4[i::76]))),pr_r5.append(float(slope_(pr_slp5[i::76]))),pr_r6.append(float(slope_(pr_slp6[i::76]))),\
    pr_r7.append(float(slope_(pr_slp7[i::76]))),pr_r8.append(float(slope_(pr_slp8[i::76]))),pr_r9.append(float(slope_(pr_slp9[i::76]))),\
    pr_r10.append(float(slope_(pr_slp10[i::76]))),pr_r11.append(float(slope_(pr_slp11[i::76]))),pr_r12.append(float(slope_(pr_slp12[i::76])))

        
    tasmax_r1.append(float(slope_(tasmax_slp1[i::76]))),tasmax_r2.append(float(slope_(tasmax_slp2[i::76]))),\
    tasmax_r3.append(float(slope_(tasmax_slp3[i::76]))),tasmax_r4.append(float(slope_(tasmax_slp4[i::76]))),\
    tasmax_r5.append(float(slope_(tasmax_slp5[i::76]))),tasmax_r6.append(float(slope_(tasmax_slp6[i::76]))),\
    tasmax_r7.append(float(slope_(tasmax_slp7[i::76]))),tasmax_r8.append(float(slope_(tasmax_slp8[i::76]))),\
    tasmax_r9.append(float(slope_(tasmax_slp9[i::76]))),tasmax_r10.append(float(slope_(tasmax_slp10[i::76]))),\
    tasmax_r11.append(float(slope_(tasmax_slp11[i::76]))),tasmax_r12.append(float(slope_(tasmax_slp12[i::76])))
        
    tasmin_r1.append(float(slope_(tasmin_slp1[i::76]))),tasmin_r2.append(float(slope_(tasmin_slp2[i::76]))),\
    tasmin_r3.append(float(slope_(tasmin_slp3[i::76]))),tasmin_r4.append(float(slope_(tasmin_slp4[i::76]))),\
    tasmin_r5.append(float(slope_(tasmin_slp5[i::76]))),tasmin_r6.append(float(slope_(tasmin_slp6[i::76]))),\
    tasmin_r7.append(float(slope_(tasmin_slp7[i::76]))),tasmin_r8.append(float(slope_(tasmin_slp8[i::76]))),\
    tasmin_r9.append(float(slope_(tasmin_slp9[i::76]))),tasmin_r10.append(float(slope_(tasmin_slp10[i::76]))),\
    tasmin_r11.append(float(slope_(tasmin_slp11[i::76]))),tasmin_r12.append(float(slope_(tasmin_slp12[i::76])))
 
    new_data_pr_r = pd.DataFrame()
new_data_tasmax_r = pd.DataFrame()
new_data_tasmin_r = pd.DataFrame()

new_data_pr_r['id'] = [int(i[:5]) for i in os.listdir(path_an08)]
new_data_tasmax_r['id'] = [int(i[:5]) for i in os.listdir(path_an08)]
new_data_tasmin_r['id'] = [int(i[:5]) for i in os.listdir(path_an08)]

new_data_pr_r['r1'],new_data_pr_r['r2'],new_data_pr_r['r3'],new_data_pr_r['r4'],\
new_data_pr_r['r5'],new_data_pr_r['r6'],new_data_pr_r['r7'],new_data_pr_r['r8'],\
new_data_pr_r['r9'],new_data_pr_r['r10'],new_data_pr_r['r11'],new_data_pr_r['r12'] = pr_r1,\
pr_r2,pr_r3,pr_r4,pr_r5,pr_r6,pr_r7,pr_r8,pr_r9,pr_r10,pr_r11,pr_r12

new_data_tasmax_r['r1'],new_data_tasmax_r['r2'],new_data_tasmax_r['r3'],new_data_tasmax_r['r4'],\
new_data_tasmax_r['r5'],new_data_tasmax_r['r6'],new_data_tasmax_r['r7'],new_data_tasmax_r['r8'],\
new_data_tasmax_r['r9'],new_data_tasmax_r['r10'],new_data_tasmax_r['r11'],new_data_tasmax_r['r12'] = tasmax_r1,\
tasmax_r2,tasmax_r3,tasmax_r4,tasmax_r5,tasmax_r6,tasmax_r7,tasmax_r8,tasmax_r9,tasmax_r10,tasmax_r11,tasmax_r12


new_data_tasmin_r['r1'],new_data_tasmin_r['r2'],new_data_tasmin_r['r3'],new_data_tasmin_r['r4'],\
new_data_tasmin_r['r5'],new_data_tasmin_r['r6'],new_data_tasmin_r['r7'],new_data_tasmin_r['r8'],\
new_data_tasmin_r['r9'],new_data_tasmin_r['r10'],new_data_tasmin_r['r11'],new_data_tasmin_r['r12'] = tasmin_r1,\
tasmin_r2,tasmin_r3,tasmin_r4,tasmin_r5,tasmin_r6,tasmin_r7,tasmin_r8,tasmin_r9,tasmin_r10,tasmin_r11,tasmin_r12

new_data_pr_r.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_pr_r.csv',index=False,)
new_data_tasmax_r.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_tmax_r.csv',index=False,)
new_data_tasmin_r.to_csv(r'I:\环渤海\未来气象\analysis\ac_85_tmin_r.csv',index=False,)
#############################################################################################

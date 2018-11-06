import os
import numba as nb
import numpy as np
from osgeo import gdal
from osgeo import gdal
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def writeTiff(im_data,im_width,im_height,im_bands,im_geotrans,im_proj,path):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32

    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    elif len(im_data.shape) == 2:
        im_data = np.array([im_data])
    else:
        im_bands, (im_height, im_width) = 1,im_data.shape
        #创建文件
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(path, im_width, im_height, im_bands, datatype)
    if(dataset!= None):
        dataset.SetGeoTransform(im_geotrans) #写入仿射变换参数
        dataset.SetProjection(im_proj) #写入投影
    for i in range(im_bands):
        dataset.GetRasterBand(i+1).WriteArray(im_data[i])
    del dataset
path_cli = r'G:\china_geodata\china_pre_tem\yn\tem'
out_path = r'G:\china_geodata\yunnan_region\chang'
#print(os.walk(path))
ds = gdal.Open(path_cli+'\\'+'tem19801.tif')
tr = ds.GetGeoTransform()
prj = ds.GetProjection()
x = ds.RasterXSize
y = ds.RasterYSize
im_bands = ds.RasterCount #波段数
year = [i for i in range(1980,2013,1)]
d1= ds.ReadAsArray(0, 0, x, y).reshape(-1, 1)
arr = []
for i in range(33):
    d2 = gdal.Open(path_cli+'//'+'tem%d.tif'%(19801+i*10)).ReadAsArray(0, 0, x, y).reshape(-1, 1)
    arr.append(d2)
slope = []#2000-2010 ndvi
year = np.array(year).reshape(33,1)
arr=np.array(arr)/10

@nb.jit()
def slope_(arr):
    for i in range(969*947):
        # Create linear regression object
        regr = linear_model.LinearRegression()

    # Train the model using the training sets
        regr.fit(year,arr[:,i])
        
        slope.append(regr.coef_)
    return slope
writeTiff(slope1, x, y,im_bands, tr, prj, yr_path)

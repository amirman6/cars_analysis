# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:32:26 2022

@author: T430s
"""
import streamlit as st
import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt
import seaborn as sns


# opening the file
import pickle
with open('cars', 'rb') as f: # wb = write binary file
    cars = pickle.load(f)


cars['mpg'] = (cars['city-mpg']+cars['highway-mpg'])/2
cars['horsepower'] = cars['horsepower'].astype(int)


st.sidebar.header('specify the parameters for histogram')
hist = st.sidebar.selectbox('select',('wheel-base','length','width','height','curb-weight','engine-size','compression-ratio','horsepower',
                                         'mpg','price'))

if st.sidebar.button('Histogram/BoxPlot'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    plt.hist(cars[hist],edgecolor='k',bins = 30)
    plt.title(hist)
    st.pyplot()
    
    plt.boxplot(cars[hist])
    plt.title(hist)
    plt.show()
    st.pyplot()
    st.write(cars.describe()[hist])


st.sidebar.header('specify the parameters for correlation')
corr = st.sidebar.selectbox('select',('all','wheel-base','length','width','height','curb-weight','engine-size','compression-ratio','horsepower',
                                         'mpg','price'))
if st.sidebar.button('correlation'):
    if corr == 'all':
        st.write(cars.corr())
        cars_num=cars.select_dtypes(include=['float64','int64','int32'])
        all_corr = cars_num.corr()
        sns.heatmap(all_corr[(all_corr >= 0.5) | (all_corr <= -0.4)], cmap='viridis',vmax=1.0,
                       vmin= -1.0, linewidth = 0.1,annot = True,
                       annot_kws={'size':8})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    else:
        cars.corr()[corr]    
        

st.sidebar.header('Vehicle details(average) by Make/Company')
make_list = cars.make.unique().tolist()
make_list.insert(0,'all')
make = st.sidebar.selectbox('select',make_list)    
# cars details average by make
if st.sidebar.button('Vehicle Details'):
    if make == 'all':
        st.write(cars.describe())
    else:
        details = cars.groupby('make').mean()
        details.loc[make] 
    


st.sidebar.header('Vehicles MPG and Price Comparison Plot')
if st.sidebar.button('Vehicle mpg Compare'):
    mpg = cars.groupby('make')['mpg'].mean()
    mpg.plot(kind='bar')
    plt.title('miles per gallon(mpg) by make')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.show()
    st.pyplot()
    
if st.sidebar.button('Vehicle Price Compare'):
    mpg = cars.groupby('make')['price'].mean()
    mpg.plot(kind='bar')
    plt.title('Price($ thousands) by make')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.show()
    st.pyplot()    
           


# pair plots
cars_num=cars.select_dtypes(include=['float64','int64','int32'])
st.sidebar.header('Select for PairPlot')
pair = st.sidebar.selectbox('select',('mpg','wheel-base','length','width','height','curb-weight','engine-size','horsepower','price'))

# plotting pairplot correlation
if st.sidebar.button('PairPlot'):
    
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    #cars_num=cars.select_dtypes(include=['float64','int64','int32'])
    sns.pairplot(cars,x_vars = ['mpg','wheel-base','length','width','height','curb-weight','engine-size','horsepower','price'],
             y_vars=[pair], kind='reg', plot_kws={'line_kws':{'color':'red'}})
    
    #fig = plt.figure(figsize=(12,8)) 
    st.pyplot()
    
    

    
    




    


#!/usr/bin/env python
# coding: utf-8

# # Project measuring waterflows

# ## Instaling MannKendall test in conda framework

# In[1]:


#conda install pyMannKendall
#conda install -c conda-forge pymannkendall
# https://pypi.org/project/pymannkendall/
# Explanation: https://www.geeksforgeeks.org/how-to-perform-a-mann-kendall-trend-test-in-python/


# ## Project waterflows

# ### Importing packages

# In[1]:


import numpy as np
import pandas as pd
import pymannkendall as mk
import scipy as sp


# ### Load and check data

# In[2]:


df=pd.read_excel('InputData.xlsx', sheet_name='pod')
df.head()


# In[3]:


df.info()


# ### Implementing MannKandall test and evaulating values for Theil-Sen trend estimator

# In[4]:


from scipy.special import logsumexp
#Empty lists
df_list1 = []
df_nOBS = []

listSredGodP1 = []
listSredGodT1 = []
listSredGodS1 = []
listSredGodI1 = []
listSredGodK = []
listSredGodLam = []
listSredGodLocation = []


listMinSrMesP1 = []
listMinSrMesT1 = []
listMinSrMesS1 = []
listMinSrMesI1 = []
listMinSrMesK = []
listMinSrMesLam = []
listMinSrMesLocation = []


#appling MannKendal test on subsets and creating columns with results
for i in range(1,max(df['station'])+1):
    try:
        if mk.original_test(df[df['station']==i]['SredGod'])[0]=='no trend' and mk.original_test(df[df['station']==i]['MinSrMes'])[0]=='no trend':
        
            dg=str(i)
            df_list1.append(dg)
            dfNOBS = len(df[df['station']==i])
            df_nOBS.append(dfNOBS)
        
            p=mk.original_test(df[df['station']==i]['SredGod'])[2]
            listSredGodP1.append(p)  
            pS=mk.original_test(df[df['station']==i]['SredGod'])[7]
            listSredGodS1.append(pS)  
            pI=mk.original_test(df[df['station']==i]['SredGod'])[8]
            listSredGodI1.append(pI)
            pT=mk.original_test(df[df['station']==i]['SredGod'])[0]
            listSredGodT1.append(pT)
            lstSredGodK=1/3-1/(0.31+0.91*df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listSredGodK.append(lstSredGodK)          
            lstSredGodLam=(df[df['station']==i]['SredGod'].std(axis = 0, skipna = True)*abs(lstSredGodK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstSredGodK, out=None)))-(np.exp(sp.special.loggamma(1-lstSredGodK, out=None))**2)))
            listSredGodLam.append(lstSredGodLam)
            lstSredGodLocation=df[df['station']==i]['SredGod'].mean(axis = 0, skipna = True)-(lstSredGodLam*(np.exp(sp.special.loggamma(1-lstSredGodK, out=None))-1)/lstSredGodK)
            listSredGodLocation.append(lstSredGodLocation)
          
        
            qP=mk.original_test(df[df['station']==i]['MinSrMes'])[2]
            listMinSrMesP1.append(qP)
            qS=mk.original_test(df[df['station']==i]['MinSrMes'])[7]
            listMinSrMesS1.append(qS)
            qI=mk.original_test(df[df['station']==i]['MinSrMes'])[8]
            listMinSrMesI1.append(qI)
            qT=mk.original_test(df[df['station']==i]['MinSrMes'])[0]
            listMinSrMesT1.append(qT)
            lstMinSrMesK=1/3-1/(0.31+0.91*df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listMinSrMesK.append(lstMinSrMesK)
            lstMinSrMesLam=(df[df['station']==i]['MinSrMes'].std(axis = 0, skipna = True)*abs(lstMinSrMesK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstMinSrMesK, out=None)))-(np.exp(sp.special.loggamma(1-lstMinSrMesK, out=None))**2)))
            listMinSrMesLam.append(lstMinSrMesLam)
            lstMinSrMesLocation=df[df['station']==i]['MinSrMes'].mean(axis = 0, skipna = True)-(lstMinSrMesLam*(np.exp(sp.special.loggamma(1-lstMinSrMesK, out=None))-1)/lstMinSrMesK)
            listMinSrMesLocation.append(lstMinSrMesLocation)
           
        
        elif mk.original_test(df[df['station']==i]['SredGod'])[0]=='no trend' and (mk.original_test(df[df['station']==i]['MinSrMes'])[0]=='decreasing' or mk.original_test(df[df['station']==i]['MinSrMes'])[0]=='increasing'):   
            dg=str(i)
            df_list1.append(dg)
            dfNOBS = len(df[df['station']==i])
            df_nOBS.append(dfNOBS)
        
            p=mk.original_test(df[df['station']==i]['SredGod'])[2]
            listSredGodP1.append(p)  
            pS=mk.original_test(df[df['station']==i]['SredGod'])[7]
            listSredGodS1.append(pS)  
            pI=mk.original_test(df[df['station']==i]['SredGod'])[8]
            listSredGodI1.append(pI)
            pT=mk.original_test(df[df['station']==i]['SredGod'])[0]
            listSredGodT1.append(pT)
            lstSredGodK=1/3-1/(0.31+0.91*df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listSredGodK.append(lstSredGodK)          
            lstSredGodLam=(df[df['station']==i]['SredGod'].std(axis = 0, skipna = True)*abs(lstSredGodK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstSredGodK, out=None)))-(np.exp(sp.special.loggamma(1-lstSredGodK, out=None))**2)))
            listSredGodLam.append(lstSredGodLam)
            lstSredGodLocation=df[df['station']==i]['SredGod'].mean(axis = 0, skipna = True)-(lstSredGodLam*(np.exp(sp.special.loggamma(1-lstSredGodK, out=None))-1)/lstSredGodK)
            listSredGodLocation.append(lstSredGodLocation)
           
        
            qP=mk.original_test(df[df['station']==i]['MinSrMes'])[2]
            listMinSrMesP1.append(qP)
            qS=mk.original_test(df[df['station']==i]['MinSrMes'])[7]
            listMinSrMesS1.append(qS)
            qI=mk.original_test(df[df['station']==i]['MinSrMes'])[8]
            listMinSrMesI1.append(qI)
            qT=mk.original_test(df[df['station']==i]['MinSrMes'])[0]
            listMinSrMesT1.append(qT)
            lstMinSrMesK=1/3-1/(0.31+0.91*df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listMinSrMesK.append(lstMinSrMesK)
            lstMinSrMesLam=(df[df['station']==i]['MinSrMes'].std(axis = 0, skipna = True)*abs(lstMinSrMesK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstMinSrMesK, out=None)))-(np.exp(sp.special.loggamma(1-lstMinSrMesK, out=None))**2)))
            listMinSrMesLam.append(lstMinSrMesLam) 
            lstMinSrMesLocation=(qI+qS*(len(df[df['station']==i])-1))
            listMinSrMesLocation.append(lstMinSrMesLocation)
          
    
        elif (mk.original_test(df[df['station']==i]['SredGod'])[0]=='increasing' or mk.original_test(df[df['station']==i]['SredGod'])[0]=='decreasing') and mk.original_test(df[df['station']==i]['MinSrMes'])[0]=='no trend':
  
            dg=str(i)
            df_list1.append(dg)
            dfNOBS = len(df[df['station']==i])
            df_nOBS.append(dfNOBS)
        
            p=mk.original_test(df[df['station']==i]['SredGod'])[2]
            listSredGodP1.append(p)  
            pS=mk.original_test(df[df['station']==i]['SredGod'])[7]
            listSredGodS1.append(pS)  
            pI=mk.original_test(df[df['station']==i]['SredGod'])[8]
            listSredGodI1.append(pI)
            pT=mk.original_test(df[df['station']==i]['SredGod'])[0]
            listSredGodT1.append(pT)
            lstSredGodK=1/3-1/(0.31+0.91*df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listSredGodK.append(lstSredGodK)          
            lstSredGodLam=(df[df['station']==i]['SredGod'].std(axis = 0, skipna = True)*abs(lstSredGodK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstSredGodK, out=None)))-(np.exp(sp.special.loggamma(1-lstSredGodK, out=None))**2)))
            listSredGodLam.append(lstSredGodLam)
            lstSredGodLocation=(pI+pS*(len(df[df['station']==i])-1))
            listSredGodLocation.append(lstSredGodLocation)

        
            qP=mk.original_test(df[df['station']==i]['MinSrMes'])[2]
            listMinSrMesP1.append(qP)
            qS=mk.original_test(df[df['station']==i]['MinSrMes'])[7]
            listMinSrMesS1.append(qS)
            qI=mk.original_test(df[df['station']==i]['MinSrMes'])[8]
            listMinSrMesI1.append(qI)
            qT=mk.original_test(df[df['station']==i]['MinSrMes'])[0]
            listMinSrMesT1.append(qT)
            lstMinSrMesK=1/3-1/(0.31+0.91*df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listMinSrMesK.append(lstMinSrMesK)
            lstMinSrMesLam=(df[df['station']==i]['MinSrMes'].std(axis = 0, skipna = True)*abs(lstMinSrMesK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstMinSrMesK, out=None)))-(np.exp(sp.special.loggamma(1-lstMinSrMesK, out=None))**2)))
            listMinSrMesLam.append(lstMinSrMesLam)
            lstMinSrMesLocation=df[df['station']==i]['MinSrMes'].mean(axis = 0, skipna = True)-(lstMinSrMesLam*(np.exp(sp.special.loggamma(1-lstMinSrMesK, out=None))-1)/lstMinSrMesK)
            listMinSrMesLocation.append(lstMinSrMesLocation)

        else:
            dg=str(i)
            df_list1.append(dg)
            dfNOBS = len(df[df['station']==i])
            df_nOBS.append(dfNOBS)
        
            p=mk.original_test(df[df['station']==i]['SredGod'])[2]
            listSredGodP1.append(p)  
            pS=mk.original_test(df[df['station']==i]['SredGod'])[7]
            listSredGodS1.append(pS)  
            pI=mk.original_test(df[df['station']==i]['SredGod'])[8]
            listSredGodI1.append(pI)
            pT=mk.original_test(df[df['station']==i]['SredGod'])[0]
            listSredGodT1.append(pT)
            lstSredGodK=1/3-1/(0.31+0.91*df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['SredGod'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listSredGodK.append(lstSredGodK)          
            lstSredGodLam=(df[df['station']==i]['SredGod'].std(axis = 0, skipna = True)*abs(lstSredGodK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstSredGodK, out=None)))-(np.exp(sp.special.loggamma(1-lstSredGodK, out=None))**2)))
            listSredGodLam.append(lstSredGodLam)
            lstSredGodLocation=(pI+pS*(len(df[df['station']==i])-1))
            listSredGodLocation.append(lstSredGodLocation)
 
        
            qP=mk.original_test(df[df['station']==i]['MinSrMes'])[2]
            listMinSrMesP1.append(qP)
            qS=mk.original_test(df[df['station']==i]['MinSrMes'])[7]
            listMinSrMesS1.append(qS)
            qI=mk.original_test(df[df['station']==i]['MinSrMes'])[8]
            listMinSrMesI1.append(qI)
            qT=mk.original_test(df[df['station']==i]['MinSrMes'])[0]
            listMinSrMesT1.append(qT)
            lstMinSrMesK=1/3-1/(0.31+0.91*df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)+np.sqrt((df[df['station']==i]['MinSrMes'].skew(axis = 0, skipna = True)*0.91)**2+1.8))
            listMinSrMesK.append(lstMinSrMesK)
            lstMinSrMesLam=(df[df['station']==i]['MinSrMes'].std(axis = 0, skipna = True)*abs(lstMinSrMesK))/(np.sqrt((np.exp(sp.special.loggamma(1-2*lstMinSrMesK, out=None)))-(np.exp(sp.special.loggamma(1-lstMinSrMesK, out=None))**2)))
            listMinSrMesLam.append(lstMinSrMesLam) 
            lstMinSrMesLocation=(qI+qS*(len(df[df['station']==i])-1))
            listMinSrMesLocation.append(lstMinSrMesLocation)

    except:
        pass
    
#Rename columns
s1 = pd.DataFrame(df_list1,columns=['Index'])
s1['Index'] = pd.to_numeric(s1['Index'])
s2 = pd.DataFrame(df_nOBS,columns=['NumberOfYears'])

k1 = pd.DataFrame(listSredGodP1,columns=['pValueSredGod'])
k2 = pd.DataFrame(listSredGodS1,columns=['SlopeSredGod'])
k3 = pd.DataFrame(listSredGodI1,columns=['InterceptSredGod'])
k5 = pd.DataFrame(listSredGodK,columns=['ShapeParamSredGod'])
k6 = pd.DataFrame(listSredGodLam,columns=['ScaleParamSredGod'])
k7 = pd.DataFrame(listSredGodLocation,columns=['LocationParamSredGod'])
k4 = pd.DataFrame(listSredGodT1,columns=['TrendSredGod'])

l1 = pd.DataFrame(listMinSrMesP1,columns=['pValueMinSrMes'])
l2 = pd.DataFrame(listMinSrMesS1,columns=['SlopeMinSrMes'])
l3 = pd.DataFrame(listMinSrMesI1,columns=['InterceptMinSrMes'])
l5 = pd.DataFrame(listMinSrMesK,columns=['ShapeParamMinSrMes'])
l6 = pd.DataFrame(listMinSrMesLam,columns=['ScaleParamMinSrMes'])
l7 = pd.DataFrame(listMinSrMesLocation,columns=['LocationParamMinSrMes'])
l4 = pd.DataFrame(listMinSrMesT1,columns=['TrendMinSrMes'])


# ### Marging columns into one dataframe with results

# In[5]:


s1['NumberOfYears']=s2['NumberOfYears']
s1['pValueSredGod']=k1['pValueSredGod']
s1['SlopeSredGod']=k2['SlopeSredGod']
s1['InterceptSredGod']=k3['InterceptSredGod']
s1['ShapeParamSredGod']=k5['ShapeParamSredGod']
s1['ScaleParamSredGod']=k6['ScaleParamSredGod']
s1['LocationParamSredGod']=k7['LocationParamSredGod']
s1['TrendSredGod']=k4['TrendSredGod']

s1['pValueMinSrMes']=l1['pValueMinSrMes']
s1['SlopeMinSrMes']=l2['SlopeMinSrMes']
s1['InterceptMinSrMes']=l3['InterceptMinSrMes']
s1['ShapeParamMinSrMes']=l5['ShapeParamMinSrMes']
s1['ScaleParamMinSrMes']=l6['ScaleParamMinSrMes']
s1['LocationParamMinSrMes']=l7['LocationParamMinSrMes']
s1['TrendMinSrMes']=l4['TrendMinSrMes']
s1


# ### Hihhlight cells with yellow which satisfied conditions, where is trend increasing or decreasing

# In[6]:


s1.style.applymap(lambda x: 'background-color : yellow' if x == 'decreasing' or x == 'increasing' else '')


# ### Load new data frame with River station names and coordinates

# In[8]:


kord=pd.read_excel('coordinates.xlsx', sheet_name='kord')
kord.head(5)


# In[9]:


s1.info()


# In[10]:


kord.info()


# ### Merging two data frames, results and names from river stations 

# In[11]:


newdf = s1.merge(kord, how='inner',on='Index')
newdf


# In[12]:


newdf.info()


# ### Replacing NA values with zero

# In[13]:


cols = ['Drainage Area (km2)', 'X coordinate', 'Y coordinate']
newdf[cols] = newdf[cols].fillna(0).applymap(np.int64)


# ### Hihhlight cells with yellow which satisfied conditions, where is trend increasing or decreasing

# In[14]:


newdf.style.applymap(lambda x: 'background-color : yellow' if x == 'decreasing' or x == 'increasing' else '')


# ### Saving merged dataframe results with cordinates to Excel file without index

# In[15]:


newdf.to_excel("WaterFlowEstimationResultsWithCooordinates.xls", index=False)


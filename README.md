<div align="center">
 <h3>
	<img src="https://miro.medium.com/max/720/1*CDj-lEsfn9HAbpMSNmziLQ.gif"      width="300" 
     height="200"/>
</h3>
</div>


<h3 align="center">Milos Todorov PhD, University professor and data scientist</h3>

- 🔭 I’m currently working on **faculty**

- 🌱 I’m currently learning **ML algortihms**

- 📫 How to reach me **milos.todorov82@gmail.com**


<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://www.linkedin.com/in/milos-todorov-phd-2bb4a6201/" target="blank"><img align="center" img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/milos-todorov-phd-2bb4a6201/" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

# PyProgramForMinimalAndAnnualTrendFlowEstimation
This Python program is used for predictive analytics estimation of the river flows in Serbia. This code applies Mann - Kendall test which works for all distributions to analyze time series data for trends. If there is no trend, then probability value p is greater than 0.05, otherwise, there is a trend in time series with significant level (p-value) less or equal than 0.05 and trend could be positive or negative. 

With respect to Mann-Kendall test, the Theil-Sen estimator is used to calculate trend intercept and slope. For this purpose is used `pyMannkendal` package.

## Case study
This datataset contains measurements from 3 hydrological stations of the Republic Hydrometeorological Service of Serbia. It is sample from hydrological site where data collection is carried out. There are two identical files with different extension, which contains program script, conda file - `WaterFlowEstimation.ipynb` and python file - `WaterFlowEstimation.py`. There is also a mathlab file - `TrendFlow.m`, which represent low-flow time series for a subset of hydrological stations showing statistically significant patterns.


## Input datasets

There are two Excel files with input data. The first one is `InputData.xlsx` and it contains measurements from 3 hydrological stations. The second one is `coordinates.xlsx` and it displays basic information about hidrological stations.

`InputData.xlsx` table contains the following variables:

- **Year**:  year when the data were collected
- **MinSrMes**: minimal monthly flow measurements
- **SredGod**: Annual flow measurements
- **station**: Number(index) of the hidrological stations.

`coordinates.xlsx` table contains the following variables:

- **Index**: Index number
- **River No.**: River number in registry
- **River basin**: Name of the river basin
- **River**: Name of the river 
- **Hydrological station**: Name of the Hydrological station
- **Drainage Area (km2)**: Drainage Area (km2)
- **X coordinate**: X coordinate of the measuring station
- **Y coordinate**: Y coordinate of the measuring station

## Table with results

Program generates `WaterFlowEstimationResultsWithCooordinates.xls` file, i.e.table, which contains the following variables:

- **Index**: Index number
- **NumberOfYears**: Number of observation(years)
- **pValueSredGod/pValueMinSrMes**: p-value of the significance test
- **SlopeSredGod/SlopeMinSrMes**: Theil-Sen estimator for slope
- **InterceptSredGod/InterceptMinSrMes**: Theil-Sen estimator for intercept 
- **TrendSredGod/TrendMinSrMes**: Tells about trend (increasing, decreasing or no trend)
- **ShapeParamSredGod/ShapeParamMinSrMes**: Calculation of the shape parameter
- **ScaleParamSredGod/ScaleParamMinSrMes**: Calculation of the scale parameter
- **LocationParamSredGod/LocationParamMinSrMes**: Calculation of the location parameter
- **River No.**: River number in registry
- **River basin**: Name of the river basin
- **River**: Name of the river 
- **Hydrological station**: Name of the Hydrological station
- **Drainage Area (km2)**: Drainage Area (km2)
- **X coordinate**: X coordinate of the measuring station
- **Y coordinate**: Y coordinate of the measuring station


**Part of code which give output coefficients**
```python

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

```

## Dependencies

For running program the following packages are required:
- [numpy](https://www.numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [pyMannKendall](https://github.com/mmhs013/pyMannKendall)
- [scipy](https://scipy.org/)

## Mathlab program - TrendFlow.m

The low-flow time series for a subset of hydrological stations exhibiting statistically significant trends are represented by the Mathlab file `TrendFlow.m`.

## Workmates

On this project I have worked with:
- [Milan Stojkovic, PhD](https://www.linkedin.com/in/milan-stojkovi%C4%87-0b8738b0/)
- [Ivana Krtolica, PhD](https://www.linkedin.com/in/ivana-krtolica-96437a24b/)
- Stevan Prohaska, PhD

## References

1. Hussain et al., (2019). pyMannKendall: a python package for non parametric Mann Kendall family of trend tests.. Journal of Open Source Software, 4(39), 1556, https://doi.org/10.21105/joss.01556

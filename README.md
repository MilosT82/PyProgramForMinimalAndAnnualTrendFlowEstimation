# PyProgramForMinimalAndAnnualTrendFlowEstimation
This Python program for minimal and annual trend flow estimation in Serbia

<div align="center">
 <h3>
	<img src="https://miro.medium.com/max/720/1*CDj-lEsfn9HAbpMSNmziLQ.gif"      width="300" 
     height="200"/>
</h3>
</div>


<h3 align="center">University professor and data scientist</h3>

- 🔭 I’m currently working on **faculty**

- 🌱 I’m currently learning **ML algortihms**

- 📫 How to reach me **milos.todorov82@gmail.com**


<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/https://www.linkedin.com/in/milos-todorov-phd-2bb4a6201/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/milos-todorov-phd-2bb4a6201/" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>



# pyMannKendall
[![Build Status](https://travis-ci.com/mmhs013/pyMannKendall.svg?branch=master)](https://travis-ci.com/mmhs013/pyMannKendall)
[![PyPI](https://img.shields.io/pypi/v/pymannkendall.svg)](https://pypi.org/project/pymannkendall/)
[![PyPI - License](https://img.shields.io/pypi/l/pymannkendall.svg)](https://pypi.org/project/pymannkendall/)
[![PyPI - Status](https://img.shields.io/pypi/status/pymannkendall.svg)](https://pypi.org/project/pymannkendall/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pymannkendall.svg)](https://pypi.org/project/pymannkendall/)

[![Downloads](https://pepy.tech/badge/pymannkendall)](https://pepy.tech/project/pymannkendall)
[![Conda](https://img.shields.io/conda/dn/conda-forge/pymannkendall?label=conda-downloads)](https://anaconda.org/conda-forge/pymannkendall)

[![Google Scholar](https://github.com/mmhs013/Citation_Parser/blob/main/images/gs_pymk_cite.svg?raw=true)](https://scholar.google.com/scholar?q=pyMannKendall%3A+a+python+package+for+non+parametric+Mann+Kendall+family+of+trend+tests.)
[![Researchgate](https://github.com/mmhs013/Citation_Parser/blob/main/images/rg_pymk_cite.svg?raw=true)](https://www.researchgate.net/publication/334688255_pyMannKendall_a_python_package_for_non_parametric_Mann_Kendall_family_of_trend_tests)

[![status](http://joss.theoj.org/papers/14903dbd55343be89105112e585d262a/status.svg)](http://joss.theoj.org/papers/14903dbd55343be89105112e585d262a)
[![DOI](https://zenodo.org/badge/174495388.svg)](https://zenodo.org/badge/latestdoi/174495388)

## What is the Mann-Kendall Test ?
The Mann-Kendall Trend Test (sometimes called the MK test) is used to analyze time series data for consistently increasing or decreasing trends (monotonic trends). It is a non-parametric test, which means it works for all distributions (i.e. data doesn't have to meet the assumption of normality), but data should have no serial correlation. If the data has a serial correlation, it could affect in significant level (p-value). It could lead to misinterpretation. To overcome this problem, researchers proposed several modified Mann-Kendall tests (Hamed and Rao Modified MK Test, Yue and Wang Modified MK Test, Modified MK test using Pre-Whitening method, etc.). Seasonal Mann-Kendall test also developed to remove the effect of seasonality.

Mann-Kendall Test is a powerful trend test, so several others modified Mann-Kendall tests like Multivariate MK Test, Regional MK Test, Correlated MK test, Partial MK Test, etc. were developed for the spacial condition. `pyMannkendal` is a pure Python implementation of non-parametric Mann-Kendall trend analysis, which bring together almost all types of Mann-Kendall Test. Currently, this package has 11 Mann-Kendall Tests and 2 sen's slope estimator function. Brief description of functions are below:

1.	**Original Mann-Kendall test (*original_test*):** Original Mann-Kendall test is a nonparametric test, which does not consider serial correlation or seasonal effects.

2.	**Hamed and Rao Modified MK Test (*hamed_rao_modification_test*):** This modified MK test proposed by *Hamed and Rao (1998)* to address serial autocorrelation issues. They suggested a variance correction approach to improve trend analysis. User can consider first n significant lag by insert lag number in this function. By default, it considered all significant lags.

3.	**Yue and Wang Modified MK Test (*yue_wang_modification_test*):** This is also a variance correction method for considered serial autocorrelation proposed by *Yue, S., & Wang, C. Y. (2004)*. User can also set their desired significant n lags for the calculation.

4.	**Modified MK test using Pre-Whitening method (*pre_whitening_modification_test*):** This test suggested by *Yue and Wang (2002)* to using Pre-Whitening the time series before the application of trend test.

5.	**Modified MK test using Trend free Pre-Whitening method (*trend_free_pre_whitening_modification_test*):** This test also proposed by *Yue and Wang (2002)* to remove trend component and then Pre-Whitening the time series before application of trend test.

6.	**Multivariate MK Test (*multivariate_test*):** This is an MK test for multiple parameters proposed by *Hirsch (1982)*. He used this method for seasonal mk test, where he considered every month as a parameter.

7.	**Seasonal MK Test (*seasonal_test*):** For seasonal time series data, *Hirsch, R.M., Slack, J.R. and Smith, R.A. (1982)* proposed this test to calculate the seasonal trend.

8.	**Regional MK Test (*regional_test*):** Based on*Hirsch (1982)* proposed seasonal mk test, *Helsel, D.R. and Frans, L.M., (2006)* suggest regional mk test to calculate the overall trend in a regional scale.

9.	**Correlated Multivariate MK Test (*correlated_multivariate_test*):** This multivariate mk test proposed by *Hipel (1994)* where the parameters are correlated.

10.	**Correlated Seasonal MK Test (*correlated_seasonal_test*):** This method proposed by *Hipel (1994)* used, when time series significantly correlated with the preceding one or more months/seasons.

11.	**Partial MK Test (*partial_test*):** In a real event, many factors are affecting the main studied response parameter, which can bias the trend results. To overcome this problem, *Libiseller (2002)* proposed this partial mk test. It required two parameters as input, where, one is response parameter and other is an independent parameter.

12.	**Theil-Sen's Slope Estimator (*sens_slope*):** This method proposed by *Theil (1950)* and *Sen (1968)* to estimate the magnitude of the monotonic trend. Intercept is calculate using *Conover, W.J. (1980)* method.

13.	**Seasonal Theil-Sen's Slope Estimator (*seasonal_sens_slope*):** This method proposed by *Hipel (1994)* to estimate the magnitude of the monotonic trend, when data has seasonal effects. Intercept is calculate using *Conover, W.J. (1980)* method.

## Function details:

All Mann-Kendall test functions have almost similar input parameters. Those are:

- **x**:   a vector (list, numpy array or pandas series) data
- **alpha**: significance level (0.05 is the default)
- **lag**: No. of First Significant Lags (Only available in hamed_rao_modification_test and yue_wang_modification_test)
- **period**: seasonal cycle. For monthly data it is 12, weekly data it is 52 (Only available in seasonal tests)

And all Mann-Kendall tests return a named tuple which contained:

- **trend**: tells the trend (increasing, decreasing or no trend)
- **h**: True (if trend is present) or False (if the trend is absence)
- **p**: p-value of the significance test
- **z**: normalized test statistics
- **Tau**: Kendall Tau
- **s**: Mann-Kendal's score
- **var_s**: Variance S
- **slope**: Theil-Sen estimator/slope
- **intercept**: intercept of Kendall-Theil Robust Line, for seasonal test, full period cycle consider as unit time step

sen's slope function required data vector. seasonal sen's slope also has optional input period, which by the default value is 12. Both sen's slope function return only slope value.

## Dependencies

For running program the following packages are required:
- [numpy](https://www.numpy.org/)
- [scipy](https://www.scipy.org/)
- [pyMannKendall](https://github.com/mmhs013/pyMannKendall)
- [scipy](https://scipy.org/)

## Installation

You can install `pyMannKendall` using pip. For Linux users

```python
sudo pip install pymannkendall
```

or, for Windows user

```python
pip install pymannkendall
```

or, you can use conda
```python
conda install -c conda-forge pymannkendall
```

or you can clone the repo and install it:

```bash
git clone https://github.com/mmhs013/pymannkendall
cd pymannkendall
python setup.py install
```

## Tests

`pyMannKendall` is automatically tested using `pytest` package on each commit [here](https://travis-ci.org/mmhs013/pyMannKendall/), but the tests can be manually run:

```
pytest -v
```

## Usage

A quick example of `pyMannKendall` usage is given below. Several more examples are provided [here](https://github.com/mmhs013/pyMannKendall/blob/master/Examples/Example_pyMannKendall.ipynb).

```python
import numpy as np
import pymannkendall as mk
# Data generation for analysis
data = np.random.rand(360,1)
result = mk.original_test(data)
print(result)
```
Output are like this:
```python
Mann_Kendall_Test(trend='no trend', h=False, p=0.9507221701045581, z=0.06179991635055463, Tau=0.0021974620860414733, s=142.0, var_s=5205500.0, slope=1.0353584906597959e-05, intercept=0.5232692553379981)
```
Whereas, the output is a named tuple, so you can call by name for specific result:
```python
print(result.slope)
```
or, you can directly unpack your results like this:
```python
trend, h, p, z, Tau, s, var_s, slope, intercept = mk.original_test(data)
```

## Citation

[![Google Scholar](https://github.com/mmhs013/Citation_Parser/blob/main/images/gs_pymk_cite.svg?raw=true)](https://scholar.google.com/scholar?q=pyMannKendall%3A+a+python+package+for+non+parametric+Mann+Kendall+family+of+trend+tests.)
[![Researchgate](https://github.com/mmhs013/Citation_Parser/blob/main/images/rg_pymk_cite.svg?raw=true)](https://www.researchgate.net/publication/334688255_pyMannKendall_a_python_package_for_non_parametric_Mann_Kendall_family_of_trend_tests)

If you publish results for which you used `pyMannKendall`, please give credit by citing [Hussain et al., (2019)](https://doi.org/10.21105/joss.01556):

> Hussain et al., (2019). pyMannKendall: a python package for non parametric Mann Kendall family of trend tests.. Journal of Open Source Software, 4(39), 1556, https://doi.org/10.21105/joss.01556

```
@article{Hussain2019pyMannKendall,
	journal = {Journal of Open Source Software},
	doi = {10.21105/joss.01556},
	issn = {2475-9066},
	number = {39},
	publisher = {The Open Journal},
	title = {pyMannKendall: a python package for non parametric Mann Kendall family of trend tests.},
	url = {http://dx.doi.org/10.21105/joss.01556},
	volume = {4},
	author = {Hussain, Md. and Mahmud, Ishtiak},
	pages = {1556},
	date = {2019-07-25},
	year = {2019},
	month = {7},
	day = {25},
}
```

## Contributions

`pyMannKendall` is a community project and welcomes contributions. Additional information can be found in the [contribution guidelines](https://github.com/mmhs013/pyMannKendall/blob/master/CONTRIBUTING.md).


## Code of Conduct

`pyMannKendall` wishes to maintain a positive community. Additional details can be found in the [Code of Conduct](https://github.com/mmhs013/pyMannKendall/blob/master/CODE_OF_CONDUCT.md).


## References

1. Bari, S. H., Rahman, M. T. U., Hoque, M. A., & Hussain, M. M. (2016). Analysis of seasonal and annual rainfall trends in the northern region of Bangladesh. *Atmospheric Research*, 176, 148-158. doi:[10.1016/j.atmosres.2016.02.008](https://doi.org/10.1016/j.atmosres.2016.02.008)

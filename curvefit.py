#fit function #################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Define film calibration function ############################################

def dose_response_curve(x, a, b):
    y = (a*x)/(1+b*x)
    return y

###############################################################################
# Input data for 100kV ########################################################
dose_100 = [6, 16, 40, 70, 120]
dR_100 = [0.03823258, 0.083857208, 0.150979853, 0.206926819, 0.25379452]

dose_100 = np.asarray(dose_100)
dR_100 = np.asarray(dR_100)
#plt.plot(dR_100, dose_100, 'o')


# Obtain best fit parameters a and b for 100kV ################################
parameters_100, covariance = curve_fit(dose_response_curve, dR_100, dose_100)
fit_100_a = parameters_100[0]
fit_100_b = parameters_100[1]

print('parameter a for curve 100 is:', fit_100_a)
print('parameter b for curve 100 is:', fit_100_b)

'''
# To plot the fitted curve 100 ################################################
fitted_curve_100 = dose_response_curve(dR_100, fit_100_a, fit_100_b)
plt.plot(dR_100, dose_100, 'o', label='100kV data points')
plt.plot(dR_100, fitted_curve_100, '-', label='100kV fitted curve')
plt.legend()
'''
###############################################################################
# Input data for 120kV ########################################################
dose_120 = [6, 16, 40, 70, 120]
dR_120 = [0.037675552, 0.082163905, 0.142951599, 0.200079086, 0.24666007]

dose_120 = np.asarray(dose_120)
dR_120 = np.asarray(dR_120)
#plt.plot(dR_120, dose_120, 'o')

# Obtain best fit parameters a and b for 120kV ################################

parameters_120, covariance = curve_fit(dose_response_curve, dR_120, dose_120)
fit_120_a = parameters_120[0]
fit_120_b = parameters_120[1]

print('parameter a for curve 120 is:', fit_120_a)
print('parameter b for curve 120 is:', fit_120_b)

'''
# To plot the fitted curve 120 ################################################
fitted_curve_120 = dose_response_curve(dR_120, fit_120_a, fit_120_b)
plt.plot(dR_120, dose_120, 'o', label='120kV data points')
plt.plot(dR_120, fitted_curve_120, '-', label='120kV fitted curve')
plt.legend()
'''
###############################################################################

###############################################################################
# Input data for 140kV ########################################################
dose_140 = [6, 16, 40, 70, 120]
dR_140 = [0.034509613, 0.077277466, 0.139722031, 0.192292384, 0.238410227]

dose_140 = np.asarray(dose_140)
dR_140 = np.asarray(dR_140)
#plt.plot(dR_140, dose_140, 'o')

# Obtain best fit parameters a and b for 140kV ################################

parameters_140, covariance = curve_fit(dose_response_curve, dR_140, dose_140)
fit_140_a = parameters_140[0]
fit_140_b = parameters_140[1]

print('parameter a for curve 140 is:', fit_140_a)
print('parameter b for curve 140 is:', fit_140_b)

'''
# To plot the fitted curve 140 ################################################
fitted_curve_140 = dose_response_curve(dR_140, fit_140_a, fit_140_b)
plt.plot(dR_140, dose_140, 'o', label='140kV data points')
plt.plot(dR_140, fitted_curve_140, '-', label='140kV fitted curve')
plt.legend()
'''
###############################################################################

###############################################################################
# Input data for 80kV ########################################################
dose_80 = [6, 16, 40, 70, 120]
dR_80 = [0.048724365, 0.091683629, 0.159818665, 0.219141169, 0.263824371]

dose_80 = np.asarray(dose_80)
dR_80 = np.asarray(dR_80)
#plt.plot(dR_80, dose_80, 'o')

# Obtain best fit parameters a and b for 80kV ################################

parameters_80, covariance = curve_fit(dose_response_curve, dR_80, dose_80)
fit_80_a = parameters_80[0]
fit_80_b = parameters_80[1]

print('parameter a for curve 80 is:', fit_80_a)
print('parameter b for curve 80 is:', fit_80_b)

'''
# To plot the fitted curve 80 ################################################
fitted_curve_80 = dose_response_curve(dR_80, fit_80_a, fit_80_b)
plt.plot(dR_80, dose_80, 'o', label='80kV data points')
plt.plot(dR_80, fitted_curve_80, '-', label='80kV fitted curve')
plt.legend()
'''
###############################################################################

###### Uncertainties ################################################

xerr_100 = [0.006757161, 0.007609685, 0.006578578, 0.006636581, 0.00671165, 0.006437251, 0.00614357, 0.006274862, 0.006605591, 0.006335403]
xerr_120 = [0.007128794, 0.007288289, 0.007009791, 0.006722885, 0.007163223, 0.006668294, 0.006859294, 0.006971634]
xerr_140 = [0.006915731, 0.006620117, 0.006601995, 0.006595286, 0.006633194, 0.006572032, 0.006576808, 0.006460653, 0.006421407, 0.00696111]
xerr_80 = [0.006528488, 0.006819789, 0.006852671, 0.006555781, 0.006703176, 0.007097768, 0.007065882, 0.007088323, 0.007323293]


# To plot smooth curves #######################################################
# use all x values to make curve smooth

x_all = np.linspace(0, 0.31, 100)
#print(type(x_all))

plt.plot(dR_100, dose_100, 'o', label='100kV data points')
plt.plot(dR_120, dose_120, 'o', label='120kV data points')
plt.plot(dR_140, dose_140, 'o', label='140kV data points')
plt.plot(dR_80, dose_80, 'o', label='80kV data points')

plt.plot(x_all, dose_response_curve(x_all, fit_120_a, fit_120_b), '-', label='120kV curve')
plt.plot(x_all, dose_response_curve(x_all, fit_100_a, fit_100_b), '-', label='100kV curve')
plt.plot(x_all, dose_response_curve(x_all, fit_140_a, fit_140_b), '-', label='140kV curve')
plt.plot(x_all, dose_response_curve(x_all, fit_80_a, fit_80_b), '-', label='80kV curve')



plt.xlabel('delta R')
plt.ylabel('Dose [mGy]')
plt.legend()
###############################################################


############## ERRORBARS ###############
'''
###########################################################################

# 80kV curve
# a = 216.64540348136268, b = -2.3745827531866266
xval_80 = dR_80
yval_80 = dose_80
yerr_80 = dose_80*0.1

fig, ax = plt.subplots()

ax.errorbar(xval_80, yval_80, xerr=xerr_80, yerr=yerr_80)
plt.xlabel('delta R')
plt.ylabel('Dose [mGy]')
plt.title('80kV curve with error bar')
plt.show()

'''

###########################################################################
'''
# 100kV curve
# a = 175.50412391356937, b = -2.4939697696188388
xval_100 = dR_100
yval_100 = dose_100
yerr_100 = dose_100*0.1

fig, ax = plt.subplots()

ax.errorbar(xval_100, yval_100, xerr=xerr_100, yerr=yerr_100)
plt.xlabel('delta R')
plt.ylabel('Dose [mGy]')
plt.title('100kV curve with error bar')
plt.show()

'''
###########################################################################
'''
# 120kV curve
# a = 243.28585118246392, b = -2.5211798814707254
xval_120 = dR_120
yval_120 = dose_120
yerr_120 = dose_120*0.1

fig, ax = plt.subplots()

ax.errorbar(xval_120, yval_120, xerr=xerr_120, yerr=yerr_120)
plt.xlabel('delta R')
plt.ylabel('Dose [mGy]')
plt.title('120kV curve with error bar')
plt.show()

'''
###########################################################################
'''
# 140kV curve
# a = 223.5040602243455, b = -2.5626066562710004
xval_140 = dR_140
yval_140 = dose_140
yerr_140 = dose_140*0.1

fig, ax = plt.subplots()

ax.errorbar(xval_140, yval_140, xerr=xerr_140, yerr=yerr_140)
plt.xlabel('delta R')
plt.ylabel('Dose [mGy]')
plt.title('140kV curve with error bar')
plt.show()

'''


























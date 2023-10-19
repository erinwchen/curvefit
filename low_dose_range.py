#Plot the dose response curves
#fit function #################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Define film calibration function ############################################
def dose_response_curve(x, a, m):
    y = a*x*(np.exp(m*x))
    return y

###############################################################################
# Input data for 100kV ########################################################
dose_100 = [4,6,7,10,16]
dR_100 = [0.041989751,0.03823258,0.055099599,0.065352091,0.083857208]

dose_100 = np.asarray(dose_100)
dR_100 = np.asarray(dR_100)
#plt.plot(dR_100, dose_100, 'o')


# Obtain best fit parameters a and m for 100kV ################################
parameters_100, covariance = curve_fit(dose_response_curve, dR_100, dose_100)
fit_100_a = parameters_100[0]
fit_100_m = parameters_100[1]

print('parameter a for curve 100 is:', fit_100_a)
print('parameter m for curve 100 is:', fit_100_m)

'''
# To plot the fitted curve 100 ################################################
fitted_curve_100 = dose_response_curve(dR_100, fit_100_a, fit_100_b)
plt.plot(dR_100, dose_100, 'o', label='100kV data points')
plt.plot(dR_100, fitted_curve_100, '-', label='100kV fitted curve')
plt.legend()
'''
###############################################################################
# Input data for 120kV ########################################################
dose_120 = [4,6,7,10,16]
dR_120 = [0.043808777,0.037675552,0.048642268,0.053739543,0.082163905]

dose_120 = np.asarray(dose_120)
dR_120 = np.asarray(dR_120)
#plt.plot(dR_120, dose_120, 'o')

# Obtain best fit parameters a and m for 120kV ################################

parameters_120, covariance = curve_fit(dose_response_curve, dR_120, dose_120)
fit_120_a = parameters_120[0]
fit_120_m = parameters_120[1]

print('parameter a for curve 120 is:', fit_120_a)
print('parameter m for curve 120 is:', fit_120_m)

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
dose_140 = [4,6,7,10,16]
dR_140 = [0.032667201,0.034509613,0.053369868,0.055657791,0.077277466]

dose_140 = np.asarray(dose_140)
dR_140 = np.asarray(dR_140)
#plt.plot(dR_140, dose_140, 'o')

# Obtain best fit parameters a and m for 140kV ################################

parameters_140, covariance = curve_fit(dose_response_curve, dR_140, dose_140)
fit_140_a = parameters_140[0]
fit_140_m = parameters_140[1]

print('parameter a for curve 140 is:', fit_140_a)
print('parameter m for curve 140 is:', fit_140_m)

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
dose_80 = [4,6,7,10,16]
dR_80 = [0.031854329,0.048724365,0.047121857,0.060702647,0.091683629]

dose_80 = np.asarray(dose_80)
dR_80 = np.asarray(dR_80)
#plt.plot(dR_80, dose_80, 'o')

# Obtain best fit parameters a and m for 80kV ################################

parameters_80, covariance = curve_fit(dose_response_curve, dR_80, dose_80)
fit_80_a = parameters_80[0]
fit_80_m = parameters_80[1]

print('parameter a for curve 80 is:', fit_80_a)
print('parameter m for curve 80 is:', fit_80_m)

'''
# To plot the fitted curve 80 ################################################
fitted_curve_80 = dose_response_curve(dR_80, fit_80_a, fit_80_b)
plt.plot(dR_80, dose_80, 'o', label='80kV data points')
plt.plot(dR_80, fitted_curve_80, '-', label='80kV fitted curve')
plt.legend()
'''
###############################################################################

###### Uncertainties ################################################
'''
xerr_100 = [0.006757161, 0.007609685, 0.006578578, 0.006636581, 0.00671165, 0.006437251, 0.00614357, 0.006274862, 0.006605591, 0.006335403]
xerr_120 = [0.007128794, 0.007288289, 0.007009791, 0.006722885, 0.007163223, 0.006668294, 0.006859294, 0.006971634]
xerr_140 = [0.006915731, 0.006620117, 0.006601995, 0.006595286, 0.006633194, 0.006572032, 0.006576808, 0.006460653, 0.006421407, 0.00696111]
xerr_80 = [0.006528488, 0.006819789, 0.006852671, 0.006555781, 0.006703176, 0.007097768, 0.007065882, 0.007088323, 0.007323293]
'''

# To plot smooth curves #######################################################
# use all x values to make curve smooth

x_all = np.linspace(0, 0.1, 100)
#print(type(x_all))

plt.plot(dR_100, dose_100, 'o', label='100kV data points')
plt.plot(dR_120, dose_120, 'o', label='120kV data points')
plt.plot(dR_140, dose_140, 'o', label='140kV data points')
plt.plot(dR_80, dose_80, 'o', label='80kV data points')

plt.plot(x_all, dose_response_curve(x_all, fit_120_a, fit_120_m), '-', label='120kV curve')
plt.plot(x_all, dose_response_curve(x_all, fit_100_a, fit_100_m), '-', label='100kV curve')
plt.plot(x_all, dose_response_curve(x_all, fit_140_a, fit_140_m), '-', label='140kV curve')
plt.plot(x_all, dose_response_curve(x_all, fit_80_a, fit_80_m), '-', label='80kV curve')


plt.title('Dose response curves (low dose range)')
plt.xlabel('delta R')
plt.ylabel('Dose [mGy]')
plt.legend()
###############################################################
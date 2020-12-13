import openpyxl, os, glob
import numpy as np
import matplotlib.pyplot as plt
import xlrd
'''
a= allantools.Dataset(data=x, data_type = 'freq',rate = 500, taus=interval)
a.compute("adev")
b = allantools.Plot()
b.plot(a, errorbars=True, grid=True)
c= allantools.Dataset(data=y, data_type = 'freq',rate = 500, taus=interval)
c.compute("adev")
b = allantools.Plot()
b.plot(c, errorbars=True, grid=True)
e= allantools.Dataset(data=z, data_type = 'freq',rate = 500, taus=interval)
e.compute("adev")
b = allantools.Plot()
b.plot(e, errorbars=True, grid=True)
b.show()'''
from pyexcel.cookbook import merge_all_to_a_book
from scipy import signal
import allantools
os.chdir("F://7th sem//EE 617")
wb = openpyxl.load_workbook('acc-data.xlsx')
sheet = wb.get_sheet_by_name('acc-data')
x = []
y = []
z = []
t = []
for i in range(5,20005):
    x.append(sheet['B' + str(i)].value)
    y.append(sheet['C' + str(i)].value)
    z.append(sheet['D' + str(i)].value)
    t.append(sheet['A' + str(i)].value)
#max interval = NTs/9 = 223
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)
z_min = min(z)
z_max = max(z)
x_diff = round(x_max - x_min, 5)
y_diff = round(y_max - y_min, 5)
z_diff = round(z_max - z_min, 5)
print(x_min,x_max, x_diff,y_min,y_max, y_diff,z_min,z_max, z_diff)
interval = []
X_min = x_min
#print(diff)
int_x = np.linspace(0.00281,0.054990,1000)
int_y = np.linspace(0.045490,0.045080,1000)
int_z = np.linspace(0.04,0.071180,1000)
print('offet in x = ', np.mean(x))
print('offet in y = ', np.mean(y))
print('offet in z = ', np.mean(z))
print('std of z = ', np.std(z))
# Compute a deviation using the Dataset class
#to get individual plots with error bars and grid lines
'''
a= allantools.Dataset(data=x, data_type = 'freq',rate = 500, taus=interval)
a.compute("adev")
b = allantools.Plot()
b.plot(a, errorbars=True, grid=True)
c= allantools.Dataset(data=y, data_type = 'freq',rate = 500, taus=interval)
c.compute("adev")
b = allantools.Plot()
b.plot(c, errorbars=True, grid=True)
e= allantools.Dataset(data=z, data_type = 'freq',rate = 500, taus=interval)
e.compute("adev")
b = allantools.Plot()
b.plot(e, errorbars=True, grid=True)
b.show()'''
arr = x
(tau_out, adev, adevrr,n) = allantools.adev(arr, rate=1.0, data_type='freq', taus=interval)
plt.loglog(tau_out, adev)
plt.show()
print(min(adev))
print(np.interp(1,tau_out,adev))
arr = y
(tau_out, adev, adevrr,n) = allantools.adev(arr, rate=1.0, data_type='freq', taus=interval)
plt.loglog(tau_out, adev)
plt.show()
print(min(adev))
print(np.interp(1,tau_out,adev))
arr = z
(tau_out, adev, adevrr,n) = allantools.adev(arr, rate=1.0, data_type='freq', taus=interval)
plt.loglog(tau_out, adev)
plt.show()
print(min(adev))
print(np.interp(1,tau_out,adev))
fs = 500 # as sample was taken after every 50 seconds 
f, psd = signal.periodogram(x, fs)
plt.semilogy(f, psd, linewidth=1.0, label='x-direction' )
plt.xlabel('Acceleration')
plt.ylabel('Periodogram')
plt.legend()
plt.show()
f, psd = signal.periodogram(y, fs)
plt.semilogy(f, psd, linewidth=1.0, label='y-direction')
plt.xlabel('Acceleration')
plt.ylabel('Periodogram')
plt.legend()
plt.show()
f, psd = signal.periodogram(z, fs)
plt.semilogy(f, psd, linewidth=1.0, label='z-direction')
plt.xlabel('Acceleration')
plt.ylabel('Periodogram')
plt.legend()
plt.show()

'''
print('std of x = ', np.std(x))
print('std of y = ', np.std(y))'''



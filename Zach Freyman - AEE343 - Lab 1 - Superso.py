#Zach Freyman - AEE343 - Lab 1 - Supersonic Wind Tunnel Calibration

#%%  Imports and Packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gamma = 1.4
base_path = r'C:\Users\zachf\Git\AEE343\Datasets'
 
data_files = {}

for i in range(1, 5,1):
    for j in range(600, 1201, 200):
        folder_path = f"{base_path}\\dataset_{i}"
        file_path = f"{folder_path}\\d{j}.dat"
    
        key = f"data{i}_{j}"
        data_files[key] = pd.read_csv(file_path, delim_whitespace=True)
# print(data_filesdata1_600)
variables = {}
time = {}

#%% Calculating Mach in test section based on isentropic relations
for i in range(1, 5):
    for j in range(600, 1201, 200):
        key = f"data{i}_{j}"
        df = data_files[key]
        time[f"time_{j}"] = df["Time"]
        variables[f"M{i}_{j}"] = np.sqrt((2 / (gamma - 1)) * ((df["Tap4P01"] / df["Tap3P1"])**((gamma - 1) / gamma) - 1))
        plt.plot(df["Time"], variables[f"M{i}_{j}"], label=f"M{i}_{j}")
        plt.ylim(1.75, 2.5)
        plt.xlim(4, 8)
        plt.xlabel('Time (sec)')
        plt.ylabel('Mach Number in Test Section')
        plt.title('Mach Number vs. Time - Isentropic Relations - All Datasets ')
        plt.legend(loc='upper right', shadow=True, fontsize='small')
plt.grid()

Average600 = sum(variables["M4_600"][30000:45000]) / 15000
print(Average600)
Average800 = sum(variables["M4_800"][30000:45000]) / 15000
print(Average800)
Average1000 = sum(variables["M4_1000"][30000:45000]) / 15000
print(Average1000)
Average1200 = sum(variables["M4_1200"][30000:45000]) / 15000
print(Average1200)
#%% Plotting
# 600
# for i in range(1,5):
#     key = f"data{i}_600"
#     df = data_files[key]
#     plt.plot(df["Time"], variables[f"M{i}_600"], label=f"M{i}")
#     plt.ylim(1.75, 2.5)
#     plt.xlim(4, 8)
#     plt.legend(loc='upper right', shadow=True, fontsize='small')

# #%% 800
# for i in range(1,5):
#     key = f"data{i}_800"
#     df = data_files[key]
#     plt.plot(df["Time"], variables[f"M{i}_800"], label=f"M{i}")
#     plt.ylim()
#     plt.xlim()
#     plt.legend(loc='upper right', shadow=True, fontsize='small')

# #%% 1000
# for i in range(1,5):
#     key = f"data{i}_1000"
#     df = data_files[key]
#     plt.plot(df["Time"], variables[f"M{i}_1000"], label=f"M{i}")
#     plt.ylim(1.75, 2.5)
#     plt.xlim(4, 8)
#     plt.legend(loc='upper right', shadow=True, fontsize='small')

# #%% 1200
# for i in range(1,5):
#     key = f"data{i}_1200"
#     df = data_files[key]
#     plt.plot(df["Time"], variables[f"M{i}_1200"], label=f"M{i}")
#     plt.ylim(1.75, 2.5)
#     plt.xlim(4, 8)
#     plt.legend(loc='upper right', shadow=True, fontsize='small')


# %% Importing data from set 4

data4_600 = pd.read_csv(r'C:\Users\zachf\Git\AEE343\Datasets\dataset_4\d600.dat', delim_whitespace=True)
data4_800 = pd.read_csv(r'C:\Users\zachf\Git\AEE343\Datasets\dataset_4\d800.dat', delim_whitespace=True)
data4_1000 = pd.read_csv(r'C:\Users\zachf\Git\AEE343\Datasets\dataset_4\d1000.dat', delim_whitespace=True)
data4_1200 = pd.read_csv(r'C:\Users\zachf\Git\AEE343\Datasets\dataset_4\d1200.dat', delim_whitespace=True)


P02_600 = data4_600[['Tap2P02']] + 14.7
time_600 = data4_600[['Time']] # Adding 14.7psi to account for pressure being recorded within gauge reference
P02_800 = data4_800[['Tap2P02']] + 14.7
P02_1000 = data4_1000[['Tap2P02']] + 14.7
P02_1200 = data4_1200[['Tap2P02']] + 14.7
# print(P02_600)

time_800 = data4_800[['Time']]
time_1000 = data4_1000[['Time']]
time_1200 = data4_1200[['Time']]

P1_600 = data4_600[['Tap3P1']]
P1_800 = data4_800[['Tap3P1']]
P1_1000 = data4_1000[['Tap3P1']]
P1_1200 = data4_1200[['Tap3P1']]
# print(P1_600)

Pratio_600 = (P02_600['Tap2P02'] /P1_600['Tap3P1'])
Pratio_800 = (P02_800['Tap2P02']/P1_800['Tap3P1'])
Pratio_1000 = (P02_1000['Tap2P02']/P1_1000['Tap3P1'])
Pratio_1200 = (P02_1200['Tap2P02']/P1_1200['Tap3P1'])
print(Pratio_600)

#%% Iteration Code (Takes Long Time to Run)
# 600
m = np.linspace(1,3, 1000)
M_guess600 = []
# print(m)
Pratio_raleigh = []
for i in range(0, len(Pratio_600)):
    j = 0
    while 0.001 < Pratio_600[i] - ((((((gamma + 1)**2) * (m[j]**2))/((4 * gamma * (m[j]**2)) - (2*(gamma - 1))))**(gamma/(gamma - 1))) * (((1 - gamma) + (2*(gamma * m[j]**2)))/(gamma + 1))):
        j+=1
    M_guess600.append(m[j])

print(M_guess600)

# 800
m = np.linspace(1,3, 1000)
M_guess800 = []
# print(m)
Pratio_raleigh = []
for i in range(0, len(Pratio_800)):
    j = 0
    while 0.001 < Pratio_800[i] - ((((((gamma + 1)**2) * (m[j]**2))/((4 * gamma * (m[j]**2)) - (2*(gamma - 1))))**(gamma/(gamma - 1))) * (((1 - gamma) + (2*(gamma * m[j]**2)))/(gamma + 1))):
        j+=1
    M_guess800.append(m[j])

print(M_guess800)

# 1000
m = np.linspace(1,3, 1000)
M_guess1000 = []
# print(m)
Pratio_raleigh = []
for i in range(0, len(Pratio_1000)):
    j = 0
    while 0.001 < Pratio_1000[i] - ((((((gamma + 1)**2) * (m[j]**2))/((4 * gamma * (m[j]**2)) - (2*(gamma - 1))))**(gamma/(gamma - 1))) * (((1 - gamma) + (2*(gamma * m[j]**2)))/(gamma + 1))):
        j+=1
    M_guess1000.append(m[j])

print(M_guess1000)

# 1200
m = np.linspace(1,3, 1000)
M_guess1200 = []
# print(m)
Pratio_raleigh = []
for i in range(0, len(Pratio_1200)):
    j = 0
    while 0.001 < Pratio_1200[i] - ((((((gamma + 1)**2) * (m[j]**2))/((4 * gamma * (m[j]**2)) - (2*(gamma - 1))))**(gamma/(gamma - 1))) * (((1 - gamma) + (2*(gamma * m[j]**2)))/(gamma + 1))):
        j+=1
    M_guess1200.append(m[j])

print(M_guess1200)

#%% Averaging and Plotting from Iteration
Average600R = sum(M_guess600[30000:45000]) / 15000
print(Average600R)
Average800R = sum(M_guess800[30000:45000]) / 15000
print(Average800R)
Average1000R = sum(M_guess1000[30000:45000]) / 15000
print(Average1000R)
Average1200R = sum(M_guess1200[30000:45000]) / 15000
print(Average1200R)


plt.plot(time_600 , M_guess600, label="Tunnel set to 600")
plt.plot(time_800 , M_guess800, label="Tunnel set to 800")
plt.plot(time_1000 , M_guess1000, label="Tunnel set to 1000")
plt.plot(time_1200 , M_guess1200, label="Tunnel set to 1200")
plt.legend(title='', loc='upper right', shadow=True, fontsize='small')
plt.xlabel('Time (sec)')
plt.ylabel('Mach Number in Test Section')
plt.xlim(1.8, 10)
plt.ylim(1, 2.5)
plt.title('Mach Number vs. Time - Raleigh Pitot Tube Method')
plt.grid()


#%% Building Calibration Plot
TunnelSetting = [600, 800, 1000, 1200]
IsenMach = [Average600, Average800, Average1000, Average1200]
RaleighMach = [Average600R, Average800R, Average1000R, Average1200R]
plt.plot(TunnelSetting, IsenMach, label="Isentropic Calibration")
plt.plot(TunnelSetting, RaleighMach, label="Raleigh Calibration")
plt.grid()
plt.xlabel('Tunnel Throat Setting')
plt.ylabel('Mach Number in Test Section')
plt.legend(loc='upper left', shadow=True, fontsize='small')

#%% Generating Theoretical Plots regarding error induced by inaccuracy in P02 and P1

gamma = 1.4
M = np.linspace(1, 3, 100)
P02 = [33, 35, 37, 39, 41, 43, 45]

# Plotting Mach versus Static Pressure 1 with variable Total Pressure 2
for i in range(0, len(P02)):
    P1 =  P02[i] / ((((((gamma + 1)**2) * (M**2))/((4 * gamma * (M**2)) - (2*(gamma - 1))))**(gamma/(gamma - 1))) * (((1 - gamma) + (2*(gamma * M**2)))/(gamma + 1)))
    plt.plot(P1, M)
    plt.title('Mach Number vs. P1')
    plt.ylim(1.3, 3)
    plt.xlim(4, 12)
    plt.legend(P02, title='Po2 (psi)' , loc='upper right', shadow=True, fontsize='small')
    plt.grid()
    plt.xlabel('Static Pressure P1 (psi)')
    plt.ylabel('Mach Number')

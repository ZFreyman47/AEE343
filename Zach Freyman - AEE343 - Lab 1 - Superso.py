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
 
variables = {}
time = {}

#%% Calculating Mach in test section based on isentropic relations
for i in range(1, 5):
    for j in range(600, 1201, 200):
        key = f"data{i}_{j}"
        df = data_files[key]
        time[f"time_{j}"] = df["Time"]
        variables[f"M{i}_{j}"] = np.sqrt((2 / (gamma - 1)) * ((df["Tap4P01"] / df["Tap3P1"])**((gamma - 1) / gamma) - 1))

#%% Plotting
# 600
for i in range(1,5):
    key = f"data{i}_600"
    df = data_files[key]
    plt.plot(df["Time"], variables[f"M{i}_600"], label=f"M{i}")
    plt.ylim(1.75, 2.5)
    plt.xlim(4, 8)
    plt.legend(loc='upper right', shadow=True, fontsize='small')

#%% 800
for i in range(1,5):
    key = f"data{i}_800"
    df = data_files[key]
    plt.plot(df["Time"], variables[f"M{i}_800"], label=f"M{i}")
    plt.ylim(1.75, 2.5)
    plt.xlim(4, 8)
    plt.legend(loc='upper right', shadow=True, fontsize='small')

#%% 1000
for i in range(1,5):
    key = f"data{i}_1000"
    df = data_files[key]
    plt.plot(df["Time"], variables[f"M{i}_1000"], label=f"M{i}")
    plt.ylim(1.75, 2.5)
    plt.xlim(4, 8)
    plt.legend(loc='upper right', shadow=True, fontsize='small')

#%% 1200
for i in range(1,5):
    key = f"data{i}_1200"
    df = data_files[key]
    plt.plot(df["Time"], variables[f"M{i}_1200"], label=f"M{i}")
    plt.ylim(1.75, 2.5)
    plt.xlim(4, 8)
    plt.legend(loc='upper right', shadow=True, fontsize='small')


# %%

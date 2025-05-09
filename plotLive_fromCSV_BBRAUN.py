import pandas as pd
import numpy as np
from  matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path
import shelve

def to_binary(num,index):
    return int(bin(num).split('b')[1].rjust(2,'0')[index])

vect_to_binary = np.vectorize(to_binary)

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({"legend.frameon": True})
MAX_FRAMES = 200

FolderPath = Path('D:/BBRAUN/Datalog')

with shelve.open(str(FolderPath/'filePath')) as shelfFile:
    #FolderPath = shelfFile['folderPath']
    todayPath = shelfFile['currentFile']
    print(todayPath)

def animate(i):
    data = pd.read_csv(todayPath, delimiter=',')

    ax1.cla()
    ax1.grid()
    #axs[0,0].cla()
    #axs[1,0].cla()
    #axs[2,0].cla()
    
    #axs[0,0].grid()
    #axs[1,0].grid()
    #axs[2,0].grid()
    
    if len(data)<=200:
        ax1.plot(data.iloc[:,2]/100, label='Pos1')
        ax1.plot([2]*len(data), linestyle='dashed', color = 'black')
        ax1.plot([125]*len(data), linestyle='dashed', color = 'black')
        #axs[0,0].plot(data.iloc[:,2]/100, label='Pos1')
        #axs[1,0].plot(data.iloc[:,3]/100, label='Pos2_1')
        #axs[2,0].plot(data.iloc[:,4]/100, label='Pos2_2')
        
    else:
        ax1.plot(data.iloc[-200:,2]/100, label='Pos1')
        ax1.plot(data.iloc[-200:,2].index, [2]*200, linestyle='dashed',
                 color = 'black')
        ax1.plot(data.iloc[-200:,2].index, [125]*200, linestyle='dashed',
                 color = 'black')
        #axs[0,0].plot(data.iloc[-200:,2]/100, label='Pos1')
        #axs[1,0].plot(data.iloc[-200:,3]/100, label='Pos2_1')
        #axs[2,0].plot(data.iloc[-200:,4]/100, label='Pos2_2')

    ax1.grid()
    #axs[0,0].grid()
    #axs[1,0].grid()
    #axs[2,0].grid()

    plt.tight_layout()

#fig, axs = plt.subplots(3,2,sharex=True)
fig, ax1 = plt.subplots(1,1,sharex=True)
ani = FuncAnimation(fig, animate, interval= 1000, save_count=MAX_FRAMES)

#plt.tight_layout()
plt.show()
plt.close(fig)


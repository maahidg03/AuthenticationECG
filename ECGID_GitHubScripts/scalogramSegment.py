import os
import numpy as np
import matplotlib.pyplot as plt
import pywt
from PIL import Image

path = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/Segments"
path1 = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/Scalograms"

for subject_name in os.listdir(path):
    print(subject_name)
    if subject_name == ".DS_Store":
        continue
    if not os.path.isdir(path1+"/"+subject_name):
        os.makedirs(path1+"/"+subject_name)

    for items in os.listdir(path+"/"+subject_name):
        # print(items)
        if items.endswith(".csv"):
            segLabel = items.rsplit(".", 1)[0]
            print(segLabel)
            scalName = str(segLabel)+".png"
            df1 = np.genfromtxt(path+"/"+subject_name+"/"+items, delimiter=',')
            im1 = df1
            cwtmatr, freqs = pywt.cwt(im1, 14, 'mexh', sampling_period=500)
            plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
                       vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
            plt.savefig(path1+"/"+subject_name+"/"+scalName)
            plt.close()
            del(im1)
            del(df1)

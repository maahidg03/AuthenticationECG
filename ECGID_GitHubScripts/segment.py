import os
import numpy as np

import wfdb as wf
import random
from matplotlib import pyplot as plt
import csv

#from helper import save_to_csv

# experimental package: adding a package for detecting r peaks using pan tomkins algorithm
from ecgdetectors import Detectors
detectors = Detectors(500)

path = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/Butterworth"
path1 = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/Segments"

for subject_name in os.listdir(path):
    print(subject_name)
    if subject_name == ".DS_Store":
        continue

    if not os.path.isdir(path1+"/"+subject_name):
        os.makedirs(path1+"/"+subject_name)

    count = 0
    for items in os.listdir(path+"/"+subject_name):
        # print(items)
        if items.endswith(".csv"):
            path3 = path+"/"+subject_name+"/"+items
            path4 = path1+"/"+subject_name
            df1 = np.genfromtxt(path3, delimiter=',')
            r_peaks = detectors.pan_tompkins_detector(df1)
            #print("R_Peaks length:", len(r_peaks))

        r2r_sum = 0
        for i in range(len(r_peaks)-1):
            r2r = r_peaks[i+1]-r_peaks[i]
            r2r_sum += r2r

        r2r_avg = r2r_sum/len(r_peaks)
        distance = r2r_avg/2
        for peak in r_peaks:
            count += 1
            i = int(peak - distance) if (peak - distance) > 0 else 0
            j = int(peak + distance) if (peak +
                                         distance) < len(df1) else len(df1)
            segment = df1[i:j+1]
            segment_for_csv = np.array(segment, dtype=np.float)
            # print("length of segment:",len(segment))
            # print(count)
            # print(len(segment_for_csv))
            nameAdd = "seg"+str(count)+".csv"
            FILE_PATH1 = os.path.join(path4, nameAdd)
            # print(FILE_PATH1)
            np.savetxt(FILE_PATH1, segment_for_csv, delimiter=",", fmt="%.2f")

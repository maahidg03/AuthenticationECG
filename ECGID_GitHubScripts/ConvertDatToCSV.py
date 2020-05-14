# WaveForm-Database package. A library of tools for reading, writing, and processing WFDB signals and annotations.
import os
import wfdb as wf
import pandas as pd
import numpy as np
import glob

path = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/ecg-id-database-1.0.0"
path2 = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/ECG_Records_CSV"
for subject_name in os.listdir(path):
    print(subject_name)
    if subject_name == ".old":
        continue
    if subject_name == "images":
        continue
    if subject_name == "ANNOTATORS":
        continue
    if subject_name == "biometric.shtml":
        continue
    if subject_name == "README":
        continue
    if subject_name == "RECORDS":
        continue
    if subject_name == "SHA256SUMS.txt":
        continue
    if subject_name == ".DS_Store":
        continue

    if not os.path.isdir(path2+"/"+subject_name):
        os.makedirs(path2+"/"+subject_name)
        # print(path1+"/"+subject_name)

    for items in os.listdir(path+"/"+subject_name):
        if items.endswith(".dat"):
            print(items)
            path3 = path+"/"+subject_name
            path4 = path2+"/"+subject_name
            # print(path3)
            base = os.path.basename(path+"/"+subject_name+"/"+items)
            recordingLabel = os.path.splitext(base)[0]
            FILE_PATH = os.path.join(path3, recordingLabel)
            FILE_PATH1 = os.path.join(path4, recordingLabel+'.csv')
            record = wf.rdsamp(FILE_PATH, channels=[0])
            record = np.asarray(record[0])
            np.savetxt(FILE_PATH1, record, delimiter=",", fmt="%.2f")

from scipy.signal import butter, filtfilt
import scipy.signal
import os
import numpy as np

path = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/ECG_Records_CSV"
path1 = "/Users/maahichatterjee/Desktop/Semester 4/Cmpe295B/ECGID/Butterworth"

for subject_name in os.listdir(path):
    # print(subject_name)

    if not os.path.isdir(path1+"/"+subject_name):
        os.makedirs(path1+"/"+subject_name)

    for items in os.listdir(path+"/"+subject_name):
        # print(items)
        if items.endswith(".csv"):
            path3 = path+"/"+subject_name+"/"+items
            path4 = path1+"/"+subject_name
            base = os.path.basename(path+"/"+subject_name+"/"+items)
            recordingLabel = os.path.splitext(base)[0]

            df1 = np.genfromtxt(path3, delimiter=',')
            # print(df1)
            nyq = 0.5 * 500
            low = 5 / nyq
            high = 50 / nyq
            order = 5

            b, a = scipy.signal.butter(
                order, [low, high], 'bandpass', analog=False)
            y = scipy.signal.filtfilt(b, a, df1, axis=0)
            # print(y)
            FILE_PATH1 = os.path.join(path4, recordingLabel+'.csv')
            np.savetxt(FILE_PATH1, y, delimiter=",", fmt="%.2f")


"""
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y
"""

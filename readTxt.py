import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

col_name = ["5:00", "5:20", "5:30", "5:40", "5:50", "6:00", "6:10", "6:20", "6:30", "6:40", "6:50", "7:00", "7:10", "7:20", "7:30", "7:40", "7:50", "8:00", "8:10", "8:20", "8:30", "8:40", "8:50", "9:00", "9:10", "9:20", "9:30", "9:40", "9:50", "10.00"]

data_arr = []
list_files = os.listdir('txt/')

#sort date
list_files.sort()


for file in list_files:

    row = []
    with open('txt/'+file, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            row.append(int(currentPlace))

        if len(row) < 30:
            miss_col = 30 - len(row)

            #in case miss some last cols
            for i in range (miss_col):
                row.append(0)

        data_arr.append(row)

df = pd.DataFrame(data_arr, columns= col_name, index=list_files)

print(df)

print()

# start plot graph

fig, axs = plt.subplots(df.shape[0])
fig.suptitle('amount of people vs time for each day')
for i in range (df.shape[0]):
    axs[i].plot(col_name, df.iloc[i])

plt.show()

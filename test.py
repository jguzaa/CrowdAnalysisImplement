import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#col_name = ["5:00-5:30", "5:30-6:00", "6:00-6:30", "6:30-7:00", "7:00-7:30", "7:30-8:00", "8:00-8:30", "8:30-9:00", "9:00-9:30", "9:30-10:00"]

#df = pd.DataFrame([[0,1,2,4,5,3,5,0,1,4]], columns= col_name)

for file_no in range(4):

    data_arr = []
    ppl_count_temp = 0

    for current_frame in range(18000):

        ppl_count_temp += random.randint(0,10)
        if(current_frame % 600) == 0:

            data_arr.append(int(ppl_count_temp/600))
            ppl_count_temp = 0

    with open('txt/'+ str(file_no+1) +'Aug', 'w') as filehandle:
        for listitem in data_arr:
            filehandle.write('%s\n' % listitem)

    print(data_arr)

    print()
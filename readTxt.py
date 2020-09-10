import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import operator

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

df = pd.DataFrame(data_arr, columns = col_name)

print(df)

# create the list of the day which data collected
days = pd.DataFrame(list(range(1, df.shape[0]+1)), columns = ['day'])

# train the system which X is the day and Y is the number of ppl in each period
X_train, X_test, y_train, y_test = train_test_split(days, df, test_size=0.2, random_state=5)

# model instantiation
lm = LinearRegression()

# fitting model for each time period then add to predict list
predict_list = []
trending_list = []
score_list = []

for period in col_name:
    lm.fit(X_train, y_train[period])
    predict_val = lm.predict([[df.shape[0]+1]])
    if predict_val >= 0:
        predict_list.append(predict_val[0])
    else:
        predict_list.append(0)
    trending_list.append(lm.coef_[0])
    score_list.append(lm.score(X_test, y_test[period]))

print(score_list)

# Looking for beta value which shows the trend of number in future
index_max, value_max = max(enumerate(trending_list), key=operator.itemgetter(1))
index_min, value_min = min(enumerate(trending_list), key=operator.itemgetter(1))

# Match with the period of time
print("The period which most tend to have more customer ", col_name[index_max])
print("The period which most tend to lost customer ", col_name[index_min])

# start plot graph
fig, axs = plt.subplots(df.shape[0]+1, sharex=True, sharey=True, gridspec_kw={'hspace': 1})
fig.suptitle('amount of people vs time for each day')
count = 0
for i in range (df.shape[0]):
    axs[i].title.set_text(list_files[i])
    axs[i].plot(col_name, df.iloc[i])
    count += 1
axs[count].title.set_text("Prediction")
axs[count].plot(col_name, predict_list)

for ax in axs.flat:
    ax.set(xlabel='time', ylabel='no. ppl')
    ax.label_outer()

plt.show()


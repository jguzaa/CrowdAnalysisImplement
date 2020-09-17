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


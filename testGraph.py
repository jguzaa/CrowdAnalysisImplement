import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Generate mock up matrix
#column represent the period every 10 minute
#row represent the day
#the number in matrix represent the avreage number of people in 10 minutes

data = np.random.randint(10, size=(7, 30))

barHrRef = np.arange(30)

print(data)

#print(data[0])

#plt.figure(figsize=(40,10))
plt.bar(barHrRef, data[0], color="blue")
plt.title("The crowd amount vs time")
plt.xlabel("time")
plt.ylabel("no of ppl")
plt.show()

#multiple line plot
plt.plot(barHrRef, data[0], "b",
         barHrRef, data[1], "r",)
plt.legend(["3rd Aug", "4th Aug"])
plt.show()


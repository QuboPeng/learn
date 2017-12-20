import pandas

foodInfo = pandas.read_csv("food_info.csv")


print(type(foodInfo))
print(foodInfo.dtypes)

# print(help(foodInfo.head()))
print(foodInfo.head(3))
print(foodInfo.tail(3))
print(foodInfo.columns)
print(foodInfo.shape)
foodInfo.sort_values("Water_(g)", inplace=True)
print("-------------------")
print(foodInfo)
print("---------numpy----------")

import numpy

titanic = pandas.read_csv("titanic_train.csv")




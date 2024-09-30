import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("Iris.csv")
sns.displot(iris['SepalLengthCm'], kde=True, rug=True)
plt.title("Distribution of Sepal Length")
plt.show()

sns.histplot(iris['PetalWidthCm'], kde=True, bins=20)
plt.title("Histogram of Petal Width")
plt.show()

sns.relplot(x="SepalLengthCm", y="SepalWidthCm", data=iris,hue="Species",style="Species")
plt.title("Sepal Length v/s Sepal Width")
plt.show()

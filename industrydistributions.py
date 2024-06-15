import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Billionaires Statistics Dataset.csv')  # reading the csv file

groupByFrame = df.groupby('industries').size().sort_values(ascending=False)  # grouping, identifying number and sorting

industry_counts_dict = groupByFrame.to_dict()  # turning pandas series to dictionary

labels = industry_counts_dict.keys()  # adding labels to chart
sizes = industry_counts_dict.values()  # creating sizes of chart

plt.pie(sizes, labels=labels)  # creating the chart
#plt.axis('equal')
plt.title('Industry Distribution')
plt.show()

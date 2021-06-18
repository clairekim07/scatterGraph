import pandas as panda
import plotly.express as plot
import csv

df = panda.read_csv("studentData.csv")
mean = df.groupby(["attempt"].mean()
graph = plot.scatter(df,y="level" ,x="student_id" ,color=mean,size= 5)
graph.show()
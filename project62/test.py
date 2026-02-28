import pandas as pd

df=pd.read_csv("C:/Users/CASPER/Desktop/python_projects/project62/song_names.csv").iloc[549:599]

for index,row in df.iterrows():
    print(row[0])


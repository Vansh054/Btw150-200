import pandas as pd 

df = pd.read_csv("calculated.csv")
radius = df['Radius'].tolist()
mass = df['Mass'].tolist()
gravity = df['Gravity'].tolist()

btw150and200 = []

for i in gravity:
    if(i>=150 and i<=200) :
        btw150and200.append(i)

print(btw150and200)
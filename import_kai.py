import pandas as pd

df=pd.read_csv('data2018_2019.csv', skiprows=5)

#print(df)

df.sort_index()
print(df)

df.dropna(how='any', inplace=True)
df.drop(['8','1','8.1','1.1','0','1.2','8.2','1.3'], axis=1, inplace=True)

print(df)
all_list=[]
date=[]
temp=[]
pres=[]
weat=[]
humi=[]
count=0


for i in df:
    all_list=df.values.flatten()

    date.append(i)
    temp.append(i)
    pres.append(i)
    weat.append(i)
    humi.append(i)

#slice SAIKO!
date=all_list[::5]
temp=all_list[1::5]
pres=all_list[2::5]
weat=all_list[3::5]
humi=all_list[4::5]

print(all_list)
#print(humi)
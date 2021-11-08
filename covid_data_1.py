import pandas as pd
import numpy as np
import plotly.express as px


ct1 = pd.read_csv (r'C:\Users\Dulmi\Desktop\covid_mobility_dataset_with_missing_values1.csv',header=None)   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print (ct1)

Field_Name= ct1[1] +"-"+ ct1[2]
print(Field_Name)

Description = ct1[1] +"-"+ ct1[2]+":"+ ct1[3]
print(Description)

#cols=list(ct1.columns.values)
#ct1=ct1[[cols[-1]]+cols[4:417]]
print(ct1)
#ct1=ct1[cols[4:417]]
#print(ct1)
print (ct1.dtypes)

ct1_tr = ct1.transpose()
print(ct1_tr)
Pandas_Data_Type=ct1_tr.dtypes
print (Pandas_Data_Type)

for i in range(559):
   ct1_tr[i] = pd.to_numeric(ct1_tr[i], errors='coerce')




print (ct1_tr.dtypes)


print(ct1_tr.describe())

ct9=ct1_tr.describe().loc[['mean', 'min', 'max']]
print(ct9)
ct9_tr = ct9.transpose()
print(ct9_tr)
Min_Max=ct9_tr.drop(labels='mean', axis=1)
print(Min_Max)

print (Min_Max.dtypes)

Min_Max['min'] =Min_Max['min'].astype(str)
Min_Max['max'] = Min_Max['max'].astype(str)
print (Min_Max.dtypes)
Data_Scale = "("+Min_Max['min']+")" +"-" + "(" +Min_Max['max']+")"
print(Data_Scale)
#print(ct1_tr.iloc[].describe())

print(ct1.info())
print(ct1_tr.info())


#for i in range(559):
    #print(ct1_tr[i].unique())
Unique_Value_Count=ct1_tr.nunique()
print(Unique_Value_Count)

#print(len(ct1_tr.index) - ct1_tr.count())
Missing_Value_Count=ct1_tr.isnull().sum(axis=0)
print(Missing_Value_Count)




dat1 = pd.concat([Field_Name,Description,Pandas_Data_Type,Data_Scale,Min_Max,Unique_Value_Count,Missing_Value_Count], axis=1)
dat1.columns = ['Field Name', 'Description ', 'Panda Data Type', 'Data Scale','Min. Value','Max. Value','Unique Values','Missing Value Count']
print(dat1)
dat1.to_csv(r'C:\Users\Dulmi\Desktop\dat1.csv')

#plotly.express.scatter(data_frame=dat1, x='Field Name', y='Min. Value')



df = px.data.iris()
fig = px.scatter(df, x=dat1['Field Name'], y=dat1['Min. Value'])
fig.show()

df = px.data.tips()
fig = px.pie(df, values=dat1['Min. Value'], names=dat1['Field Name'])
fig.show()


df = px.data.tips()
fig = px.histogram(df,x=dat1['Field Name'], y=dat1['Min. Value'])
fig.show()
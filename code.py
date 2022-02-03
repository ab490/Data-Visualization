#Name: Anooshka Bajaj


#1
import pandas as pd
df=pd.read_csv(r'E:\landslide_dataset.csv')
pd.set_option('display.max_columns',50)        #to display all the columns
print(df.describe())                  #gives statistical values of the data
print(df[df.columns[2:]].mode())      #for finding out mode


#2

#2(a)
import matplotlib.pyplot as plt
attributes1=['temperature','humidity','pressure','lightavgw/o0','lightmax','moisture']
fig,axs=plt.subplots(nrows=3,ncols=2,figsize=(11,16))

r=0;c=0
for i in attributes1:
    x = df['rain']
    y=df[i]
    axs[r][c].scatter(x,y,color='red',marker='*')
    axs[r][c].set_title(i +' vs rain')
    axs[r][c].set_xlabel('rain')
    axs[r][c].set_ylabel(i)
    c+=1
    if c==2:
        r+=1;c=0
    
plt.show()

#2(b)
attributes2=['humidity','pressure','rain','lightavgw/o0','lightmax','moisture']
fig,axs=plt.subplots(nrows=3,ncols=2,figsize=(11,16))

r=0;c=0
for i in attributes2:
    x = df['temperature']
    y=df[i]
    axs[r][c].scatter(x,y,color='red',marker='*')
    axs[r][c].set_title(i +' vs temperature')
    axs[r][c].set_xlabel('temperature')
    axs[r][c].set_ylabel(i)
    c+=1
    if c==2:
        r+=1;c=0
    
plt.show()


#3

#3(a)
c1=df.corrwith(df['rain'])       #finding correlation coefficient with rain
print('Correlation Coeffecient of rain with:')
print(c1)

#3(b)
c2=df.corrwith(df['temperature'])   #finding correlation coefficient with temperature
print('Correlation Coefficient of temperature with:')
print(c2)


#4
plt.hist(df['rain'],label='rain')     #plotting histogram with rain
plt.xlabel('rain')
plt.ylabel('frequency')
plt.legend()
plt.show()

plt.hist(df['moisture'],label='moisture')     #plotting histogram with moisture
plt.xlabel('moisture')
plt.ylabel('frequency')
plt.legend()
plt.show()


#5
g=df.groupby('stationid')             
fig,axs=plt.subplots(nrows=5,ncols=2,figsize=(11,30))
r=0;c=0
for i in g['rain']:
    axs[r][c].hist(i[1],label='rain')
    axs[r][c].set_title(i[0])
    axs[r][c].set_xlabel('Rain')
    axs[r][c].set_ylabel('Frequency')
    axs[r][c].legend()
    c+=1
    if c==2:
        r+=1;c=0

plt.show()


#6
df.boxplot(column=['rain'], figsize=(8,8))    #boxplot for rain
plt.ylabel('Amount of rainfall in ml')
plt.show()

df.boxplot(column=['moisture'], figsize=(8,8))     #boxplot for moisture
plt.ylabel('Moisture content in percentage')
plt.show()












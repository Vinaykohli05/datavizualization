import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
#list storing date in string formate
'''date=["25/12","26/12","27/12"]
print(date)
temp=[8.5,10.5,6.8]
print(temp)'''
#create a figure plotting temp vs date




'''date=("25/12","26/12","27/12")
print(date)
temp=(8.5,10.5,6.8)
print(temp)
plt.plot(date,temp)
plt.show()'''

#plt.savefig('x.png')

#functions in matplotlib

#grid([b,which,axis])configure the grid line
#legend('  ')place legend on axis
#save fig('   ')#save the current figure
#show('   ')display all figures
#title  (' label ' )set a title for the axis
#xlabel('label for x axis')
#ylabel('set a label for yaxis')
#xticks()set the current tick locations
#yticks()set the current tick locations

'''plt.plot(date,temp,marker='d',color='k',markersize=6,linestyle='dashdot',)
plt.title("date wise temp")
plt.xlabel("date")
plt.ylabel("temperature")
plt.grid(True)
plt.yticks(temp)
plt.xticks(date)
plt.show()'''
#marker . point,o circle,v tri down, ^ tri up ,tri left, tri right,x star,
#color=blue, green ,red,cyan,magenta,yellow,black,white

'''height=[121.9,124.5,126.5,134.6,139.7,147.3,152.4,153.5,162.6]
print(height)
weight=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]
print(weight)'''

'''plt.plot(height,weight,marker='d',color='y',markersize=10,linewidth=5,linestyle='dashed')
plt.title(height and weight)
plt.xlabel("height")
plt.ylabel("weight")
plt.grid(True)
plt.yticks(height)
plt.xticks(weight)
plt.show()'''

#plottting scatter chart.
'''discount=np.array([10,20,30,40,50])
salesinRS=np.array([140000,45000,50000,48000,100000])
plt.scatter(discount,salesinRS,color='k',marker='d')
plt.title('sales vs discount')
plt.xlabel('dicount offered')
plt.ylabel('sales in rs')
plt.show()'''





'''discount=np.array([10,20,30,40,50])
salesinRS=np.array([140000,45000,50000,48000,100000])
size=discount*50
plt.scatter(x=discount,y=salesinRS,color='r',marker='*',linewidth=5,edgecolor='b',s=size)
plt.title('sales vs discount')
plt.xlabel('dicount offered')
plt.ylabel('sales in rs')'''

'''data={'name':['arnav','sheela','azhar','bincy','yash','nazar'],
      'height':[60,61,63,65,61,60],
      'weight':[47,89,52,58,50,47]}
print(data)
data=pd.DataFrame(data)
print(data)
data.plot(kind='hist',edgecolor='c',linewidth=3,linestyle='dotted',fill=True,hatch='o',bins=[18,19,20,21,22])
plt.show()'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''discount = np.array([10, 20, 30, 40, 50])
salesinRS = np.array([140000, 45000, 50000, 48000, 100000])

plt.pie(
    salesinRS,
    labels=discount,
    
    startangle=90
)

plt.title("Sales by Discount")
plt.show()'''






'''plt.show()
fig,ax=plt.subplots(subplots_kw=("projection":"3"))
ax.bar3d()'
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
plt.show()'''
'''def my_plotter(ax,d1,d2,param_dict):
    out=ax.plot(d1,d2,**param_dict)
    return out
d1,d2,d3,d4=np.random.randn(4,100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5,2.7))

my_plotter(ax1,d1,d2,{'marker':'x'})
my_plotter(ax2,d3,d4,{'marker':'o'})

#styling artist
fig,ax=plt.subplots(figsize=(5,3))
x=np.arange(len(d1,))
ax.plot(x,np.cumsum(d1),color='c',linewidth=3,linestyle='--')
new,=ax.plot(x,np.cumsum(d2),color='k',linewidth=8,linestyle='dotted')
new.set_linestyle(':')

fig,ax=plt.subplots(figsize=(5,4))
ax.plot(d1,'o',label='data1')
ax.plot(d2,'d',label='data2')
ax.plot(d3,'v',label='data3')
ax.plot(d4,'s',label='data4')
ax.legend()



mu,sigma=115,15
x=mu+sigma*np.random.randn(10000)
fig,ax=plt.subplots(figsize=(5,3),layout='constrained')
#hist
n,bins,patches=ax.hist(x,50,density=True,color='r',alpha=0.75)

#annotations
fig,ax=plt.subplots(figsize=(5,2))
t=np.arange(0,5,0.01)
s=np.cos(2*np.pi*t)
line,=ax.plot(t,s, lw=2)
ax.annotate('local max',xy=(2,1),
            xytext=(3,2),arrowprops=dict(facecolor='r',shrink=0.1))
ax.set_ylim(-2,2)

#legends
fig,ax=plt.subplots(figsize=(5,6))
ax.plot(np.arange(len(d1)),d1,label='data1')
ax.plot(np.arange(len(d2)),d2,label='data2')
ax.plot(np.arange(len(d3)),d3,'d',label='data3')
ax.legend()


fig,axs=plt.subplots(2,2,figsize=(5,3))
xdata=np.arange(len(d1))
data=10**d1
axs[0,0].plot(xdata,data)
axs[1,0].set_yscale('log')
axs[1,0].plot(xdata,data)
plt.show()'''

#using open data
'''cgp=pd.read_csv(r"C:/Users/PC/Downloads/Quote-Equity-CGPOWER-EQ-07-09-2025-07-09-2026.csv")
print(cgp)

df=pd.DataFrame(cgp)
print(df)'''
      
#plot hist
'''df.plot(kind='hist',y='HIGH')
plt.xlabel("number")
plt.ylabel("change price")
plt.legend()

plt.show()'''

'''df.plot(kind='hist',y='LOW')'''
'''df.plot(kind='hist',y='OPEN')

df.plot(kind='hist',y='CLOSE')'''

'''df.plot(kind='hist',y='SERIES')'''
'''df.plot(kind='hist',y='52 WEEK HIGH')
plt.show()

plt.show()


cgp.info()  '''
'''df.plot(kind='hist',y='52 WEEK LOW')
plt.show()'''
'''df.plot(kind='hist',y='LTP')

plt.show()'''

'''df.plot(kind='pie',y='HIGH',color='r')
plt.title("performance analysis")
plt.xlabel("numbers")
plt.ylabel("change price")
plt.show()'''

'''df=pd.DataFrame({'geoarea':[83743,78438,22429,21081,165579,9486,123456],
                 'forestcover':[61759,27692,17280,17321,19240,13464,8073]},
                index=['arunachal','assam','manipur','meghlaya','mizoram','nagaland','tripura'])
print(df)

exp=[0.1,0,0,0,0.2,0,0]
df.plot(kind='pie',y='forestcover')

c=['r','g','m','c','brown','pink','purple']


plt.show()'''

#seaborn

#relationship plot
import seaborn as sns
                                                                                                                                                                                                         
tips=sns.load_dataset("tips")
print(tips)
sns.relplot(data=tips,x="total_bill",y="tip",color="c",hue="smoker",style="time")
sns.relplot(data=tips,x="total_bill",y="tip",color='r')

sns.relplot(data=tips,x="total_bill",y="tip",hue="smoker",style="time")
plt.show()

sns.relplot(data=tips,x="total_bill",y="tip",hue="size",palette="ch:r=-.5",alpha=.4555)
plt.show()

'''dowjones=sns.load_dataset("dowjones")
dowjones.info()
df=pd.DataFrame(dowjones)
print(df)
sns.relplot(data=dowjones,x="Date",y="Price",kind="line")
plt.show()'''

#aggregation and representing uncertainity
'''fmri=sns.load_dataset("fmri")
fmri.info()
sns.relplot(data=fmri,x="timepoint",y="signal",kind="line")           
sns.relplot(data=fmri,kind="line",x="timepoint",y="signal",errorbar=None)
plt.show()'''

import seaborn.objects as so

#seaborn objects interface
'''penguins=sns.load_dataset("penguins")
print(penguins)'''
'''so.Plot(penguins,x='bill_lenght_mm',y='bill_depth_mm').add(so.dot())
plt.show()'''

import seaborn as sns
import seaborn.objects as so

'''penguins = sns.load_dataset("penguins")'''

'''so.Plot(
penguins,
    x="bill_length_mm",
    y="bill_depth_mm"
).add(
    so.Dot()
)

so.Plot(
penguins,x="bill_length_mm",y="bill_depth_mm").add(so.Dot(color="g",pointsize=4)).show()'''
#mapping properties
'''so.Plot(penguins,x="bill_length_mm",y="bill_depth_mm",color="species",pointsize="body_mass_g").add(so.Dot()).show()

so.Plot(penguins,x="bill_length_mm",y="bill_depth_mm",edgecolor="sex",edgewidth="body_mass_g").add(so.Dot(color="blue")).show()'''

#statistical transformation
'''so.Plot(penguins,x="species",y="body_mass_g").add(so.Bar(),so.Agg()).show()'''
'''so.Plot(penguins,x="species",y="body_mass_g",color="sex").add(so.Bar(),so.Agg()).show()'''       
'''so.Plot(penguins,x="species",y="body_mass_g",color="sex",).add(so.Bar(),so.Agg(),so.Dodge(),so.Jitter(.3)).show()'''
'''so.Plot(penguins,x="flipper_length_mm").facet(col="species",row="sex").add(so.Bars(),so.Hist(),so.Line()).show()
so.Plot(
    penguins,
    x="flipper_length_mm"
).facet(
    col="species",
    row="sex"
).add(
    so.Bars(),
    so.Hist()
).show()'''


'''sns.set_theme(style="darkgrid")'''
'''tips=sns.load_dataset("tips")
print(tips)
tips.info()'''
'''g=sns.jointplot(x="total_bill",y="tip",data=tips,kind="reg",truncate=False,xlim=(0,60,),ylim=(0,12),color='r',height=7)
plt.show()'''


'''g=sns.jointplot(x="total_bill",y="tip",data=tips,kind="hist",xlim=(0,60,),ylim=(0,12),color='r',height=7)
plt.show()

g=sns.jointplot(x="total_bill",y="tip",data=tips,kind="kde",xlim=(0,60,),ylim=(0,12),color='r',height=7)
plt.show()

g=sns.jointplot(x="total_bill",y="tip",data=tips,kind="hex",xlim=(0,60,),ylim=(0,12),color='r',height=7)
plt.show()'''

'''g=sns.jointplot(x="total_bill",y="tip",data=tips,kind="resid",xlim=(0,60,),ylim=(0,12),color='r',height=7)
plt.show()'''

#sns.pairplor  'scatter', 'hist',  'kde', 'reg'


'''g = sns.pairplot(tips, kind="hist",height=7)

plt.show()'''


'''sns.pairplot(tips,hue="time",kind='kde',diag_kind="kge",palette="dark2")
plt.show()'''
'''rs=np.random.RandomState(365)
values=rs.randn(365,4).cumsum(axis=0)
dates=pd.date_range("112016",periods=365,freq="d")
data=pd.DataFrame(values,dates,columns=["A","B","C","D"])
data=data.rolling(7).mean()
sns.lineplot(data=data,palette="tab10",linewidth=2.5)
plt.show()
             
sns.lineplot(data=values,palette="tab10",linewidth=2.5)
plt.show()
             

sns.lineplot(data=rs,palette="tab10",linewidth=2.5)
plt.show()

sns.pairplot(tips,hue="time",kind='kde',diag_kind="kge",palette="dark2")
plt.show()'''


             

#calculator using def function

'''a=input("enter a number:")
b=input("enter the second number:")
choice=input("press + - * /:")

def calculator (a,opr,b):
    return eval(a+opr+b)
res=calculator(a,choice,b)
print(res)'''

penguins=sns.load_dataset("penguins")
print(penguins)

sns.lineplot(data=penguins,linewidth=8,palette="tab10")
plt.show

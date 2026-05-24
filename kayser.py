import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class data:
    def init(self):
        pass
    def loading(self):
        self.df=pd.read_csv('ss.csv')
        print("loading data done....")
        return '******************************************************************************'
    def eda(self):
        print(f'the first row are ..')
        print(self.df.head())
        print("*"*100)
        print(f'rows : {self.df.shape[0]} col : {self.df.shape[1]}')
        print(self.df.info())
        return '*'*100
    def tranform(self):
        self.df['Date']=pd.to_datetime(self.df['Date'])
        self.df['Age']=pd.to_numeric(self.df['Age'],errors='coerce')
        self.df['Total']=pd.to_numeric(self.df['Total'],errors='coerce')
        print(self.df.info())
        return '*'*100

    def cleaning(self):
        print('        data cleaning')
        print(self.df.head(15))
        print('*'*100)
        print(f'number of null : {self.df.isnull().sum()}')
        print(f'number of dup : {self.df.duplicated().sum()}')
        self.meanb=self.df[self.df['Productc']=='Beauty']['Total'].mean()
        self.df['Total']=np.where((self.df['Productc']=='Beauty')&(self.df['Total'].isna())
                                  ,self.meanb
                                  ,self.df['Total'])
        self.meana=self.df['Age'].mean()
        self.df['Age']=self.df['Age'].fillna(self.meana)
        print('*'*100)
        print(self.df.info())
        return "*"*100
    def futureEng(self):
        self.df['price_of_one']=self.df['Total'] / self.df['Quantity']
        self.df['Month']=self.df['Date'].dt.month_name()
        cond = [
        self.df["Total"] <= 100,  
        (self.df["Total"] > 100) & (self.df["Total"] <= 500),  
        self.df["Total"] > 500,]
        c = ["Low", "Medium", "High"]
        self.df["OrderType"] = np.select(cond, c, default="Unknown")
        print(self.df.head())
        return '*'*100
    def pivot(self):
        print(self.df.groupby('Productc')['Total'].sum())
        print(self.df.groupby('Month')['Total'].sum())
        p=self.df.pivot_table(values='Total'
                              ,index='Productc'
                              ,columns='Month',
                              aggfunc='sum',
                              margins='ALL')
        print(p)
        return '*'*100
    def kpis(self):
        print('              KPIs         ')
        print(f"TOTAL SALES \n {int(self.df['Total'].sum())}$")
        print(f"PRODUCT \n {len(self.df['Productc'].unique())}")
        print(f"TOTAL AMOUNT \n {self.df['Quantity'].sum()}")
        print(f"AVE AGE \n {int(self.df['Age'].mean())}")
        return '*'*100
    def vis(self):
        g=self.df['Gender'].value_counts()
        plt.pie(g,labels=g.index,autopct="%1.1f%%")
        plt.title("Gender")
        plt.xticks(rotation=45)
        plt.show()
        sns.histplot(data=self.df,x='OrderType')
        plt.xticks(rotation=45)
        plt.title("order type")
        plt.show()
        sns.barplot(data=self.df,x='Productc',y='Total')
        plt.title("product sales")
        plt.xticks(rotation=45)
        plt.show()
        sns.boxplot(data=self.df,x='Month',y='Total')
        plt.title("sales by mounth")
        plt.xticks(rotation=45)
        plt.show()
        sns.scatterplot(data=self.df,y='Total',x='Quantity',hue='Gender')
        plt.show()
    
d1=data()
print(d1.loading())
print(d1.eda())
print(d1.tranform())
print(d1.cleaning())
print(d1.futureEng())
print(d1.pivot())
print(d1.kpis())

c =input('are you ready for vis : ')
if c =="kkkkkkkhhh":
    print(6789)
else:
    print(d1.vis())
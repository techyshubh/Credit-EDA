#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Inmporting neccessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Imporing Warnings
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#importing the file data dictionary file for Ref.
Col_d = pd.read_csv("columns_description.csv",  sep=",", encoding='mac_roman')


# In[4]:


#for reference print data dictinary Col_d
Col_d


# ## Application Data Analysis

# In[5]:


#importing file dataset
Appl = pd.read_csv("application_data.csv")


# In[6]:


#cheking shape the of Dataframe
print(Appl.shape)       


# In[7]:


#Viewing the top 5 rows of our Dataframe
Appl.head()


# ## Dropping unneccesary columns

# In[8]:


#Dropping of unnecessary Columns
Appl.drop('CNT_CHILDREN', axis=1, inplace = True)
Appl.drop('REGION_POPULATION_RELATIVE', axis= 1, inplace = True)
Appl.drop('NAME_TYPE_SUITE', axis= 1, inplace = True)
Appl.drop('OWN_CAR_AGE', axis= 1, inplace = True)
Appl.drop('WEEKDAY_APPR_PROCESS_START', axis= 1, inplace = True)
Appl.drop('HOUR_APPR_PROCESS_START', axis= 1, inplace = True)
Appl.drop(Appl.loc[:,'EXT_SOURCE_1':'EMERGENCYSTATE_MODE'].columns, axis=1,inplace=True)


# In[9]:


#cheking info and data types of columns
Appl.info(verbose=True)


# ## Missing Value Percentage in Dataframe

# In[10]:


#missing values in %
Appl.isna().sum().sort_values(ascending = False).head(63)*100/len(Appl)


# ## Fixing Rows and Column, Imputing Values and Handeling Missing Values

# In[11]:


#checking if any missing value is there in column DAYS_BIRTH
Appl.DAYS_BIRTH.isnull().sum()


# In[12]:


#convetrting days in to year
Appl['Age']= abs(Appl.DAYS_BIRTH/365)//1


# In[13]:


#read the column Age
Appl.Age


# In[14]:


#bucketing Age column
Appl['Age_Group']= pd.cut(Appl.Age, [0,30,40,50,60,999], labels = ['<30','30-40','40-50','50-60','60+'])


# In[15]:


#cheking each bucket of age with their respecting percentage
Appl.Age_Group.value_counts(normalize = True)*100


# In[16]:


#checking missing values AMT_INCOME_TOTAL   
Appl.AMT_INCOME_TOTAL.isnull().sum()


# In[17]:


#reading the column AMT_INCOME_TOTAL
Appl.AMT_INCOME_TOTAL 


# In[18]:


#bucket or binned of column Appl.AMT_INCOME_TOTAL
Appl['Income_Group']= pd.cut(Appl.AMT_INCOME_TOTAL , [0,100000,200000,300000, 400000, 500000,600000], labels = ['<1L','1L-2L','2L-3L','3L-4L','5L-6L','6L+'])
Appl.Income_Group.value_counts()


# In[19]:


#read AMT_INCOME_TOTAL column
Appl.AMT_INCOME_TOTAL


# In[20]:


#converting column AMT_INCOME_TOTAL from float to int
Appl.AMT_INCOME_TOTAL.astype(int)


# In[21]:


#read the column AMT_GOODS_PRICE
Appl.AMT_GOODS_PRICE


# In[22]:


#checking missing values AMT_GOODS_PRICE 
Appl.AMT_GOODS_PRICE.isnull().sum()


# In[23]:


plt.figure(figsize=[5,3])
sns.boxplot(Appl.AMT_GOODS_PRICE)
plt.show() 
#as outlier is present in the coulmn hence we will replace missing value with median


# In[24]:


#imputing values
Appl['AMT_GOODS_PRICE'].fillna(Appl.AMT_GOODS_PRICE.median(), inplace= True)


# In[25]:


#cross check if any missing value prsent in column
Appl.AMT_GOODS_PRICE.isnull().sum()


# In[26]:


#convert it data type to int from float
Appl.AMT_GOODS_PRICE.astype(int)


# In[27]:


#read the column AMT_CREDIT  
Appl. AMT_CREDIT  


# In[28]:


#checking missing values
Appl.AMT_CREDIT.isnull().sum() #no actoin is needed


# In[29]:


#convert data type from float to int 
Appl.AMT_CREDIT.astype(int)


# In[30]:


#read column OCCUPATION_TYPE
Appl.OCCUPATION_TYPE


# In[31]:


#count the missing values
Appl.OCCUPATION_TYPE.isnull().sum()


# In[32]:


#checking missing values in %
100*96391/len(Appl.OCCUPATION_TYPE)


# In[33]:


#using mode fucntion to get most frequent value
Appl.OCCUPATION_TYPE.mode()


# In[34]:


#imputing most frequent value in OCCUPATION_TYPE
Appl.OCCUPATION_TYPE.fillna(Appl.OCCUPATION_TYPE.mode()[0], inplace = True)


# In[35]:


Appl.OCCUPATION_TYPE.isnull().sum()


# In[36]:


#read the column NAME_EDUCATION_TYPE
Appl.NAME_EDUCATION_TYPE   #no action is needed


# In[37]:


#read the column AMT_REQ_CREDIT_BUREAU_YEAR
Appl.AMT_REQ_CREDIT_BUREAU_YEAR


# In[38]:


#check if outlier present in colum AMT_REQ_CREDIT_BUREAU_YEAR
sns.boxplot(Appl.AMT_REQ_CREDIT_BUREAU_YEAR)
plt.show() 


# In[39]:


#check the missing values
Appl.AMT_REQ_CREDIT_BUREAU_YEAR.isnull().sum()


# In[40]:


#checking missing values in percentage
Appl.AMT_REQ_CREDIT_BUREAU_YEAR.isnull().sum()*100/len(Appl)


# In[41]:


#find the mean of of column and imput the mean in column
Appl.AMT_REQ_CREDIT_BUREAU_YEAR.mean()
Appl.AMT_REQ_CREDIT_BUREAU_YEAR.fillna(Appl.AMT_REQ_CREDIT_BUREAU_YEAR.mean(), inplace=True)


# In[42]:


#cross check if missing value present in column AMT_REQ_CREDIT_BUREAU_YEAR
Appl.AMT_REQ_CREDIT_BUREAU_YEAR.isna().sum()


# In[43]:


#read the AMT_REQ_CREDIT_BUREAU_QRT column
Appl.AMT_REQ_CREDIT_BUREAU_QRT


# In[44]:


#check if outlier present in column AMT_REQ_CREDIT_BUREAU_QRT
sns.boxplot(Appl.AMT_REQ_CREDIT_BUREAU_QRT)
plt.show()


# In[45]:


#check the missing values
Appl.AMT_REQ_CREDIT_BUREAU_QRT.isnull().sum()


# In[46]:


#take the mean of column and imput it in the same(AMT_REQ_CREDIT_BUREAU_QRT)
Appl.AMT_REQ_CREDIT_BUREAU_QRT.median()
Appl.AMT_REQ_CREDIT_BUREAU_QRT.fillna(Appl.AMT_REQ_CREDIT_BUREAU_QRT.median(), inplace= True)


# In[47]:


#cross check if any missing value present in column AMT_REQ_CREDIT_BUREAU_QRT
Appl.AMT_REQ_CREDIT_BUREAU_QRT.isnull().sum()


# In[48]:


#read the column REQ_CREDIT_BUREAU_MON
Appl.AMT_REQ_CREDIT_BUREAU_MON


# In[49]:


#check the missing values in column
Appl.AMT_REQ_CREDIT_BUREAU_MON.isnull().sum()


# In[50]:


#cehck if outlier is present
sns.boxplot(Appl.AMT_REQ_CREDIT_BUREAU_MON)
plt.show()


# In[51]:


#take the mean and inpute it in the same column (Appl.AMT_REQ_CREDIT_BUREAU_MON)
Appl.AMT_REQ_CREDIT_BUREAU_MON.mean()
Appl.AMT_REQ_CREDIT_BUREAU_MON.fillna(Appl.AMT_REQ_CREDIT_BUREAU_MON.mean(), inplace= True)


# In[52]:


#chek if any missing value present in column AMT_REQ_CREDIT_BUREAU_MON
Appl.AMT_REQ_CREDIT_BUREAU_MON.isnull().sum()


# In[53]:


# Replace the XNA value with F for CODE_GENDER Column
Appl.loc[Appl.CODE_GENDER == 'XNA','CODE_GENDER'] = 'F'
Appl.CODE_GENDER.value_counts()


# In[54]:


#create gender_flag of numerical data type where response "yes"= 1, "no"= 0
Appl['gender_flag'] = np.where(Appl.CODE_GENDER == 'M',1,0)


# In[55]:


#cheking percentage of Target variable
Appl.TARGET.value_counts(normalize= True)*100 # it is balance


# In[56]:


#cheking percentage of CODE_GENDER variable
Appl.CODE_GENDER.value_counts(normalize= True)*100


# ### ↑ No Balancing is Required ↑

# ### <font color = navy> Splitting Dataframe
# 1. Appl_0 (Non_defaulter)
# 2. Appl_1 (defaulter)

# In[57]:


#read the dataframe for non-defulter
Appl_0 = Appl[Appl.TARGET== 0]
Appl_0


# In[58]:


#read the dataframe for defalulter
Appl_1 = Appl[Appl.TARGET== 1]
Appl_1


# ### <font color= navy> Univariate Analysis
# -  Appl_0
# -  Appl_1

# <font color = 'brown'> **↓↓ Bar graph for column  variable Name Contract for Appl_0 ↓↓**

# In[59]:


#plot the bar graph Name Contract for Appl_0
fig, ax = plt.subplots(ncols=2, nrows=1, sharex=True, sharey=True)
plt.subplot(1,2,1)
Appl_0.NAME_CONTRACT_TYPE.value_counts().plot.bar()
plt.title('Name Contract for Appl_0\n', fontdict={'fontsize':13, 'fontweight': 4 })
plt.xlabel('Loans', fontdict={'fontsize':13, 'fontweight':5})
plt.ylabel('Amount', fontdict={'fontsize':13, 'fontweight':5})

plt.subplot(1,2,2)
Appl_1.NAME_CONTRACT_TYPE.value_counts().plot.bar()
plt.title('Name Contract for Appl_1\n', fontdict={'fontsize':13, 'fontweight': 4 })
plt.xlabel('Loans', fontdict={'fontsize':13, 'fontweight':5})
plt.ylabel('Amount', fontdict={'fontsize':13, 'fontweight':5})
plt.show()


# <font color = 'navy'> **Obsevations**
# -  For Non-Defaulter the loan Amount big is very as compare to defaulter and this should be the case as Non-Defaulter will    pay the but Defaulter won't hence our observation are correct 

# In[60]:


#draw pie-plot for column variable CODE_GENDER
plt.figure(figsize=[10,10])
plt.subplot(1,2,1)
plt.title('Non-Defaulter')
Appl_0.CODE_GENDER.value_counts().plot.pie()
plt.subplot(1,2,2)
Appl_1.CODE_GENDER.value_counts().plot.pie()
plt.title('Defaulter')
plt.show()


# <font color = 'navy'> **Obsevations**
# -  As we can clearly see in above plot in Non-Defaulter case Females are more and as compare to Defaulter 
# -  By above plot males are more in Defaulter case as compare to Non-Defaulter

# <font color = 'brown'> **↓↓ Simple-Plot and Boxplot for column varibale AMT_INCOME_TOTAL↓↓**

# In[61]:


#draw the plot for column varibale AMT_INCOME_TOTAL
plt.figure(figsize=[15,5])
plt.subplot(2,2,1)
plt.title('Non-Defaulter')
Appl_0.AMT_INCOME_TOTAL.plot()
plt.xlabel('People', fontdict={'fontsize':13, 'fontweight':5})
plt.ylabel('Amount', fontdict={'fontsize':13, 'fontweight':5})

plt.subplot(2,2,2)
plt.title('Defaulter')
Appl_1.AMT_INCOME_TOTAL.plot()
plt.xlabel('People', fontdict={'fontsize':13, 'fontweight':5})
plt.ylabel('Amount', fontdict={'fontsize':13, 'fontweight':5})

plt.subplot(2,2,3)
sns.boxplot(Appl_0.AMT_INCOME_TOTAL)

plt.subplot(2,2,4)
sns.boxplot(Appl_1.AMT_INCOME_TOTAL)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()


# <font color = 'navy'> **Obsevations**
# -  In case of Non-Defaulter most of people their Income is realistic Countineous And some of income is High
# -  In case of Defaulter case Defaulter people income is low and not realistic and outlier is present hence it is
#    considered as Defaulters

# ### <font color= navy> Bivariate Analysis
# -  Appl_0
# -  Appl_1

# <font color = 'brown'> **↓↓ Scatter plot for Age and  AMT_INCOME_TOTAL Column Varibale ↓↓**

# In[64]:


plt.figure(figsize=[18,4])
plt.subplot(1,2,1)
plt.title('Non-Defaulter')
plt.scatter(Appl_0.Age,Appl_0.AMT_INCOME_TOTAL )
plt.xlabel('Age', fontdict={'fontsize':13, 'fontweight':5})
plt.ylabel('Income', fontdict={'fontsize':13, 'fontweight':5})


plt.subplot(1,2,2)
plt.title('Defaulter')
plt.scatter(Appl_1.Age,Appl_1.AMT_INCOME_TOTAL )
plt.xlabel('Age', fontdict={'fontsize':13, 'fontweight':5})
plt.ylabel('Income', fontdict={'fontsize':13, 'fontweight':5})
plt.show()


# <font color = 'navy'> **Obsevations**
# - In case of Non-Defalulter income with respect to age is pretty much continueos 
# - for Defaulter it is not contineous and there is huge gap too (outlier)
# - Hence we can conlude people with low income and high income can be Defaulters
#   

# <font color = 'brown'> **↓↓ Boxplot for NAME_EDUCATION_TYPE and  AMT_CREDIT Column Varibale ↓↓**

# In[65]:


plt.figure(figsize=[15,8])
plt.subplot(2,1,1)
plt.title('Non-Defaulter')
sns.boxplot(data= Appl_0,x='NAME_EDUCATION_TYPE',y='AMT_CREDIT')

plt.subplot(2,1,2)
plt.title('Defaulter')
sns.boxplot(data= Appl_1,x='NAME_EDUCATION_TYPE',y='AMT_CREDIT')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()


# <font color = 'navy'> **Obsevations**
#    
# - For Non-Defaulter the AMT_CREDIT is continious with respect to Education gradually increasing no significant change         is observed
# - For Defaulter only in Secondary/Secondary special is exception and has outlier means people who has secondary
#   /secondary special education tend to have payment in difficulties and asked for more AMT_CREDIT As compare to rest

# <font color = 'brown'> **↓↓ Barplot for NAME_EDUCATION_TYPE and  AMT_GOODS_PRICE Column Varibale ↓↓**

# In[66]:


plt.figure(figsize=[10,4])
plt.subplot(1,2,1)
plt.title('Non-Defaulter\n')
Appl_0.groupby('NAME_EDUCATION_TYPE')['AMT_GOODS_PRICE'].mean().plot.bar()
plt.subplot(1,2,2)
plt.title('Defaulter\n')
Appl_1.groupby('NAME_EDUCATION_TYPE')['AMT_GOODS_PRICE'].mean().plot.bar()
plt.show()


# <font color = 'navy'> **Obsevations**
#    - In case of Non-Defaulter Academic degree and secondary special are more likely to pay the loan As compare to rest
#    - The people with high income groups are mostly non defaulters
#    - The people who are  highly qualified are mostly non defaulters as compared to the one who are simply graduates or          secondary school passed 

# ### <font color= navy> Multivariate Analysis
# -  Appl_0 (Non-Defaulter)

# In[67]:


# Analysis of NAME_EDUCATION_TYPE vs Age_Group vs gender_flag
corr1 = pd.pivot_table(Appl_0, index= 'NAME_EDUCATION_TYPE', columns ='Age_Group', values= 'gender_flag' )
plt.figure(figsize=[10, 8])
sns.heatmap(corr1, annot=True, )
plt.show()


# <font color = 'navy'> **Observations**
#    - Here we can observe that  people who are highly educated are likely to be non- defaulters as compared to the ones who      are with lower educational qualification.
#    - The lower educated people are likely to be more defaulters

# -  Appl_1 (Defaulter)

# In[68]:


# Analysis of NAME_EDUCATION_TYPE vs Age_Group vs gender_flag
corr2 = pd.pivot_table(Appl_1, index= 'NAME_EDUCATION_TYPE', columns ='Age_Group', values= 'gender_flag' )
plt.figure(figsize=[10, 8])
sns.heatmap(corr2, annot=True)
plt.show()


# <font color = 'navy'> **Obsevations**
#   - Here we can see that people with highly paid salary are less likely to defaulter in comparison with the people getting       less or average salary.

# ## <font color= Green> Previous Application Data Analysis

# In[69]:


#importh the dataset 
Pre_a = pd.read_csv('previous_application.csv')


# In[70]:


#cheking shape the of Dataframe
print(Pre_a.shape)      #Pre_a had 1670214 rows and 37 columns


# In[71]:


#print the head of Pre_a
Pre_a.head()


# In[72]:


# print the tail of Pre_a
Pre_a.tail()


# #### Dropping unneccesary columns

# In[74]:


#Dropping uneccessary columns
Pre_a.drop('WEEKDAY_APPR_PROCESS_START', axis= 1, inplace=True)
Pre_a.drop('AMT_DOWN_PAYMENT', axis= 1, inplace=True)
Pre_a.drop('RATE_DOWN_PAYMENT', axis= 1, inplace=True)
Pre_a.drop('HOUR_APPR_PROCESS_START', axis= 1, inplace=True)
Pre_a.drop(Pre_a.loc[:,'RATE_INTEREST_PRIMARY':'RATE_INTEREST_PRIVILEGED'].columns,axis= 1, inplace=True)
Pre_a.drop('NAME_CASH_LOAN_PURPOSE', axis= 1, inplace=True)
Pre_a.drop(Pre_a.loc[:,'DAYS_FIRST_DRAWING':'DAYS_LAST_DUE'].columns, axis= 1, inplace=True)
Pre_a.drop('SELLERPLACE_AREA', axis= 1, inplace=True)


# In[75]:


#cheking info and data types of columns
Pre_a.info(verbose=True)


# In[76]:


#cheking info and data types of columns
Pre_a.info(verbose=True)


# ###  <font color= brown> **Missing Value Percentage in Dataframe**

# In[77]:


#missing values in %
Pre_a.isna().sum().sort_values(ascending = False).head(60)*100/len(Pre_a)


# ### <font color = Brown>  Fixing Rows and Column, Imputing Values and Handeling Missing Values

# **NFLAG_INSURED_ON_APPROVAL Column**

# In[78]:


#find the missing value in column NFLAG_INSURED_ON_APPROVAL 
Pre_a.NFLAG_INSURED_ON_APPROVAL.isna().sum()*100/(len(Pre_a))


# In[79]:


# imputing median in column NFLAG_INSURED_ON_APPROVAL
Pre_a.NFLAG_INSURED_ON_APPROVAL.fillna(Pre_a.NFLAG_INSURED_ON_APPROVAL.mode(), inplace = True)


# In[80]:


#cross check if mrdian is present in NFLAG_INSURED_ON_APPROVAL
Pre_a.NFLAG_INSURED_ON_APPROVAL.mode().isnull().sum()


# **Pre_a.AMT_GOODS_PRICE**

# In[81]:


#checking missing value for AMT_GOODS_PRICE column
Pre_a.AMT_GOODS_PRICE.isnull().sum()


# In[82]:


#plot the boxplot for AMT_GOODS_PRICE
sns.boxplot(Pre_a.AMT_GOODS_PRICE)
plt.show()


# In[83]:


#as the value amount is contineous we will use mean for imputing
Pre_a.AMT_GOODS_PRICE.fillna(Pre_a.AMT_GOODS_PRICE.mean(), inplace= True)


# In[84]:


#cross check missing value is present in AMT_GOODS_PRICE column
Pre_a.AMT_GOODS_PRICE.isna().sum()


# **AMT_ANNUITY column**

# In[86]:


#plot the box plot for AMT_ANNUITY column
sns.boxplot(Pre_a.AMT_ANNUITY  )
plt.show()


# In[87]:


#imputing value with  maen because value is contineous in boxplot
Pre_a.AMT_ANNUITY.fillna(Pre_a.AMT_ANNUITY.mean(), inplace=True)
Pre_a.AMT_ANNUITY


# In[88]:


#cross check if any missing value present
Pre_a.AMT_ANNUITY.isnull().sum()


# **CODE_REJECT_REASON Column**

# In[90]:


#Handling the values of XNA in column CODE_REJECT_REASON
Pre_a.loc[Pre_a.CODE_REJECT_REASON == 'XNA','CODE_REJECT_REASON'] = Pre_a.CODE_REJECT_REASON.mode()[0]
Pre_a.CODE_REJECT_REASON.value_counts()


# **NAME_CONTRACT_TYPE Column**

# In[91]:


#repalcing value with most common value 'Cash loans' in column NAME_CONTRACT_TYPE
Pre_a.loc[Pre_a.NAME_CONTRACT_TYPE== 'XNA','NAME_CONTRACT_TYPE'] = 'Cash loans'
Pre_a.NAME_CONTRACT_TYPE.value_counts()


# ### <font color = brown > Checking Imbalance

# In[92]:


#cheking percentage of NFLAG_INSURED_ON_APPROVAL variable
Pre_a.NFLAG_INSURED_ON_APPROVAL.value_counts(normalize= True)*100


# #### ↑ No Balancing is Required ↑

# In[93]:


Pre_a.NAME_CONTRACT_STATUS.value_counts()


# ### <font color = Brown> Univariate Analysis

# <font color = 'navy'> **↓↓ Plot the bar graph for NAME_CONTRACT_STATUS ↓↓**

# In[94]:


#plot the bar plot for column NAME_CONTRACT_STATUS
Pre_a.NAME_CONTRACT_STATUS.value_counts().plot.bar()
plt.title('Loan Status\n', fontdict={'fontsize':13, 'fontweight': 4 })
plt.xlabel('Loans', fontdict={'fontsize':13, 'fontweight':5})
plt.show()


# <font color = 'green'> **Obsevations**
#   - In previous Application it seems that most of client has got Approvel for the loan
#   - Approved > Canceled > Refused > Unused offer

# <font color = 'navy'> **↓↓ Plot the pie chart  for NFLAG_INSURED_ON_APPROVAL ↓↓**

# In[97]:


Pre_a.NFLAG_INSURED_ON_APPROVAL.value_counts().plot.pie()
plt.show()


# <font color = 'green'> **Obsevations**
#   - From Above plot is seems that during Application most clients were asking for insurance

# <font color = 'navy'> **↓↓ Plot the distplot  for AMT_CREDIT ↓↓**

# In[98]:


plt.style.use('dark_background')
plt.figure(figsize=[10,5])
sns.distplot(Pre_a.AMT_CREDIT, bins =20)
plt.title('Distribution of Credit Amt', fontsize = 12)
plt.show


# <font color = 'green'> **Obsevations**
#   - From Above plot is seems that the In pre. application people are more likely to ask for Amount In between 10k - 150k

# ### <font color = Brown> Bivariate and Multivariate Analysis

# In[99]:


#To reset all the settings we have set
plt.style.use('default')
get_ipython().run_line_magic('matplotlib', 'inline')


# <font color = 'navy'> **↓↓ Plot the scatter plot  for NAME_CONTRACT_STATUS and AMT_CREDIT ↓↓**

# In[100]:


#plot the scatter plot
plt.scatter(Pre_a.NAME_CONTRACT_STATUS, Pre_a.AMT_CREDIT )
plt.show()


# <font color = 'green'> **Observations**
#   - In Prev. Application the freq. of status Approved, Refused, Canceled same except Unused offer

# In[101]:


#plot the bar graph of AMT_GOODS_PRICE'S mean an median with NAME_CONTRACT_STATUS.
Pre_a.groupby('NAME_CONTRACT_STATUS')['AMT_GOODS_PRICE'].aggregate(['mean', 'median']).plot.bar()
plt.show()


# <font color = 'green'> **Observations** 
#   - In case of Approved mean is greater than median (Goods Price)
#   - Significantly In case of refused mean is bit high compare to median 
#   - It shows that most of client Application getting rejected and refused 

# <font color = 'navy'> **↓↓ Plot the pairplot for AMT_CREDIT, AMT_GOODS_PRICE,AMT_APPLICATION ↓↓**

# In[102]:


#plot the pairplot for AMT_CREDIT,AMT_GOODS_PRICE and AMT_APPLICATION
plt.figure(figsize=[12,12])
sns.pairplot(data= Pre_a, vars=['AMT_CREDIT', 'AMT_GOODS_PRICE','AMT_APPLICATION'] )
plt.show()


# <font color = 'green'> **Observations**
# 
#  1 - Amount of goods price and Amount of credit is correalated and it also cause causetion <br>
#  2 - Amount of Credit And Amount of Application are correlated <br>
#  3 - Amount of goods price and amount of application has linear relation between them (Causetion)

# <font color = 'navy'> **↓↓ Plot the heatmap for AMT_CREDIT,AMT_GOODS_PRICE and AMT_APPLICATION ↓↓**

# In[103]:


#plot the heatmap forfor AMT_CREDIT,AMT_GOODS_PRICE and AMT_APPLICATION
sns.heatmap(Pre_a[['AMT_CREDIT', 'AMT_GOODS_PRICE','AMT_APPLICATION']].corr(),annot= True, cmap='Greens')
plt.show()


# <font color = 'green'> **Observations**
# 
#  1 - Amount of goods price and Amount of credit is correalated and it also cause causetion <br>
#  2 - Amount of Credit And Amount of Application are correlated <br>
#  3 - Amount of goods price and amount of application has linear relation between them (Causetion)

# <font color = 'navy'> **↓↓ Plot the heatmap for NAME_CONTRACT_TYPE,NAME_CONTRACT_STATUS and AMT_CREDIT ↓↓**

# In[104]:


#Plot the heatmap NAME_CONTRACT_TYPE vs NAME_CONTRACT_STATUS vs AMT_CREDIT
Htmp = pd.pivot_table(Pre_a, index='NAME_CONTRACT_TYPE', columns='NAME_CONTRACT_STATUS', values='AMT_CREDIT')


# In[105]:


# print the pivot table ofNAME_CONTRACT_TYPE vs NAME_CONTRACT_STATUS vs AMT_CREDIT
Htmp


# In[106]:


#print the heat mapNAME_CONTRACT_TYPE vs NAME_CONTRACT_STATUS vs AMT_CREDIT
plt.figure(figsize=[8, 6])
sns.heatmap(Htmp, annot = True,cmap="Reds")
plt.show()


# <font color = 'green'> **Observations**
#  -  

# - Here it can be seen that a major portion of the loan amount has been refused by the bank. A portion of the major amount     was approved and was provided to the people.                                                      
# - For consumer loans the amount is not as huge as compared to cash loans. For revolving loans and unused loan offers,   
#   amount is considerably low with respect to the cash loans. 
# - A huge amount of loan has been refused by the users i.e. who have good previous records or cibil scores but are not   
#   looking for loan seeking opportunities.

# In[ ]:





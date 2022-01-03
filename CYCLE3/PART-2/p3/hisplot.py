import seaborn as sns
import pandas
import matplotlib.pyplot as plt
sns.get_dataset_names()
df = sns.load_dataset('iris')
df.head()
sns.histplot(x = 'sepal_length',kde=True,bins = 6 , data =df)

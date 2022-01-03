import seaborn as sns
import pandas
Import matplotlib.pyplot as plt
sns.get_dataset_names()
df = sns.load_dataset('iris')
df.head()
sns.displot(x = 'sepal_length',kde=True,bins = 5 , data =df)






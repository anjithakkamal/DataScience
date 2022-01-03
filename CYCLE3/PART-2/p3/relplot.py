import seaborn as sns
sns.set(style ="ticks")
dataset = sns.load_dataset('iris')
col=['sepal_length','sepal_width','petal_length','petal_width','type']
sns.relplot(x ="sepal_length", y ="petal_width", data = dataset)

import numpy as np
import pandas as pd
import seaborn as sns 

import matplotlib.pyplot as plt
%matplotlib inline 


iris = sns.load_dataset('iris')
my_data_frame = pd.DataFrame(iris)


g = sns.pairplot(my_data_frame)
g = sns.pairplot(iris, kind="reg", hue="species")
g = sns.pairplot(iris, kind="hist", hue="species")
g = sns.pairplot(iris, kind="kde", hue="species")
g = sns.pairplot(iris, kind="scatter", hue="species")


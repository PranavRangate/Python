import pandas as pd
import numpy as np

data=pd.read_csv('data.csv')

x = data.iloc[:,:-1]
y = data.iloc[:,-1].values.reshape(-1,1)

from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values = np.nan , strategy = 'mean')

y_imputed=imp.fit_transform(y)

y_imputed_df = pd.DataFrame(y_imputed,columns=[data.columns[-1]])

imputed_data = pd.concat([x,y_imputed_df],axis=1)

print(data)
print(imputed_data)
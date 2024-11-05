import pandas as pd
import numpy as np # Imported numpy so that we can represent missing values as  np.nan and handle/ignore them using 'skipna=True'

# Create a DataFrame

Mark_list={#'Name':['Anu', 'Anjali', 'Sameer', 'Malavika', 'Neelima'],
      #'Student_ID':[1201, 1202, 1203, 1204, 1205],
      'Malayalam':[47, 35, 34, 48, 45],
      'English':[48, 48, 46, 50, 30],
      'Science':[46, 45, 41, 43, 47],
      'Mathematics':[48,47,44,49,43],
      'Arabic':[np.nan, np.nan, 49, 45, np.nan], #
      #'F/P':['P','P','P','P','P']
      }
df= pd.DataFrame(Mark_list)
print(df)

Avg_of_Each_Column= df.mean(axis=0,skipna=True) # axis=0: Calculates the mean of each column.
print(Avg_of_Each_Column)

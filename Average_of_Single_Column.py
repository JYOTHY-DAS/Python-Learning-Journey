import pandas as pd

# Create a DataFrame

Mark_list={'Name':['Anu', 'Anjali', 'Sameer', 'Malavika', 'Neelima'],
      'Student_ID':[1201, 1202, 1203, 1204, 1205],
      'Malayalam':[47, 34, 35, 48, 45],
      'English':[48, 48, 46, 50, 30],
      'Science':[46, 45, 41, 43, 47],
      'Mathematics':[48,47,44,49,43],
      'Arabic':['NaN', 'NaN', 49, 45, 'NaN'], 
      'F/P':['P','P','P','P','P']}
df= pd.DataFrame(Mark_list)
print(df)

# Mean value of the column 'malayalam'
Avg_Mark_of_Malayalam= df['Malayalam'].mean()
print(Avg_Mark_of_Malayalam)

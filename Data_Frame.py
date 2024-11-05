import pandas as pd

# Create a DataFrame

table={'Name':['Anu', 'Anjali', 'Meera', 'Malavika', 'Neelima'],
      'Student_ID':[1201, 1202, 1203, 1204, 1205],
      'Malayalam':[47, 34, 35, 48, 45],
      'English':[48, 48, 46, 50, 30],
      'Science':[46, 45, 41, 43, 47], 
      'F/P':['P','P','P','P','P']}

print(pd.DataFrame(table))

import pandas as pd
edu = pd.read_csv('educ_figdp_1_Data.csv', na_values=':', usecols=['TIME', 'GEO', 'Value'])
print(edu)
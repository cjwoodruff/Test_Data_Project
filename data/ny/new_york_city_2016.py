'''The new_yor_city.py script will take data dowloaded from
www1.nyc.gov regading crime data for the city of New York, NY.
The XLS File contains all crimes. This script will parse out
the violent crimes only. The idea is to combine all four files
together as one and then parse out the data before getting a full
sum of crimes committed for 2016.

NOTE: This may change for ease of use in the future to make a
dictionary that uses the year as the key and sum of violent
crimes as the value.'''

from pandas import DataFrame, read_csv
import pandas as pd

# Load the first file and send it to the Data Frame.
# Perform the necessary drops to get rid of extra data
# that won't be needed. Finally, Transpose the Data
# Frame and view it.
file = r'seven-major-felony-offenses-2000-2016.xls'
df = pd.ExcelFile(file)
df = df.parse('Seven Major Felony Offenses')

df.dropna(axis=0, how='any', inplace=True)
df.drop(['ROBBERY',
         'BURGLARY',
         'GRAND LARCENY',
         'GRAND LARCENY OF MOTOR VEHICLE'],
        axis=0, inplace=True)
df = df.T

#print(df)
#print(df.info())

# Load the second file and send it to the Data Frame.
# Perform the necessary drops to get rid of extra data
# that won't be needed. Finally, Transpose the Data
# Frame and view it.
file = r'non-seven-major-felony-offenses-2000-2016.xls'
df1 = pd.ExcelFile(file)
df1 = df1.parse('Non-Seven Major Felony Offenses')

df1.dropna(axis=0, how='any', inplace=True)
df1.drop(['FELONY POSSESSION OF STOLEN PROPERTY',
          'FORGERY/THEFT_FRAUD/IDENTITY THEFT',
          'ARSON',
          'FELONY DANGEROUS DRUGS (1)',
          'FELONY DANGEROUS WEAPONS (2)',
          'FEL. CRIMINAL MISCHIEF & RELATED OFFENSES',
          'OTHER FELONIES (4)'],
         axis=0, inplace=True)
df1 = df1.T

#print(df1)
#print(df1.info())

# Load the third file and send it to the Data Frame.
# Perform the necessary drops to get rid of extra data
# that won't be needed. Finally, Transpose the Data
# Frame and view it.
file = r'misdemeanor-offenses-2000-2016.xls'
df2 = pd.ExcelFile(file)
df2 = df2.parse('Misdemeanor Offenses')

df2.dropna(axis=0, how='any', inplace=True)
df2.drop(['MISDEMEANOR POSSESSION OF STOLEN PROPERTY',
          'MISDEMEANOR DANGEROUS DRUGS (1)',
          'MISDEMEANOR DANGEROUS WEAPONS (5)',
          'PETIT LARCENY',
          'INTOXICATED & IMPAIRED DRIVING',
          'VEHICLE AND TRAFFIC LAWS',
          'MISD. CRIMINAL MISCHIEF & RELATED OFFENSES',
          'CRIMINAL TRESPASS',
          'UNAUTHORIZED USE OF A VEHICLE',
          'OFFENSES AGAINST THE PERSON (7)',
          'OFFENSES AGAINST PUBLIC ADMINISTRATION (2)',
          'ADMINISTRATIVE CODE (6) ',                   # Notice the space at the end of this one
          'FRAUDS (3)',
          'AGGRAVATED HARASSMENT 2',
          'OTHER MISDEMEANORS (8)'],
         axis=0, inplace=True)
df2 = df2.T

#print(df2)
#print(df2.info())

# Join all of the Data Frames together and add another
# column called 'Violent_Crimes' that takes the total
# of all other columns. Then print it and ouput it as
# a CSV file.
joined_table = df.join(df1).join(df2)
joined_table['Violent_Crimes'] = joined_table[list(joined_table.columns)].sum(axis=1)

print(joined_table)
print(joined_table.info())

joined_table.to_csv('new_york_city.csv')

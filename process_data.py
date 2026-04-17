import pandas as pd
import glob

files = glob.glob('data/*.csv')
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df = df[df['product'] == 'pink morsel']


df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

df['sales'] = df['quantity'] * df['price']

final_df = df[['sales', 'date', 'region']]

final_df.to_csv('formatted_output.csv', index=False)
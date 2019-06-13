import pandas as pd
from datetime import datetime

output_data = pd.read_csv("output.csv")
correct_data = pd.read_csv("Final_Data.csv")
print(output_data.index)

for i in output_data.index:
	d = output_data.loc[i, 'Date']
	if d == 'empty' or 'ET' in d:
		temp_df = correct_data[correct_data['Ticker'] == output_data.loc[i, 'Ticker']]
		temp_df = temp_df[temp_df['Year'] == output_data.loc[i, 'Year']]
		temp_df = temp_df[temp_df['Quarter'] == output_data.loc[i, 'Quarter']]
		if len(temp_df) != 1:
			print(output_data.loc[i, 'Ticker'])
			print(output_data.loc[i, 'Quarter'])
			print(output_data.loc[i, 'Year'])
			raise Exception(temp_df)	
		else:
			output_data.loc[i, 'Date'] = datetime.strptime(temp_df['Date'].iloc[0], '%m/%d/%Y %I:%M').strftime('%b %d, %Y %I:%M %p')
			# print(temp_df['Date'].iloc[0])
output_data.write_csv("output.csv")
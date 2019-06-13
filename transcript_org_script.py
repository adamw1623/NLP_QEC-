### Fill out the transcipt org with number of transcripts and dates we have ###

import pandas as pd 
import os

transcript_org_path = "C:/Users/Adam/Documents/Trading/Purple Power/Initial_Runs/transcript_organization.xlsx"
transcript_path = "C:/Users/Adam/Documents/Trading/Purple Power/Initial_Runs/Already Run/"

org_df = pd.read_excel(transcript_org_path)
org_df.fillna(value=0, inplace=True)

print(org_df.columns)


arr = [[]]
for filename in os.listdir(transcript_path):
    if 'txt' in filename:
        split = filename.split('_')
        split[2] = split[2].split('.')[0]
        files = arr.append(split)
# print(arr)
files = pd.DataFrame(data=arr, columns=['ticker', 'year', 'quarter'])
files = files.drop(0)


counts = files.groupby('ticker').count()

for ticker, count in counts.iterrows():
	org_df.loc[org_df.Ticker == ticker, 'Number of Transcripts'] = count[0]

	temp_df = files[files.ticker == ticker]
	min_year = 20
	min_q = 5
	min_index = ''

	for index, row in temp_df.iterrows():
		if int(row['year']) < min_year and int(row['quarter'][1]) < min_q:
			min_year = int(row['year'])
			min_q = int(row['quarter'][1])
			min_index = index
	org_df.loc[org_df.Ticker == ticker, 'Start Quarter'] = 'Q' + str(min_q) + '_' + str(min_year)

	max_year = 0
	max_q = 0
	max_index = ''

	for index, row in temp_df.iterrows():
		if int(row['year']) > max_year:
			max_year = int(row['year'])
			max_q = int(row['quarter'][1])
			max_index = index
		elif int(row['year']) == max_year and int(row['quarter'][1]) > max_q:
			max_year = int(row['year'])
			max_q = int(row['quarter'][1])
			max_index = index
	org_df.loc[org_df.Ticker == ticker, 'End Quarter'] = 'Q' + str(max_q) + '_' + str(max_year)
	org_df.loc[org_df.Ticker == ticker, 'Run?'] = 1


print(org_df)
org_df.to_excel(transcript_org_path)

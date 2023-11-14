import requests
import json
import io
import csv
import pandas as pd


response= requests.get("https://rakshakrita0.vercel.app/api/authority/feedback")
jsondata = response.json()
data = json.loads(json.dumps(jsondata.get('feedbacks')))

csv_file_in_memory = io.StringIO()

csv_writer = csv.writer(csv_file_in_memory)

header = data[0].keys()
csv_writer.writerow(header)

for row in data:
    csv_writer.writerow(row.values())

csv_file_in_memory.seek(0)

df = pd.read_csv(csv_file_in_memory)

df.drop(columns=['_id', 'description', '__v', 'id'], inplace=True)

df['createdAt'] = pd.to_datetime(df['createdAt'])
df.loc[:, 'createdAt'] = df.loc[:, 'createdAt'].dt.date
df['createdAt'] = pd.to_datetime(df['createdAt'])

print(df.info())

import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import networkx as nx
from faker import Faker
from datetime import timedelta
import random

def plot_to_base64(plot):
    buffer = io.BytesIO()
    plot.savefig(buffer, format='png')
    buffer.seek(0)
    plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return f"data:image/png;base64,{plot_base64}"

fake = Faker()

station_ids = [
    '6536be3227c19dbd146b1d61',
    '6539279ee0265e4af914b84f',
    '6539279ee0265e4af914b84a',
    '6539279ee0265e4af914b84b',
    '6539279ee0265e4af914b851',
    '6539279ee0265e4af914b856',
    '6539279ee0265e4af914b846',
    '6539279ee0265e4af914b848',
    '6539279ee0265e4af914b849'
]

records = []

for station_id in station_ids:
    for _ in range(1000):
        record = {
            'stationId': station_id,
            'createdAt': (fake.date_this_decade() + timedelta(days=random.randint(0, 9))).strftime('%Y-%m-%d'),
            'type': random.choice(['miscellaneous', 'Negative Feedback', 'Neutral Feedback', 'Positive Feedback']),
            'issue': random.choice(['Unprofessional Conduct', 'Response Time', 'misconduct', 'Use of Firearms', 'Inefficiency', 'Negligence', 'Misconduct'])
        }
        records.append(record)

df = pd.DataFrame(records)

df = df.sample(frac=1).reset_index(drop=True)

for i, row in df.iterrows():
    if row['type'] != 'Negative Feedback':
        row['issue'] = None

# Plot countplot
sns.countplot(x='issue', data=df)
plt.title('Distribution of Issues')
plt.xticks(rotation=45)
count_plot_base64 = plot_to_base64(plt)

# Plot line plot
df['createdAt'] = pd.to_datetime(df['createdAt'])
monthly_counts = df.groupby(df['createdAt'].dt.to_period("M")).size()
plt.title('Monthly Entries')
plt.xlabel('Month')
plt.ylabel('Count')
line_plot_base64 = plot_to_base64(plt)

# Plot pie chart
df['issue'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Proportion of Issues')
pie_chart_base64 = plot_to_base64(plt)

from sklearn.preprocessing import LabelEncoder

df_encoded = df.copy()
label_encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == 'object':
        df_encoded[column] = label_encoder.fit_transform(df[column])

# Plot heatmap
sns.heatmap(df_encoded.corr(), annot=True, cmap='viridis')
plt.title('Correlation Heatmap')
heatmap_base64 = plot_to_base64(plt)

# Plot complex heatmap
sns.heatmap(pd.crosstab(df['type'], df['issue'], normalize='index'), cmap='plasma', annot=True)
plt.title('Heatmap of Type vs. Issue')
complex_heatmap_base64 = plot_to_base64(plt)

# Plot network graph
temp_df = df.dropna(subset=['issue'])
G = nx.from_pandas_edgelist(temp_df, 'type', 'issue')
nx.draw(G, with_labels=True)
plt.title('Network Plot of Type-Issue Relationships')
network_plot_base64 = plot_to_base64(plt)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Police Station Performance Report</title>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit&display=swap');
        
        * {
            margin: 0;
            /* outline: solid black; */
        }
        
        body {
            font-family: 'Outfit', sans-serif;
            text-align: center;
            /*background: linear-gradient(120deg,#ffb78b,#ff6000 100%) no-repeat;*/
            background-color: aliceblue;
            color: #42445D;
        }

        .details {
            text-align: start;
            width: fit-content;
            margin-inline: auto;
        }

        h1 {
            font-size: 2.6rem;
            padding-top: 1rem;
            margin-bottom: 2rem;
        }
        h2 {
            font-size: 2rem;
            margin-top: 2rem;
        }
        h3 {
            font-size: 1.5rem;
            margin-top: 2rem;
        }
        p {
            font-size: 1.2rem;
        }

        .wrapper {
            margin-inline: auto;
            width: 50vw;
            min-width: 300px;
            padding-bottom: 10vh;
            /* background-color: rgba(255,255,255,0.6);
            box-shadow: 0 0 10px black; */
        }
        
        
        .graphContainer:nth-child(even) {
            text-align: end;
        }
        .graphContainer:nth-child(odd) {
            text-align: start;
            padding: 0 0;
        }
        img{
             mix-blend-mode: multiply; 
            border-radius: 5px;
            max-width: 100%;
            /*box-shadow: 0 0 10px black;*/
            margin-top: 1rem;
        }
    </style>
</head>

<body>
    <div class="wrapper">

        <h1>Police Station Performance Report</h1>

        <div class="details">
            <p><strong>Description:</strong> This report provides an analysis of the performance of police stations.</p>
            <p><strong>Creator:</strong> RakshakRita</p>
            <p><strong>Time Frame:</strong> 2022-2023</p>
        </div>
        
        <h2>Summary</h2>
        <p>The performance of police stations has been consistent throughout the month.</p>
    
        <h2>Plots</h2>
        <div class="graphWrapper">
            <div class="graphContainer">
                <h3>Issue Bar Graph</h3>
                <p>Bar Graph showing the count of various issues</p>
                <img src="CountPlot (1).png" alt="Issue Bar Graph">
            </div>
            
            <div class="graphContainer">
                <h3>Performance Trend</h3>
                <p>Line plot showing the trend of performance over time</p>
                <img src="LinePlot (1).png" alt="Performance Trend">
            </div>
            
            <div class="graphContainer">
                <h3>Issue Pie Chart</h3>
                <p>Pie Chart illustrating different issues</p>
                <img src="PieChart (1).png" alt="Issue Pie Chart">
            </div>
            
            <div class="graphContainer">
                <h3>Simple Heat Map</h3>
                <p>Heat map showing direct relation between columns</p>
                <img src="SimpleHeatmap (1).png" alt="Simple Heat Map">
            </div>
            
            <div class="graphContainer">
                <h3>Complex Heat Map</h3>
                <p>Heat map showing indirect relation between columns</p>
                <img src="ComplexHeatmap (1).png" alt="Complex Heat Map">
            </div>
            
            <div class="graphContainer">
                <h3>Network Graph</h3>
                <p>Correlation between issue and type illustrated</p>
                <img src="NetworkPlot (1).png" alt="Network Graph">
            </div>
        </div>
    </div>
</body>
</html>
"""

html_template = html_template.replace('img src="CountPlot.png"', f'img src="{count_plot_base64}"')
html_template = html_template.replace('img src="LinePlot.png"', f'img src="{line_plot_base64}"')
html_template = html_template.replace('img src="PieChart.png"', f'img src="{pie_chart_base64}"')
html_template = html_template.replace('img src="SimpleHeatmap.png"', f'img src="{heatmap_base64}"')
html_template = html_template.replace('img src="ComplexHeatmap.png"', f'img src="{complex_heatmap_base64}"')
html_template = html_template.replace('img src="NetworkPlot.png"', f'img src="{network_plot_base64}"')

# Save the template to an HTML file (optional)
with open("report_template.html", "w") as template_file:
    template_file.write(html_template)

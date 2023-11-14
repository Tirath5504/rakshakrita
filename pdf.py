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

# Save the template to an HTML file (optional)
with open("report_template.html", "w") as template_file:
    template_file.write(html_template)

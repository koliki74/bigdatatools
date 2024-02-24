# Assignment 3 submission

<center>Hasvitha Kolikineni</center>

API used: NASA's Near Earth Objects API.

Visualization tool: Matplotlib

Data Storage: Redis

This application demonstrates data fetching, data processing and visualizing, and data storing using Python and redis.

Before running the program, 
<li>
  Install the required packages using:
  <code>pip install requests matplotlib</code>
</li>
<li>
  Start Redis server
</li>
<li>
  Get API key and add it to the main.py file. {I have the API key at the top of the google doc submitted}
</li>

Run the application with <code>python main.py</code>

Charts Generated
<li>Line Chart: Shows the count of NEOs detected each day over the current week.
  <img src="https://github.com/koliki74/bigdatatools/blob/main/assignment3/line_chart.png" alt="Line Chart">
<li>Bar Chart: Compares the daily NEO counts visually.
  <img src="https://github.com/koliki74/bigdatatools/blob/main/assignment3/bar_chart.png" alt="Bar Chart">
<li>Pie Chart: Displays the distribution of NEO detections across the week.
  <img src="https://github.com/koliki74/bigdatatools/blob/main/assignment3/pie_chart.png" alt="Pie Chart">

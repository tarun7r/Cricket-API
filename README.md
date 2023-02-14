<H2>Cricket API</H2>
This is a simple Flask web application that provides an API to retrieve Player Stats, Live Score, Fixtures, Tables and Results data of Cricket Matches ( ODI, T20, Test and IPL ) from Cricbuzz
<h2>API Endpoints</h2>

<p>The application provides the following API endpoints:</p>

<h3>GET  /players/{player_name}</h3>

<p>This endpoint retrieves information about a cricket player with the given name. The player name should be provided as a URL parameter.</p>

<p>The API returns a JSON object with the following structure:</p>

<pre><code>[
    {
        "Player Name": "Player Name",
        "Country": "Country",
        "Role": "Role",
        "Batting Career Summary 1": {
            "Mode1": "Test",
            "Matches": "Matches",
            "Runs": "Runs",
            "HS": "HS",
            "Avg": "Avg",
            "SR": "SR",
            "100s": "100s",
            "50s": "50s"
        },
        "Batting Career Summary2": {
            "Mode2": "ODI",
            "Matches": "Matches",
            "Runs": "Runs",
            "HS": "HS",
            "Avg": "Avg",
            "SR": "SR",
            "100s": "100s",
            "50s": "50s"
        },
        "Batting Career Summary3": {
            "Mode2": "T20I",
            "Matches": "Matches",
            "Runs": "Runs",
            "HS": "HS",
            "Avg": "Avg",
            "SR": "SR",
            "100s": "100s",
            "50s": "50s"
        }
    }
]</code></pre>

<h3>GET /schedule</h3>
	<p>The API returns a JSON array containing the details of upcoming matches, including date, teams, and tournament.</p>
  <p>The API returns a JSON object with the following structure:</p>
<pre><code>["India vs South Africa, 1st ODI","India vs South Africa, 2nd ODI","India vs South Africa, 3rd ODI",...]</code></pre>


<h3>GET /live</h3>
<p>The API returns a JSON array containing the details of live matches, including team names, scores, and overs played.</p>
 <p>The API returns a JSON object with the following structure:</p>
<pre><code>["Australia 45/1 (8.4 ov)","Bangladesh 136/4 (17.4 ov)","India 118/2 (13.3 ov)",...]</code></pre>
  
<h2>Live Score</h2>
<ul>
  <li>Live Score of all the Matches Going on present</li>
  <br> <img src="Cricket API/live_matches.jpg"> <br>
 </ul>
 <h2>Schedule</h2>
 <ul>
  <li>Schedule of the next Upcoming Matches</li>
  <br> <img src="Cricket API/schedule.jpg"> <br>
 </ul>
 
  <h2>Individual PLayer Stats</h2>
 <ul>
  <li>Example: Stats of Virat Kohli | You can use the common name of the Players as well to retrive the datails</li>
  <br> <img src="Cricket API/player_stats.jpg"> <br>
 </ul>



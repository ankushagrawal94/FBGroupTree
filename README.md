FBGroupTree

Visualize your effect on the growth of the community by determining how many members you were directly and indirectly responsible for adding to the community

Step 1: Use CasperJS to scrape the data
        casperjs playWithCasper.js > HTML.txt
Step 2: Parse the output HTML.txt to Tab Delim Format
        python parseTheHTML.py HTML.txt > parsed.txt
Step 3: Convert the data to a Tree and into JSON format
        python NamesToJSON.py parsed.txt > flare.json
Step 4: Paste the JSON data into line 45 of TreeVisualized.html
        Open the html in Web Browser when to complete to see the results
      
To Use for your FB Group:
  Add Elleo Cheerio to the FB Group
  Change the group name / # to reflect your group in playWithCasper.js
  Change the parent name to your group name in NamesToJSON.py

Benchmarks:

On HH MHacks (~1.2K People)
Web Scraping took 17 minutes
Parsing the HTML took 48 minutes
Converting the names to JSON takes <1 second

The HTML.txt file was 232 MB
The parsed.txt file was 108 KB
The uniqparsed.txt file was 50 KB
The flare.JSON is 85 KB

To Do:
Find a way to make the string parsing much more effecient
Figure out how to save the password in an external config file
Make this mappable as a time series
Make it possible to see how many people each person is resposible for adding
Make it possible to only require parsing the new data when updating a graph
Make this available as an online service available to all
  Find a way to let users input their login information sercurely for use casper
  This will eliminate the need for Elleo to exist
Include an expand/collapse all button
Include a leaderboard for people who added the most people within X degrees (x = 1 to infinity)
Find a way to deal with the people who added so many people that it condenses all the data
  Perhaps use the time ability for this
Add the ability to hover over a person's name to see profile information?
Start storing all data in databses instead of in text files
  This looks really expensive to keep effecient
  Perhaps look into a way to host this locally?
Write a search function for each of the components
  For the graph, it highlights the path it took to get to you (and minimizes all others)
  For the leaderboards, it takes you to your name

One idea for speeding up the first two steps is two make the actions occur concurrently
That is, in the current scheme, we are
  1) Waiting a long for all the HTML to be downloaded
  2) Then waiting an even longer time for the HTML to be parsed
Step 2 does not depend on the entire completion of step 1.
If parsing of the HTML was happening as each file was downloaded the load time would be significantly faster
As a part of this, the file size would be significantly smaller
This would speed things up because:
  Smaller HTML files mean less memory required with current parsing technique
  Not waiting on the internet for files to download
  Potential to make this application multi-threaded

What we have built here can be seen as a tool for measuring the growth of a community.

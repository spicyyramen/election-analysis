# election-analysis

## Project Overview

1. Calculate the total number of votes cast
2. Get complete list of all candidates who got votes
3. Calculate total number of votes each candidate received
4. Calculate the percentage of votes each candidate received
5. Determine the winner of the election based on popular vote

## Resources
- Data source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code, 1.60.2

## Summary 
The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The candidates, their percentage of votes, and total number of votes were as follows:
	- Charles Casper Stockham: **23.0%** of the total vote and **85,213** total votes
	- Diana DeGette: **73.8%** of the total vote and **272,892** total votes
	- Raymon Anthony Doane: **3.1%** of the total vote and **11,606** total votes
- The winning candidate was:
	- Diana Degette: 73.8% (272,892)
- The votes broken down by county were as follows:
	- Jefferson: **10.5%** of votes, **38,855** total votes
	- Denver: **82.8%** of votes, **306,055** total votes
	- Arapahoe: **6.7%** of votes, **24,801** total votes
- The county with the largest number of votes:
	- Denver: 8.28% (306,055)

## Election-Audit Summary
With just a few modifications, this script can be used to analyze essentially any election. If you needed to import a different csv file with election data, you would just need to verify that the column indices (ballot ID, county, candidate) were in the same order as the election_results file. If they match, the only thing you should need to change are the names of the csv file being imported, and the text file being output. 

If the column indices don't match, you can just change the index numbers used in the `candidate_name = row[2]` and `county_name = row[1]`. 

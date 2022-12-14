# Election-Analysis

## Project Overview
We've been asked by the Colorado Board of Elections to audit the results of a recent congressional election. The task included the following steps:

- Count the total number of votes
- Track each candidate and their share of votes
- Determine the winner of the election based on popular vote

## Resources
- Source: election_results.csv
- Software: Python 3.9.13, Anaconda Navigator 2.3.0, Jupyter 6.4.12

## Results and Summary
In total, 369,711 votes were cast. The candidates are listed below:

- Charles Casper Stockham
- Diana DeGette
- Raymond Anthone Doane

Their shares of the votes were as follows:

- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

The winner of the election was Diana DeGette with 73.8% of the vote, totalling 272,892.

To the Colorado Board of Elections: This script can be used with any table of votes that is formatted exactly like election_results.csv. Regardless of the number of candidates or counties in the election, the script will count just fine. The code checks columns with index 1 and 2 (columns 2 and 3), so adding other columns to the analysis would require looking at further indices. If a table has the same data but in different columns, the indices of the columns in the code may be changed to reflect the new data.

## Challenge Overview
Our challenge was to repeat the previous analysis while also keeping track of which county each vote came from. The votes spanned three counties; Jefferson, Denver, and Arapahoe. We calculated the amount of votes belonging to each county, their percentage of the total vote count, and the county with the highest voter turnout.

## Challenge Summary
The county analysis results are as follows:
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

The county with the most votes was Denver.

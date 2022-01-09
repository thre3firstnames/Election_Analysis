# Election Audit using Python
## Overview
Assist the Colorado Board of Elections with automating the vote-counting process in a congressional precinct using Python and certifying the results. 

## Results
The following list contains the results of the election, based on the data output by Python.
##### *Command line output screenshot below data*
- **369,711** total votes were cast in this election
- Counties in this precinct, their vote percentages, and the number of votes cast in each:
  - **Jefferson:** 10.5% (38,855)
  - **Denver:** 82.8% (306,055)
  - **Arapahoe:** 6.7% (24,801)
- **Denver County** had the largest voter turnout in this election
- Candidate results, their percentages, and the total votes cast for each: 
  - **Charles Casper Stockham:** 23.0% (85,213)
  - **Diana DeGette:** 73.8% (272,892)
  - **Raymon Anthony Doane:** 3.1% (11,606)
- The election’s winner, the total votes cast, and the win percentage: 
  - Diana DeGette – 272,892 – 73.8%
 
![cmd_output.png](/Resources/cmd_output.png)

## Summary: 
With minimal modifications, any election can use this script. 
- With additional data regarding the voting method (or further insight into the *Ballot ID* structure), an analyst could provide statistics for the type of vote cast in each county in the precinct. This data could help predict and inform the voting habits of voters within each county. 
- Replacing **county** values for those **states** who do not use a ranking/weighted system(currently only Alaska & Maine), this program would need almost no modification at all to operate on a national level for the allocation of electoral college votes. 

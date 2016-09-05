# Draftkings Lineup Optimizer

Using Genetic Algorithms to optimize Draftkings lineups based on set parameters.

## How to use the Algo:

* For LoL:
  1. Download the Draftkings CSV from their website and save it in the text directory with the default name of "DKSalaries.txt"
  2. Go to http://fantasy.na.lolesports.com/en-US/stats and for each week played download the ```<tbody>``` tag of the table and save it in the html folder with lcs_fantasy_week_x.html
  3. On that site, also download the entire split stats and save it in the html folder as lcs_fantasy_stats_split.html
  4. Do the last 2 steps for the teams as well.
  5. Then just run the run.py file in the LCS folder with ```python run.py```
* For NFL:
  1. Download the Draftkings CSV from their website and save it in the data directory with the default name of "DKSalaries.txt"
  2. Then just run the run.py file in the NFL folder with ```python run.py```

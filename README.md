# DK_Lineup_Optimizer
Genetic Algorithm that prints me money

I believe that making a draftkings lineup is nothing more than an optimization/statistics problem. I am attempting to solve this problem using a Genetic Algorithm that uses a super secret fitness formula (see LCSFitnessFormulas).

## How to use the Algo:

⋅⋅ First of all it only runs for LCS, will add more sports as the seasons change
⋅⋅ For LoL:
⋅⋅1. Download the Draftkings CSV from their website and save it in the text directory with the default name of "DKSalaries.txt"
⋅⋅2. Go to http://fantasy.na.lolesports.com/en-US/stats and for each week played download the <tbody> tag of the table and save it in the html folder with lcs_fantasy_week_x.html
⋅⋅3. On that site, also download the entire split stats and save it in the html folder as lcs_fantasy_stats_split.html
⋅⋅4. Do the last 2 steps for the teams as well.
⋅⋅5. Then just run the run.py file in an IDE or with
'''bash
python run.py
'''

## ToDo:
⋅⋅ Automatically pull html and csv from the internet and save them in the appropriate directories with the correct names
⋅⋅ Add command line arguments to run the algo through terminal
⋅⋅ Add compatibility with different sports (NFL, NBA)
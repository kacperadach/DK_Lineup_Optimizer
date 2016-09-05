from BeautifulSoup import BeautifulSoup

from LCSTeamNameMatcher import match_team_name

BASE_URL = "lcs_fantasy_"
BASE_URL_TEAM = "team_lcs_fantasy_"

def update_lcs_fantasy_stats(player_holder, first, last):
    htmlFile_str = "html/" + BASE_URL + "stats_split.html"
    htmlFile = open(htmlFile_str)
    source_code = htmlFile.read()
    soup = BeautifulSoup(source_code)
    all_table_row = soup.findAll('tr')
    for r in all_table_row:
        tables = r.findAll("td")
        name = tables[0].text
        avg_points_split = tables[4].text
        player_holder.update_player_average_performance(name, avg_points_split)

    for x in range(first, last+1):
        htmlFile_str = "html/" + BASE_URL + "week_" + str(x) + ".html"
        htmlFile = open(htmlFile_str)
        source_code = htmlFile.read()
        soup = BeautifulSoup(source_code)
        all_table_row = soup.findAll('tr')
        for r in all_table_row:
            tables = r.findAll("td")
            name = tables[0].text
            avg_points = tables[4].text
            if avg_points != 0:
                player_holder.update_player_week_performance(name, avg_points)

    htmlFile_str = "html/" + BASE_URL_TEAM + "stats_split.html"
    htmlFile = open(htmlFile_str)
    source_code = htmlFile.read()
    soup = BeautifulSoup(source_code)
    all_table_row = soup.findAll('tr')
    for r in all_table_row:
        tables = r.findAll("td")
        name = tables[0].text
        avg_points_split = tables[2].text
        wins = tables[4].text
        player_holder.update_player_average_performance(match_team_name(name), avg_points_split, wins)

    for x in range(first, last+1):
        htmlFile_str = "html/" + BASE_URL_TEAM + "week_" + str(x) + ".html"
        htmlFile = open(htmlFile_str)
        source_code = htmlFile.read()
        soup = BeautifulSoup(source_code)
        all_table_row = soup.findAll('tr')
        for r in all_table_row:
            tables = r.findAll("td")
            name = tables[0].text
            avg_points = tables[2].text
            if avg_points != 0:
                player_holder.update_player_week_performance(match_team_name(name), avg_points)

    player_holder.update_player_standard_dev()







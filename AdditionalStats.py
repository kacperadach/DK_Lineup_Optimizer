from BeautifulSoup import BeautifulSoup

def update_lcs_player_stats(player_holder, file_path):
    HtmlFile = open(file_path, 'r')
    source_code = HtmlFile.read()
    soup = BeautifulSoup(source_code)
    all_table_row = soup.findAll('tr')
    for r in all_table_row:
        tables = r.findAll("td")
        name = tables[0].text
        kda = tables[3].text
        kills = tables[4].text
        deaths = tables[5].text
        assists = tables[6].text
        kill_participation = tables[7].text
        cs_per_minute = tables[8].text
        minutes_played = tables[10].text
        data = [kda, kills, deaths, assists, kill_participation, cs_per_minute, minutes_played]
        player_holder.update_player(name, data)

def update_lcs_fantasy_stats(player_holder, first, last):
    HtmlFile1 = open("na_lcs_fantasy_stats_split.html")
    source_code = HtmlFile1.read()
    soup = BeautifulSoup(source_code)
    all_table_row = soup.findAll('tr')
    for r in all_table_row:
        tables = r.findAll("td")
        name = tables[0].text
        avg_points_split = tables[4].text
        player_holder.update_player_average_performance(name, avg_points_split)

    for x in range(first, last+1):
        htmlfile_str = "na_lcs_fantasy_week_" + str(x) + ".html"
        htmlfile = open(htmlfile_str)
        source_code = htmlfile.read()
        soup = BeautifulSoup(source_code)
        all_table_row = soup.findAll('tr')
        for r in all_table_row:
            tables = r.findAll("td")
            name = tables[0].text
            avg_points = tables[4].text
            player_holder.update_player_week_performance(name, avg_points)
    player_holder.update_player_standard_dev()







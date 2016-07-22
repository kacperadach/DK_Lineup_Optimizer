from BeautifulSoup import BeautifulSoup

def update_lcs_fantasy_stats(player_holder, first, last, base_url):
    htmlfile_str = "html/" + base_url + "stats_split.html"
    HtmlFile1 = open(htmlfile_str)
    source_code = HtmlFile1.read()
    soup = BeautifulSoup(source_code)
    all_table_row = soup.findAll('tr')
    for r in all_table_row:
        tables = r.findAll("td")
        name = tables[0].text
        avg_points_split = tables[4].text
        player_holder.update_player_average_performance(name, avg_points_split)

    for x in range(first, last+1):
        htmlfile_str = "html/" + base_url + "week_" + str(x) + ".html"
        htmlfile = open(htmlfile_str)
        source_code = htmlfile.read()
        soup = BeautifulSoup(source_code)
        all_table_row = soup.findAll('tr')
        for r in all_table_row:
            tables = r.findAll("td")
            name = tables[0].text
            avg_points = tables[4].text
            if avg_points != 0:
                player_holder.update_player_week_performance(name, avg_points)
    player_holder.update_player_standard_dev()







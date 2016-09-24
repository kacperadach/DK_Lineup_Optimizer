import re
import csv
import requests
from bs4 import BeautifulSoup as BS
import unicodedata

from constants import FFPRO, POSITIONS

def build_fp_pages(week=None, use_espn=False):
    '''
    Scrape FanPros - for some reason, defense projections disappear mid-week
    so option exists to just scrape ESPN here
    '''
    fp_pages = []
    if use_espn:
        POSITIONS.remove('dst')
        fp_pages.append('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=16')
    for pos in POSITIONS:
        fp_pages.append([
            '{}{}.php{}'.format(FFPRO, pos.lower(), ('' if not week else '?week={}'.format(week))), pos
        ])
    return fp_pages


def unicode_normalize(*args):
    defense = []
    for x in args:
        defense.append(unicodedata.normalize('NFKD', x).encode('ascii', 'ignore'))
    return defense

def calculate_ppr(row, pos):
    row = [x.text for x in row]
    projected_score = 0
    if pos.upper() == 'QB':
        projected_score += (0.04 * float(row[3])) + (4 * float(row[4])) + (3 if float(row[3]) >= 300 else 0) + (-1 * float(row[5])) + (0.1 * float(row[7])) + (6 * float(row[8])) + (3 if float(row[7]) >= 100 else 0) + (-1 * float(row[9]))
    elif pos.upper() == 'RB' or pos.upper() == 'WR':
        projected_score += (0.1 * float(row[2])) + (6 * float(row[3])) + (3 if float(row[2]) >= 100 else 0) + (1 * float(row[4])) + (0.1 * float(row[5])) + (6 * float(row[6])) + (3 if float(row[5]) >= 100 else 0) + (-1 * float(row[7]))
    elif pos.upper() == 'TE':
        projected_score += (1 * float(row[1])) + (0.1 * float(row[2])) + (6 * float(row[3])) + (3 if float(row[2]) >= 100 else 0) + (-1 * float(row[4]))
    elif pos.upper() == 'DST':
        points_allowed = float(row[8])
        if points_allowed == 0:
            projected_score += 10
        elif points_allowed <= 6:
            projected_score += 7
        elif points_allowed <= 13:
            projected_score += 4
        elif points_allowed <= 20:
            projected_score += 1
        elif points_allowed <= 27:
            pass
        elif points_allowed <= 34:
            projected_score += -1
        else:
            projected_score += -4
        projected_score += (1 * float(row[1])) + (2 * float(row[2])) + (2 * float(row[3])) + (6 * float(row[5])) + (2 * float(row[7]))
    return row[0], round(projected_score, 2)

def scrape(week):
    hold = []
    for page in build_fp_pages(week):
        r = requests.get(page[0])
        soup = BS(r.text, 'html.parser')
        if 'espn' in page[0]:
            for row in soup.select('.playerTableTable tr'):
                try:
                    p_check = row.findAll(class_="playertablePlayerName")
                    if len(p_check) == 0:
                        continue
                    defense_name = p_check[0].text
                    defense_points = row.find_all('td')[-1].text
                    defense = unicode_normalize(defense_name, defense_points)
                    hold.append(defense)
                except Exception, e:
                    print 'Error scraping ESPN data: ' + str(e)
        else:
            for row in soup.find_all('tr', class_=re.compile('mpb-player-')):
                try:
                    hold.append(calculate_ppr(row.find_all('td'), page[1]))
                except Exception, e:
                    print 'Error scraping FanPros data: ' + str(e)

    with open('data/fan-pros.csv', 'w') as fp:
        w = csv.writer(fp, delimiter=',')
        w.writerows(hold)


if __name__ == "__main__":
    scrape()

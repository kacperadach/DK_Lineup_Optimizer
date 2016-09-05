from random import randint

from constants import POSITIONS_WITH_FLEX

class NFLPlayerHolder:
    def __init__(self, players, games=None, projections=None):
        self.qb = []
        self.rb = []
        self.wr = []
        self.te = []
        self.dst = []
        self.flex =[]
        self.games = games
        for p in players:
            if p.position.upper() == "QB":
                self.qb.append(p)
            elif p.position.upper() == "RB":
                self.rb.append(p)
            elif p.position.upper() == "WR":
                self.wr.append(p)
            elif p.position.upper() == "TE":
                self.te.append(p)
            elif p.position.upper() == "DST":
                self.dst.append(p)
            if p.position != "DST" or p.position != "QB":
                self.flex.append(p)
        if projections:
            self.update_projections(projections)

    def update_projections(self, projections):
        for set in (self.qb, self.rb, self.wr, self.te, self.flex, self.dst):
            for p in set:
                for proj in projections:
                    if set != self.dst:
                        p_name = p.name.split(" ")[0].upper() + p.name.split(" ")[1].upper()
                        proj_name = proj[0].split(" ")[0].upper() + proj[0].split(" ")[1].upper()
                    else:
                        p_name = p.name.replace(" ", "").upper()
                        proj_name = proj[0].split(" ")[-1].upper()
                    if p_name == proj_name:
                        p.update_projected_points(float(proj[1]))
                        projections.remove(proj)
                        break
    
    def get_random_player(self, position):
        pos_array = None
        if position in POSITIONS_WITH_FLEX:
            pos_array = getattr(self, position.lower(), None)
        if pos_array is None:
            return
        else:
            index = randint(0, len(pos_array)-1)
            return pos_array[index]

    def remove_non_projected_players(self):
        for set in (self.qb, self.rb, self.wr, self.te, self.flex, self.dst):
            for p in set:
                if not p.projected_points or p.projected_points == 0:
                    set.remove(p)

from random import randint

class LoLPlayerHolder:

    def __init__(self, players):
        self.mid = []
        self.top = []
        self.jng = []
        self.adc = []
        self.sup = []
        self.team = []
        self.flex =[]
        for p in players:
            if p.position.upper() == "MID":
                self.mid.append(p)
            elif p.position.upper() == "TOP":
                self.top.append(p)
            elif p.position.upper() == "JNG":
                self.jng.append(p)
            elif p.position.upper() == "ADC":
                self.adc.append(p)
            elif p.position.upper() == "SUP":
                self.sup.append(p)
            elif p.position.upper() == "TEAM":
                self.team.append(p)
            if p.position != "TEAM":
                self.flex.append(p)


    def update_player_week_performance(self, name, performance):
        for set in (self.mid, self.top, self.jng, self.adc, self.sup, self.flex, self.team):
            for p in set:
                if p.name.upper() == name.upper():
                    p.update_week_performances(performance)

    def update_player_average_performance(self, name, performance):
        for set in (self.mid, self.top, self.jng, self.adc, self.sup, self.flex, self.team):
            for p in set:
                if p.name.upper() == name.upper():
                    p.update_average_performance(performance)

    def update_player_standard_dev(self):
        for set in (self.mid, self.top, self.jng, self.adc, self.sup, self.flex, self.team):
            for p in set:
                p.calculate_stan_dev()

    def get_random_player(self, pos):
        if pos.upper() == "MID":
            pos_array = self.mid
        elif pos.upper() == "TOP":
            pos_array = self.top
        elif pos.upper() == "JNG":
            pos_array = self.jng
        elif pos.upper() == "ADC":
            pos_array = self.adc
        elif pos.upper() == "SUP":
            pos_array = self.sup
        elif pos.upper() == "TEAM":
            pos_array = self.team
        elif pos.upper() == "FLEX":
            pos_array = self.flex

        if pos_array is None:
            return
        else:
            index = randint(0, len(pos_array)-1)
            return pos_array[index]

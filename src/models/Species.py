class Species():
    def __init__(self, adult_food_daily, landscape, exhibit_id, adult_after):
        self.adult_food_daily = adult_food_daily
        self.landscape = landscape
        self.exhibit_id = exhibit_id
        self.adult_after = adult_after
    
    def evolueren_naar_woestijn(self):
        self.landscape = 'woestijn'
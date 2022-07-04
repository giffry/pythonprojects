class Batsman:
    def batstat(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printval(self):
        print(self.name,self.age,self.place)

class Allrounders(Batsman):
    def bowlstat(self,wickets,economy):
        self.wickets=wickets
        self.economy=economy
    def printstat(self):
        print(self.name,self.age,self.place,self.wickets,self.economy)



from abc import ABC, abstractmethod

# code not following ISP
class Cricketer(ABC):
    @abstractmethod
    def bowl(self):
        pass
    @abstractmethod
    def bat(self):
        pass
    @abstractmethod
    def field(self):
        pass
    @abstractmethod
    def wicket_keep(self):
        pass

# code that follow ISP
class Cricketer(ABC):
    @abstractmethod
    def field(self):
        pass

class Batter(Cricketer):
    @abstractmethod
    def bat(self):
        pass

class Bowler(ABC):
    @abstractmethod
    def bowl(self):
        pass

class WicketKeeper(Cricketer):
    @abstractmethod
    def wicket_keep(self):
        pass

class LeftHandedBatter(Batter):
    def bat(self):
        print("I am a left handed opner Batsman")
    
    def field(self):
        print("I am a sleep fielder")

class SpinBowler(Bowler):
    def bowl(self):
        print("I am a leg spin bowler")
    
    def field(self):
        print("I am a point fielder")

class AllRounder(Batter,Bowler):
    def bat(self):
        print("I am right handed batsman ")
    
    def bowl(self):
        print("I am a fast bowler")

    def field(self):
        print("I can field anywhere")
if __name__ == "__main__":
    batter = LeftHandedBatter()
    batter.bat()
    batter.field()
    bowler = SpinBowler()
    bowler.bowl()
    bowler.field()
    all_rounder = AllRounder()
    all_rounder.bat()
    all_rounder.bowl()
    all_rounder.field()
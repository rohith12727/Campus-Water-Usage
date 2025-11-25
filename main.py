class WaterUsage:

    def __init__(self, shower_time: int, flushes: int, sink_time: int, housing: str):
        self.shower_time = shower_time
        self.flushes = flushes
        self.sink_time = sink_time
        self.housing = housing

    def __repr__(self):
        return "Your shower usage is {} minutes, your sink usage is {} minutes, your toilet flushes number {}, and you live in {} housing.".format(self.shower_time, self.sink_time, self.flushes, self.housing)

def shower_time_to_gallons(time: list[WaterUsage]):

def flushes_to_gallons(flushes: list[WaterUsage]):

def sink_time_to_gallons(time: list[WaterUsage]):

def average_water_usage(usage: list[WaterUsage], housing: str) -> float:
        total_gallons = 0


class WaterUsage:

    def __init__(self, shower_time: float, flushes: float, sink_time: float, housing: str):
        self.shower_time = shower_time
        self.flushes = flushes
        self.sink_time = sink_time
        self.housing = housing

    def __repr__(self):
        return "Your shower usage is {} minutes, your sink usage is {} minutes, your toilet flushes number {}, and you live in {} housing.".format(self.shower_time, self.sink_time, self.flushes, self.housing)


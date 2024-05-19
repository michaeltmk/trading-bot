import strategies

class scheduler:
    def __init__(self):
        self.strategies = []
        self.strategies.append(strategies.strategy1())
        self.strategies.append(strategies.strategy2())
        self.strategies.append(strategies.strategy3())

    def run(self):
        for strategy in self.strategies:
            strategy.run()

class signal_generator:
    def __init__(self):
        self.strategies = []
        self.strategies.append(strategies.strategy1())
        self.strategies.append(strategies.strategy2())
        self.strategies.append(strategies.strategy3())

    def run(self):
        for strategy in self.strategies:
            strategy.run()

    def run(self):
        self.scheduler.run()



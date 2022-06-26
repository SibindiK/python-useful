class StrategyExecutor:
    ''' executes the chosen strategy '''
    def __init__(self, strategy=None):
        self._strategy = strategy

    def execute_strategy(self, arg1, arg2):
        if (self._strategy == None):
            return "No Strategy Selected"
        return (self._strategy.execute(arg1, arg2))

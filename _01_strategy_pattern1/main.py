#Demonstrates strategy pattern in Python by passing
#objects of type strategy
from add_strategy import AddStrategy
from subtract_strategy import SubtractStrategy

from strategy_executor import StrategyExecutor

def main():
    se1 = StrategyExecutor()
    print(se1.execute_strategy(12, 3))
    se2 = StrategyExecutor(AddStrategy())
    print(se2.execute_strategy(12, 3))
    se3 = StrategyExecutor(SubtractStrategy())
    print(se3.execute_strategy(12, 3))

if __name__ == "__main__":
    main()

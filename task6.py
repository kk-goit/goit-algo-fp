import heapq

class GreedyItem:
    def __init__(self, itm_name: str, item: list):
        self.name = itm_name
        self.greedies = item['calories']/item['cost']

    def __lt__(self, other):
        return self.greedies > other.greedies
    
def greedy_algorithm(items: dict, budget: int) -> tuple[list, int]:
    '''Greedy algorithm to choose the items'''
    gheap = []
    for itm in items.keys():
        heapq.heappush(gheap, GreedyItem(itm, items[itm]))
    gitems = []
    calories = 0
    while gheap:
        itm = heapq.heappop(gheap)
        if items[itm.name]['cost'] > budget:
            continue
        gitems.append(itm.name)
        budget -= items[itm.name]['cost']
        calories += items[itm.name]['calories']
    return gitems, calories

class DynamicItem:
    def __init__(self, name, cal, chs):
        self.name = name
        self.calories = cal
        self.chs = chs

    def __lt__(self, other):
        return self.calories > other.calories
    
    def __str__(self):
        return f"{self.name} has {self.calories}"

def dynamic_programming(items: dict, budget: int, memo: dict = {}, exclude: list = []) -> tuple[list, int]:
    '''Dynamic algorithm to choose the items'''
    if budget <= 0:
        return [], 0

    choose = []
    for itm in list(items.keys() - exclude):
        if budget >= items[itm]['cost']:
            excl = exclude.copy()
            excl.append(itm)
            ex = ','.join(excl)
            rem = budget - items[itm]['cost']
            if rem in memo and ex in memo[rem]:
                chs, cls = memo[rem][ex]
            else:
                chs, cls = dynamic_programming(items, rem, memo, excl)
                memo[rem] = {ex: (chs, cls)}
            heapq.heappush(choose, DynamicItem(itm, items[itm]['calories'] + cls, chs))
    if choose:
        itm = heapq.heappop(choose)
        chs = itm.chs
        chs.append(itm.name)
        return chs, itm.calories
    return [], 0


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    for budget in [30, 50, 100, 150, 200]:
        itms, calories = greedy_algorithm(items, budget)
        print(f"For buget {budget:3} the Greedy algorithm gives {calories:5} from: {itms}")
        itms, calories = dynamic_programming(items, budget)
        print(f"For buget {budget:3} the Dynamic algorithm gives {calories:4} from: {itms}\n")
        

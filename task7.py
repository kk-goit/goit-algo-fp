import random
from prettytable import PrettyTable

def get_new_sum(stat: list):
    cub1 = int(random.uniform(1, 7))
    cub2 = int(random.uniform(1, 7))
    stat[cub1+cub2-2] += 1

if __name__ == "__main__":
    while True:
        rq = input("Please, enter the count of experiments (in 100k):").strip()
        if not rq.isdecimal():
            print(f"{rq} is not a digit")
            continue
        break
    stat = [0]*11 
    exps = 100000*int(rq)
    for _ in range(exps):
        get_new_sum(stat)
    rez = {i+2: f"{100*stat[i]/exps:.2f}%" for i in range(len(stat))}
    
    t = PrettyTable(['Sum', 'Probability'])
    for sum in rez.keys():
        t.add_row([sum, rez[sum]])
    print(t)

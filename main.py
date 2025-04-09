from alg1 import spread_of_fire
from alg2 import find_cheapest_delivery

##inputs for algorithms
#alg1
forest1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
forest2 = [
    [2,1,1],
    [0,1,1],
    [1,0,0]
]
forest3 = [
    [0,2]
]
#alg2
routes = [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500]
]
src = 0; dst = 2
k1 = 1; k2 = 0; k3 = 1

if __name__ == '__main__':
    print("======================================")
    print("Aglorithm 1 - Spread of Fire")
    print("Example 1 Output:", spread_of_fire(forest1))  
        #4
    print("Example 2 Output:", spread_of_fire(forest2))  
        #-1
    print("Example 3 Output:", spread_of_fire(forest3))  
        #0
    print("\n======================================")
    print("Algorithm 2 - cheapest delivery")
    print("Example 1 Output:", find_cheapest_delivery(3, routes, src, dst, k1))  
        #200
    print("Example 2 Output:", find_cheapest_delivery(3, routes, src, dst, k2))  
        #500
    print("Example 3 Output:", find_cheapest_delivery(3, routes, src, 3, k3))   
        #-1

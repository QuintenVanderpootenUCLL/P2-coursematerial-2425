import itertools

def find_shortest_path(distance, city_count):
   
    cities = list(range(1, city_count)) 
    shortest_tour = None
    min_distance = float('inf')
    
    for perm in itertools.permutations(cities):
       
        tour = [0] + list(perm) + [0]
        
        total_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
       
        if total_distance < min_distance:
            min_distance = total_distance
            shortest_tour = tour
            
    return shortest_tour
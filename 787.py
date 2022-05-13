# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford
        
        # Previous array
        previous = [float("inf") for i in range(n)]
        # Set up 0th flight
        previous[src] = 0
        # Current array
        current = previous.copy()
        
        # Get max iteration count
        target_flights = k + 1
        
        for num_flights in range(1, target_flights + 1):
            for flight in flights:
                flight_from, flight_to, flight_cost = flight
                
                new_cost = previous[flight_from] + flight_cost
                if current[flight_to] > new_cost:
                    current[flight_to] = new_cost
                    
            previous = current.copy()
                
        if current[dst] == float("inf"):
            return -1
        else:
            return current[dst]
            
        
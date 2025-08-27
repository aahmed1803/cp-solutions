"""
You are designing a delivery system using drones in a linear warehouse. The warehouse is represented as a number line starting at position 0 and ending at position target (target > 0). Along this line, there are charging stations placed at various positions, represented by an array stations, where stations[i] is the position of the ith charging station.

Each drone has a limited battery that allows it to travel a maximum of 10 units after being fully charged. For example, if a drone is charged at position 12, it can travel to positions 12, 13, 14, ..., up to position 22 (inclusive), but cannot reach position 23 or beyond without recharging.

Your delivery protocol requires the following steps:

From your current position, pick up the cargo and carry it on foot to the nearest charging station ahead of you. If there are no more stations ahead, carry the cargo on foot to the target position.
Deploy a fully charged drone from this station and send it with the cargo as far as possible toward the target.
If the target hasn't been reached, walk to the point where the drone landed to retrieve the cargo, then repeat from step 1.
Your task is to calculate the total distance over which you must carry the cargo on foot, from position 0 to position target.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(stations.length × target) will fit within the execution time limit.

Example

For target = 23 and stations = [7, 4, 14], the output should be solution(target, stations) = 4.

Starting at 0, you find the nearest station at position stations[1] = 4, so you carry the cargo on foot for 4 units to get there, and then deploy a drone that travels to position 14.
There is another station at 14 (stations[2] = 14), which you use to deploy another drone that reaches the target position target = 23.
Therefore, you carried the cargo on foot only 4 units in total.
For target = 27 and stations = [15, 7, 3, 10], the output should be solution(target, stations) = 7.

Starting at position 0, you find the nearest station ahead is at position stations[2] = 3, so you carry the cargo on foot for 3 units to get there, and then deploy a drone that travels to position 13.
From position 13, the nearest station ahead is at position stations[0] = 15, which requires carrying the cargo on foot for 2 more units, and from there your drone reaches position 25.
There are no more stations ahead, so you carry the cargo on foot for 2 more units to the target position.
Therefore, you carried the cargo on foot 3 + 2 + 2 = 7 units in total.
For target = 10 and stations = [], the output should be solution(target, stations) = 10.

There are no charging stations available, so you must carry the cargo on foot the entire distance, which is 10 units.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer target

An integer representing the target position you need to reach.

Guaranteed constraints:
1 ≤ target ≤ 1000.

[input] array.integer stations

An array of charging station positions. It is guaranteed stations will all be at different positions.

Guaranteed constraints:
0 ≤ stations.length ≤ 200,
1 ≤ stations[i] < target.

[output] integer

Using the protocol described above, return the total distance over which you must carry the cargo on foot.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""


def solution(target, stations):

    stations.sort()
    current_pos = 0
    total_walk = 0
        
    while current_pos < target:
        
        nearest = None
        
        for station in stations:
            if station >= current_pos:
                nearest = station
                break # maybe
                
            
        if nearest is None:
            total_walk += target - current_pos
            break
            
        walked = nearest - current_pos
        
        #print(walked)
        total_walk += walked
        current_pos = nearest
        #print(total_walk)
        flied = current_pos + 10
        
        #print (flied)
        
        if flied >= target:
            break
        
        
        #next_pos = min(flied, target)
        
        current_pos = flied
            
    return total_walk
    

def delivery_system():
    target = 23 
    stations = [7, 4, 14]
    expected = 4
    result = solution(target, stations)
    print(result)
    assert result == expected
    
    target = 20
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    expected = 1
    result = solution(target, stations)
    print(result)
    assert result == expected


delivery_system()

    
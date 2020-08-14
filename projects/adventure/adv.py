from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# readme suggest using a random traversal
# going to mimic a depth first and use a queue to go down unexplored paths
# dfs more effcient than bfs because each traversal has psudeo weight (weight of 1?)
# go north until you can't go north, then east, then west, then south
#each time you go a direction other than north, it should still attempt to go north
# each node is a room and each edge is a "corridor"
# need path so i'm not brute forcing when I back track
# while traversing add to path in the Queue so the last one in is the first one out
# while back tracking do want to hold a seperate queue of attempted routes?
#



def dungeon_search(starting_room):
    s = Stack() 
    s.push([starting_room])
    visited = set()
    path = []
    #past_directions = Stack()
    opposites = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

    while len(visited) < len(room_graph):
        directions = []
        visited.add(player.current_room)
        exits = player.current_room.get_exits()

        for i in exits:
            if player.current_room.get_room_in_direction(i) not in visited:
                directions.append(i)

        #choose an exit based on direction order
        # add it to path
        # getting stuck in endless loops might be a k,v problem

    
        if len(directions) > 0:
            direction = random.sample(directions, 1)
            path.append(direction[0])
            player.travel(direction[0])
            s.push(direction[0])
        # if you reach a dead end go the opposite direction 
        else:
            turn_around = s.pop()
            player.travel(opposites[turn_around])
            path.append(opposites[turn_around])
    
    #thank god
    return path






traversal_path = dungeon_search(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room

visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
# for i in visited_rooms:
#     print('room:', i.name)
#     print('description:', i.description)


if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

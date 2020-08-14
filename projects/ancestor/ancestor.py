from util import Queue, Stack, Graph

# notes on problem to solve: return earliest known ancestor (the one furthest
# in distance from the imput individual in upward direction) example; furthest
# from 6 is 10, and furthest from 9 is 4, etc.
# values exist as [parent, child] pairs


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8),
                  (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    '''
    Writing a function that given dataset, we obtain the node furtheset to the
    the top.
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
    # for list of touples, check and see if the values in the tuples connect
    # to other tuples.
    # when tuples connect, that is a vertex; replace the child for the parent
    # and call the next tuple
    # ancestors_list = []
    # # parentis gonna be ancestor[a][0], child is ancestor[a][1]
    # for ancestor in range(len(ancestors)):
    #     # print(ancestor[0], ancestor[1])
    #     if ancestor[1] == starting_node:
    #         ancestors_list.append(ancestor[0])
    #         starting_node = ancestor[0]

    # Set up an empty graph with Graph() from imports
    g = Graph()

    for pair in ancestors:

        g.add_vertex(pair[0])
        g.add_vertex(pair[1])

    for pair in ancestors:
        g.add_edge(pair[1], pair[0])

    q = Queue()
    q.enqueue([starting_node])

    if len(g.get_neighbors(starting_node)) == 0:
        return -1
    #
    else:
        while q.size() > 0:
            path = q.dequeue()
            vert = path[-1]

            for parent in g.get_neighbors(vert):
                new_path = list(path)
                new_path.append(parent)
                q.enqueue(new_path)
        return vert
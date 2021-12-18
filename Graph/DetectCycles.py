def DetectNRemoveCycle(edge_list, is_directed):
    print('======================')
    vertex_set = set()
    adjacent_dict = {}
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
        if edge[0] not in adjacent_dict:
            adjacent_dict[edge[0]] = set(edge[1])
        else:
            adjacent_dict[edge[0]].add(edge[1])
        if edge[1] not in adjacent_dict:
            adjacent_dict[edge[1]] = set()
        else:
            if not is_directed:
                adjacent_dict[edge[1]].add(edge[0])
    print('adjacent_dict = ', adjacent_dict)
    visited_set = set()
    pre_numbers = {}
    post_numbers = {}
    clock = 0
    connected_component = {}
    dfs_tree = []
    def dfs(root, cc):
        nonlocal dfs_tree
        visited_set.add(root)
        connected_component[root] = cc
        nonlocal clock
        pre_numbers[root] = clock
        clock += 1
        for child in sorted(adjacent_dict[root]):
            if child not in visited_set:
                print(root, '->', child)
                dfs_tree.append([root, child])
                dfs(child, cc)
        post_numbers[root] = clock
        clock += 1


    cc = 0
    # for v in vertex_set:
    #     if v not in visited_set:
    #         print('start with v = ', v)
    #         cc += 1
    #         clock = 0
    #         dfs(v, cc)

    v = 'a'
    print('start with v = ', v)
    cc += 1
    clock = 0
    dfs(v, cc)

    print('dfs tree = ', dfs_tree)

    redundant_edges = []
    if is_directed:
        for edge in edge_list:
            if pre_numbers[edge[1]] < pre_numbers[edge[0]] and post_numbers[edge[0]] < post_numbers[edge[1]]:
                redundant_edges.append(edge)

    else:
        for edge in edge_list:
            found = False
            for dfs_edge in dfs_tree:
                if edge[0] == dfs_edge[0] and edge[1] == dfs_edge[1]:
                    found = True
            if not found:
                redundant_edges.append(edge[::])

    return redundant_edges

edges = [['a', 'b'], ['a', 'c'], ['a', 'f'], ['b', 'e'], ['c', 'd'], ['d', 'h'], ['d', 'a'], ['e', 'f'], ['e', 'g'], ['e', 'h'], ['f', 'g'], ['f', 'b'], ['h', 'g']]
print(DetectNRemoveCycle(edges, True))
print(DetectNRemoveCycle(edges, False))







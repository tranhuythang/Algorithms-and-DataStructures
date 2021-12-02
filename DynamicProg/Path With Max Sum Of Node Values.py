def PathWithMaxSumOfNodeValues(root, nodes):
    visited_nodes = set()
    def dfs(root):
        maxPathSum = float("-inf")
        visited_nodes.add(root)
        child_count = 0
        print(root, '-', 'children = ', nodes[root]['children'])
        for child in nodes[root]['children']:
            if child not in visited_nodes:
                print('child', child)
                child_count += 1
                sum_child_path = dfs(child)
                if maxPathSum < sum_child_path:
                    maxPathSum = sum_child_path
                    print('updated max', maxPathSum)
        if child_count == 0:
            return nodes[root]['value']
        else:
            return maxPathSum + nodes[root]['value']
    return dfs(root)

node_dict = {}
node_dict['A'] = {'children': ['B', 'C', 'D'], 'value': 3}
node_dict['B'] = {'children': ['A', 'E', 'F'], 'value': 2}
node_dict['C'] = {'children': ['A', 'G'], 'value': 1}
node_dict['D'] = {'children': ['A', 'G', 'H', 'K', 'L'], 'value': 10}
node_dict['E'] = {'children': ['B', 'M', 'N'], 'value': 1}
node_dict['F'] = {'children': ['B'], 'value': 3}
node_dict['G'] = {'children': ['C', 'P', 'Q'], 'value': 9}
node_dict['P'] = {'children': ['G'], 'value': 9}
node_dict['Q'] = {'children': ['G'], 'value': 8}
node_dict['M'] = {'children': ['E'], 'value': 4}
node_dict['N'] = {'children': ['E'], 'value': 5}
node_dict['H'] = {'children': ['D'], 'value': 1}
node_dict['K'] = {'children': ['D'], 'value': 5}
node_dict['L'] = {'children': ['D'], 'value': 3}


print(PathWithMaxSumOfNodeValues('A', node_dict))





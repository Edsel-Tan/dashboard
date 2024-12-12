import time
import itertools

n = 7
curr_states = {}
starting_state = [(-1, 0) for i in range(n)] #component id, component size
starting_state.append(0) #largest component size
starting_state = tuple(starting_state)
curr_states[starting_state] = 1

row_states = [list(i) for i in itertools.product(range(2), repeat = n)]
prob = 1 / 2**n

for trial in range(n):
    new_states = {}
    for curr_state in curr_states:
        for row_state in row_states:
            index = 0
            new_state = []
            component_graph = {}
            index_graph = {}
            component_order = []
            component_number = 0

            updates = True
            while updates:
                updates = False
                index = 0
                while index < n:
                    if row_state[index] == 1:
                        end_index = index
                        while row_state[end_index] == 1:
                            end_index += 1
                            if end_index >= n:
                                break

                        cn = component_number
                        for i in range(index, end_index):
                            if curr_state[i][0] != -1:
                                if curr_state[i][0] in component_graph.keys():
                                    cn = min(component_graph[curr_state[i][0]], cn)
                                else:
                                    component_graph[curr_state[i][0]] = cn
                                    
                        for i in range(index, end_index):
                            if curr_state[i][0] != -1:
                                if component_graph[curr_state[i][0]] < cn:
                                    component_graph[curr_state[i][0]] = cn
                                    updates = True

                        component_number = max(cn+1, component_number)
                        
                    index += 1

            index = 0
            component_number = 0
            while index < n:
                if row_state[index] == 0:
                    component_order.append(-1)
                    index += 1
                else:
                    end_index = index
                    while row_state[end_index] == 1:
                        end_index += 1
                        if end_index >= n:
                            break

                    cn = component_number
                    for i in range(index, end_index):
                        if curr_state[i][0] != -1:
                            if curr_state[i][0] in component_graph.keys():
                                cn = min(component_graph[curr_state[i][0]], cn)
                    for i in range(index, end_index):
                        component_order.append(cn)
                    component_number = max(cn+1, component_number)
                    index = end_index

            component_count = {}
            counted_components = []
            index = 0
            for i in component_order:
                if i != -1:
                    if curr_state[index][0] not in counted_components:
                        counted_components.append(curr_state[index][0])
                        if i in component_count.keys():
                            component_count[i] += curr_state[index][1]
                        else:
                            component_count[i] = curr_state[index][1]
                    if i in component_count.keys():
                        component_count[i] += 1
                    else:
                        component_count[i] = 1
                index += 1
                        

            for i in component_order:
                if i == -1:
                    new_state.append((-1,0))
                else:
                    new_state.append((i, component_count[i]))
                    
            
            m = curr_state[-1]
            for i in component_count.keys():
                m = max(m, component_count[i])
            new_state.append(m)
            new_state = tuple(new_state)
            if new_state in new_states.keys():
                new_states[new_state] += curr_states[curr_state] * prob
            else:
                new_states[new_state] = curr_states[curr_state] * prob

    curr_states = new_states

E = 0
for i in curr_states.keys():
    E += curr_states[i] * i[-1]
print(E)
                
                        
                        
                    
        

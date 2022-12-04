def search_path(current_vertex, current_path):
    global path_list, arcs
    for destination_vertex in arcs[current_vertex]:
        new_path = current_path.copy()
        new_path.append(destination_vertex)
        if destination_vertex == "end":
            path_list.append(new_path)
        elif destination_vertex.isupper() or destination_vertex not in current_path:
            search_path(destination_vertex, new_path)


file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

arcs = dict()
for row in input_file_rows:
    x, y = row.strip().split("-")
    if y == "start":
        if y in arcs:
            arcs[y].append(x)
        else:
            arcs[y] = [x]
    elif x == "end":
        if y in arcs:
            arcs[y].append(x)
        else:
            arcs[y] = [x]
    else:
        if x != "end":
            if x in arcs:
                arcs[x].append(y)
            else:
                arcs[x] = [y]
        if x != "start" and y != "end":
            if y in arcs:
                arcs[y].append(x)
            else:
                arcs[y] = [x]

path_list = []
for starting_vertex in arcs["start"]:
    path = ["start", starting_vertex]
    search_path(starting_vertex, path.copy())
print(len(path_list))

def dynamic_intersection(a, b):
    dict_a = {x:i for i, x in enumerate(a)}
    length_b = len(b)
    output_list = []
    for i in range(length_b):
        output = 0
        for i in range(length_b):
            intersection = dict_a.get(b[i], length_b+1)
            if intersection < i:
                output+=1
        output_list.append(output)
    return output_list
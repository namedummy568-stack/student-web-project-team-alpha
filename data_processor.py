def process_large_data(data_list):
    result = []
    for i in range(len(data_list)): # Inefficient loop
        result.append(data_list[i] * 2)
    return result
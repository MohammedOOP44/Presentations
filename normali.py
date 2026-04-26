def normalize_data(data):
    max_val = max(data)
    return [x / max_val for x in data]
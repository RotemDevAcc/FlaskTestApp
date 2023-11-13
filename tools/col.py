def myzip(it1, it2):
    if not it1 or not it2:
        return None
    
    result = zip(it1, it2)
    return list(result)
import matplotlib.pyplot as plt

def Depth(item):
    deepType = (list, tuple, dict, set)
    if not type(item) in deepType:
        return 0
    else:
        if not item:
            return 0
        else:
            if type(item) is dict:
                return 1 + max(Depth(val) for val in item.values())
            else:
                return 1 + max(Depth(val) for val in item)

# def ListPlot(data):

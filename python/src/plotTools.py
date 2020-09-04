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


def CreateCanvas():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    return fig, ax


def Show():
    plt.show()


def Export(file_name, fig):
    fig.savefig(file_name)


def ListPlot(fig, ax, datas_list):
    if Depth(datas_list) == 2:
        datas_list = [datas_list]
    elif Depth(datas_list) == 3:
        pass
    else:
        print("Error: The depth of datas_list must be 2 or 3.")
        print("       Now, the depth of datas_list is "+str(Depth(datas_list)))

    for datas in datas_list:
        xDatas = list(map(lambda data: data[0], datas))
        yDatas = list(map(lambda data: data[1], datas))
        ax.scatter(xDatas, yDatas)

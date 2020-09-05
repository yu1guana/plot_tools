import matplotlib.pyplot as plt

width_RunTimeError = 12
space_RunTimeError = " "*14

# Get depth of a variable
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


# Creates a pair of a figure and axes
def CreateCanvas():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    return fig, ax


# Shows figures
def Show():
    plt.show()


# Saves a figure as a file
def Export(file_name, fig):
    fig.savefig(file_name)


def ListPlot(fig, ax, datas_list, PlotLegendNames=None):
    # Check a number of graphs
    if Depth(datas_list) == 2:
        num_graphs = 1
        datas_list = [datas_list]
    elif Depth(datas_list) == 3:
        num_graphs = 2
    else:
        error_message = "The depth of datas_list must be 2 or 3.\n"
        error_message = space_RunTimeError + " Now, the depth of datas_list is equal to "\
                + str(Depth(datas_list)) + "."
        raise RuntimeError(error_message)

    # Check a number of legends.
    if PlotLegendNames == None:
        num_legends = num_graphs
        PlotLegendNames = [None for i in range(num_legends)]
    else:
        if Depth(PlotLegendNames) == 0:
            num_legends = 1
            PlotLegendNames = [PlotLegendNames]
        elif Depth(PlotLegendNames) == 1:
            num_legends = len(PlotLegendNames)
        else:
            error_message  = "The depth of legends is must be 0 or 1.\n"
            error_message += space_RunTimeError + " Now, the depth of legends is equal to "\
                    + str(Depth(PlotLegendNames)) + "."
            raise RuntimeError(error_message)
        if num_legends != num_graphs:
            error_message  = "The number of graphs and legends are different.\n"
            error_message += space_RunTimeError+"The number of graphs: "+str(num_graphs)+"\n"
            error_message += space_RunTimeError+"The number of legends: "+str(num_legends)
            raise RuntimeError(error_message)

    # Plot
    for i_datas in range(num_graphs):
        xDatas = list(map(lambda data: data[0], datas_list[i_datas]))
        yDatas = list(map(lambda data: data[1], datas_list[i_datas]))
        ax.scatter(xDatas, yDatas, label=PlotLegendNames[i_datas])
    # Legends
    if any([ False if PlotLegendName == None else True for PlotLegendName in PlotLegendNames]):
        ax.legend()

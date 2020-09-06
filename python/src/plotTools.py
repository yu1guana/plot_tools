import matplotlib.pyplot as plt

width_RunTimeError = 12
space_RunTimeError = " "*14

# Gets depth of a variable.
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

# Has a figure and an axes.
class Canvas():
    __fig = None
    __ax  = None
    # Creates figure and axes
    def __init__(self, FontFamily=None, MathFontFamily="custom", FlagTicks=True, TicksDirection="in", LabelNames=None, TitleName=None, PlotRange=None):
        # plt.rcParams["text.usetex"] = True
        if FontFamily != None:
            plt.rcParams["font.family"] = FontFamily
        plt.rcParams["mathtext.fontset"] = MathFontFamily
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        # Ticks settings
        if Depth(FlagTicks) == 0:
            FlagTicks = [FlagTicks for i in range(4)]
        elif Depth(FlagTicks) == 1:
            if len(FlagTicks) != 4:
                error_message  = "Length of FlagTicks is wrong.\n"
                error_message += space_RunTimeError\
                        +"Now, length of FlagTicks is equal to "+str(len(FlagTicks))
                raise RuntimeError(error_message)
        else:
            error_message  = "Depth of FlagTicks is wrong.\n"
            error_message += space_RunTimeError+"Now, "+str(Depth(FlagTicks))
            raise RuntimeError(error_message)
        if not TicksDirection in ("in", "out"):
            error_message  = "TicksDirection '"+str(TicksDirection)+"' is wrong."
            raise RuntimeError(error_message)
        self.__ax.tick_params(top=FlagTicks[0])
        self.__ax.tick_params(bottom=FlagTicks[1])
        self.__ax.tick_params(left=FlagTicks[2])
        self.__ax.tick_params(right=FlagTicks[3])
        self.__ax.tick_params(direction=TicksDirection)
        # Axes label settings
        if LabelNames != None:
            if Depth(LabelNames) == 1 and len(LabelNames) == 2:
                self.__ax.set_xlabel(LabelNames[0], fontsize=15)
                self.__ax.set_ylabel(LabelNames[1], fontsize=15)
            else:
                error_message = "Depth "+str(Depth(LabelNames))+" or length "\
                        +str(len(LabelNames))+" are wrong."
                raise RuntimeError(error_message)
        # Title settings
        if TitleName != None:
            self.__ax.set_title(TitleName, fontsize=20)
        # Plot range settings
        if PlotRange != None:
            if Depth(PlotRange) == 1 and len(PlotRange) == 2:
                self.__ax.set_xlim(xmin=PlotRange[0])
                self.__ax.set_xlim(xmax=PlotRange[1])
            elif Depth(PlotRange) == 2 and len(PlotRange) == 2\
                    and Depth(PlotRange[0]) == 1 and Depth(PlotRange[1]) == 1\
                    and len(PlotRange[0]) == 2 and len(PlotRange[1]) == 2:
                self.__ax.set_xlim(xmin=PlotRange[0][0])
                self.__ax.set_xlim(xmax=PlotRange[0][1])
                self.__ax.set_ylim(ymin=PlotRange[1][0])
                self.__ax.set_ylim(ymax=PlotRange[1][1])
            else:
                error_message = "PlotRange is wrong."
                raise RuntimeError(error_message)

    # Shows figures in all canvases
    @staticmethod
    def Show():
        plt.show()

    # Saves a figure as a file
    def Export(self, file_name):
        self.__fig.savefig(file_name)

    # Core of 2D plot.
    def Plot2dCore(self, datas_list, plotType, PlotLegendNames):
        # Check a number of graphs
        if Depth(datas_list) == 2:
            num_graphs = 1
            datas_list = [datas_list]
        elif Depth(datas_list) == 3:
            num_graphs = 2
        else:
            error_message  = "The depth of datas_list must be 2 or 3.\n"
            error_message += space_RunTimeError + " Now, the depth of datas_list is equal to "\
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
            if plotType == "ListPlot":
                self.__ax.scatter(xDatas, yDatas, label=PlotLegendNames[i_datas])
            elif plotType == "ListLinePlot":
                self.__ax.plot(xDatas, yDatas, label=PlotLegendNames[i_datas])
            else:
                error_message  = "Plot type is wrong.\n"
                error_message += space_RunTimeError+"Now, the plot type is "+str(plotType)
                raise RuntimeError(error_message)

        # Legends
        if any([ False if PlotLegendName == None else True for PlotLegendName in PlotLegendNames]):
            self.__ax.legend()

    # Plot datas as circles
    def ListPlot(self, datas_list, PlotLegendNames=None):
        self.Plot2dCore(datas_list, "ListPlot", PlotLegendNames=PlotLegendNames)

    # Plot datas as lines
    def ListLinePlot(self, datas_list, PlotLegendNames=None):
        self.Plot2dCore(datas_list, "ListLinePlot", PlotLegendNames=PlotLegendNames)

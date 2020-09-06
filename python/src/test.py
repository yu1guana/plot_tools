import numpy as np
import plotTools as pt

def test_Depth():
    print_depth = lambda item: print("Depth of", item, "is "+str(pt.Depth(item)))

    print_depth(1)
    print_depth(1.1)
    print_depth("Hello")
    print()
    print_depth( list()  )
    print_depth( tuple() )
    print_depth( dict()  )
    print_depth( set()   )
    print()
    print_depth( [1, 2] )
    print_depth( (1, 2) )
    print_depth( {"a":1, "b":2} )
    print_depth( set([1,2]) )
    print()
    print_depth( [list(), list()] )
    print_depth( [[[]]] )
    print()
    print_depth( [[1, 2], [3, 4]])
    print_depth( [[1, [2,3], 4], 5, [6,7]] )
    print()
    print_depth( ([1, (2,3), 4], 5, [6,7]) )
    print()
    print_depth( ([1, (set(),3), 4], 5, [6,7]) )
    print_depth( ([{"a": 2}, (set(),3), 4], 5, [6,7]) )


def test_Plot_1():
    canvas= pt.Canvas()
    canvas.ListPlot(gl_2d_1_graph_datas)
    # canvas.Export(gl_graphs_directory+"test.eps")

def test_Plot_2():
    canvas= pt.Canvas()
    canvas.ListPlot(gl_2d_1_graphs_datas_list)
    # canvas.Export(gl_graphs_directory+"test.png")

def test_Plot_3():
    canvas= pt.Canvas()
    canvas.ListPlot(gl_2d_1_graph_datas, PlotLegendNames="sin(x)")

def test_Plot_4():
    canvas= pt.Canvas()
    canvas.ListPlot(gl_2d_1_graphs_datas_list, PlotLegendNames=["sin($x$)","sin(x+$\pi/4$)"])
    # canvas.ListPlot(fig, ax, gl_2d_1_graphs_datas_list, PlotLegendNames=[None,"sin(x+$\pi/4$)"])

def test_Plot_5():
    canvas= pt.Canvas()
    canvas.ListLinePlot(gl_2d_1_graph_datas)
    # canvas.Export(gl_graphs_directory+"test_5.eps")

def test_Plot_6():
    canvas= pt.Canvas()
    canvas.ListLinePlot(gl_2d_1_graphs_datas_list, PlotLegendNames=["sin($x$)","sin(x+$\pi/4$)"])

def test_Plot_7():
    canvas= pt.Canvas()
    canvas.ListLinePlot(gl_2d_1_graph_datas, PlotLegendNames="sin($x$)")
    canvas.ListPlot(gl_2d_2_graph_datas, PlotLegendNames="sin(x+$\pi/4$)")
    # canvas.Export(gl_graphs_directory+"test_7")

gl_graphs_directory = "../graphs/"

gl_2d_1_graph_datas = [ (i, np.sin(i)) for i in np.arange(0, 2*np.pi, 0.1*np.pi)]
gl_2d_2_graph_datas = [ (i, np.sin(i+0.25*np.pi)) for i in np.arange(0, 2*np.pi, 0.1*np.pi)]
gl_2d_1_graphs_datas_list = [[ (i, np.sin(i)) for i in np.arange(0, 2*np.pi, 0.1*np.pi)],\
        [ (i, np.sin(i+0.25*np.pi)) for i in np.arange(0, 2*np.pi, 0.1*np.pi)]]

if __name__ == "__main__":
    # test_Depth()
    test_Plot_7()
    pt.Canvas.Show()

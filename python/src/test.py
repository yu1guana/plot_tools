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


def test_ListPlot_1():
    datas = [ (i, np.sin(i)) for i in np.arange(0, 2*np.pi, 0.1*np.pi)]
    fig, ax = pt.CreateCanvas()
    pt.ListPlot(fig, ax, datas)
    pt.Export("../graphs/ListPlot_1.eps", fig)

def test_ListPlot_2():
    datas_list = []
    datas = [ (i, np.sin(i)) for i in np.arange(0, 2*np.pi, 0.1*np.pi)]
    datas_list.append(datas)
    datas = [ (i, np.sin(i+0.25*np.pi)) for i in np.arange(0, 2*np.pi, 0.1*np.pi)]
    datas_list.append(datas)
    fig, ax = pt.CreateCanvas()
    pt.ListPlot(fig, ax, datas_list)
    pt.Export("../graphs/ListPlot_2.png", fig)

if __name__ == "__main__":
    # test_Depth()
    test_ListPlot_2()
    pt.Show()

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



if __name__ == "__main__":
    test_Depth()

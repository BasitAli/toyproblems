import math
spiral_max = 81
side_length = int(math.sqrt(spiral_max))

def axial_transform(coordinates, axis):
    (x,y) = coordinates
    if axis == 0:
        x+=1
    elif axis == 1:
        y+=1
    elif axis == 2:
        x-=1
    elif axis == 3:
        y-=1
    else:
        raise Exception, "Axis Cant be one of %s"%repr(range(4))
    return((x,y))

def digdug(start, axis=0, path_length=3, reset_lim=3, reset_count=1, last_tup=(0,0)):
    if path_length == 1:
        return (start)
    (x,y) = start
    valueofdigdug = lambda x,y: (y-1)*side_length + x
    for i in xrange(path_length):
        if(last_tup != (x,y)):
            print "(%s %s) - %s"%(x,y, valueofdigdug(x,y))
        last_tup = (x,y)
        if i == path_length - 1:
            break
        (x,y) = axial_transform((x, y), axis)
    if reset_count == reset_lim:
        path_length = path_length - 1
        reset_count = 0
        reset_lim = 2
    reset_count += 1
    return digdug((x,y), (axis+1)%4, path_length, reset_lim, reset_count, last_tup)

digdug((1,1), 0, side_length)

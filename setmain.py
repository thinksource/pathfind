from arrayio import *
from pathfind import *
import sys
if __name__=='__main__':
    startx=0
    starty=0
    string_a=''
    while True:
        in_l=sys.stdin.readline()
        if(in_l=='\n'):
            break
        else:
            string_a+=in_l
    int_a=input_array(string_a)
    endx=len(int_a[0])-1
    endy=len(int_a)-1
    # print endx
    # print endy
    # print int_a
    ps=Astarsearch(startx,starty,endx, endy,int_a)
    ps.find_path()
    print ps.printway()

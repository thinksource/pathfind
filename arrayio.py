

def input_array(data_string):
    a=[]
    # inputline=raw_input()
    for s in data_string.splitlines():
        rin=s.strip().split()
        lineA=list(map(lambda x: int(x,16),rin))
        if(len(lineA)>0):
            a.append(lineA)
    return a

def output(path):
    pass

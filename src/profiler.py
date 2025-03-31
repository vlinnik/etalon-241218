from time import time_ns
def profile(progs: list[callable],first:int = 0):
    sum = 0
    cnt = 0
    while cnt<3:
        t0 = time_ns()    
        only = first
        for prog in progs:
            prog( )
            if only is not None and only>0:
                only-=1
                if only==0: break
        t1 = time_ns()
        sum+=(t1-t0)
        cnt+=1
        yield
    if first>0: print(f'{first},{sum/cnt/first/1000000:.2f}')

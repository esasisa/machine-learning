'''
Created on Jun 19, 2017

@author: sandeep.singh
'''

if __name__ == '__main__':   
    N = int(input());
    num_list = [] 
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != 'print' :
            cmd += "("+ ",".join(args) +")"
            print(cmd)
            eval("num_list."+cmd)
        else: 
            print(num_list)

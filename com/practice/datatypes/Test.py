'''
Created on Jun 19, 2017

@author: sandeep.singh
'''

if __name__ == '__main__':
       
    N = int(input());
    l = [] 
    for _ in range(N):
        s = input().split()
        cmd = "("+ ".".join(s) +")"
        print(cmd)
        

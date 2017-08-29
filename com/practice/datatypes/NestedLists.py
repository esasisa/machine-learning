'''
Created on Jun 20, 2017

@author: sandeep.singh
'''

if __name__ == '__main__':
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]    
    print (sorted(marksheet))
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
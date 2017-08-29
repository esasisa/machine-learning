'''
Created on Jun 20, 2017

@author: sandeep.singh
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])
    
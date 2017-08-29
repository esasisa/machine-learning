'''
Created on Jun 14, 2017

@author: sandeep.singh
'''

if __name__ == '__main__':
    
    n = int(20)
    if(n%2 !=0):
        print("Weird")
    else:
        if (n in range(2,5) or n > 20):
            print("Not Weird")
        if(n in range(6, 21)):
            print("Weird")
            
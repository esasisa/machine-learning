'''
Created on Jun 19, 2017

@author: sandeep.singh
'''

if __name__ == '__main__':
    n = int(input());
    num_list = [] 
    for x in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]    
        if (cmd == "print") : 
            print(num_list)
        
        if (cmd == "insert") : 
            num_list.insert(int(args[0]), int(args[1]))
            
        if (cmd == "remove") : 
            num_list.remove(int(args[0]))
            
        if (cmd == "append") : 
            num_list.append(int(args[0]))
            
        if (cmd == "sort") : 
            num_list.sort()
            
        if (cmd == "pop") : 
            num_list.pop()
        if (cmd == "reverse") : 
            num_list.reverse()
               
    
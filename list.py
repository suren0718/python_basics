if __name__ == '__main__':
    N = int(input())
    li=[]
    
    for i in range(N):
        
        p=input().split()
        cmd=p[0]
        
        if cmd== "insert":
            i, e = int(p[1]), int(p[2])
            li.insert(i, e)
        
        elif cmd== "print":
            print(li)
        
        elif cmd== "remove":
            e=int(p[1])
            li.remove(e)
        
        elif cmd== "append":
            e=int(p[1])
            li.append(e)
        
        elif cmd== "sort":
            li.sort()
            
        elif cmd== "pop":
            li.pop()
        
        elif cmd== "reverse":
            li.reverse()
        

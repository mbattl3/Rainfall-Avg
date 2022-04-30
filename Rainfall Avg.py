def main(): 
    numlist = [0] * 12
    x = 0 
    while x < 12: 
        numb = float(input('Input number: '))
        #print(x, numb) 
        #input("Hit Enter to Continue")
        numlist[x] = numb
        print (numlist) 
        x = x+1      
    listavg = sum(numlist)/len(numlist) 
    print(' # of elements--> ', len(numlist)) 
    print(numlist)                                                              
    print('------') 
    print('highest--> ', max(numlist)) 
    print('lowest--> ', min(numlist)) 
    print('Total--> ', sum(numlist)) 
    print('Average--> ', listavg) 

main() 

# Rain Data
#2.87,1.52, 4.01,6.43, 3.28,3.44,7.68,2.51,0.32,28.70,1.75,0.59

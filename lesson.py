
def armstrong(x):
    power = len(str(x))

    list_num = list(str(x))
    sum = 0


    for i in list_num:
        i = int(i)
        sum += i**power

    if int(x) == sum:
        return (f"{x}")
    else:
        pass        

# armstrong(153)

def all_armstong(x=int(input('Enter a number: '))):
    all = []
    for i in range(x+1):
        if armstrong(i) != None:
            all.append(i)
    
    print(all)
        
    
all_armstong()
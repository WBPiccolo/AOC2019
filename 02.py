 #https://adventofcode.com/2019/day/2
 # opcode 1 a b c: x[c]=x[a]+x[b]
 # opcode 2 a b c: x[c]=x[a]*x[b]
 # opcode 99: break;
 # dopo aver letto un opcode, skippa avanti di 4
def main():
    input_filename="02input.txt"
    with open(input_filename, 'r') as f:
        x = f.readlines()
    i = 0
    #esempio:
    x=[1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    #finchè opcode non è 99:
    while x[i] != 99:
        if x[i] == 1:
            x[i+3] = x[i+1]+x[i+2]
        if x[i] == 2:
            x[i+3] = x[i+1]*x[i+2]
        i += 4
    print (x)
    #dovrebbe essere 3500,9,10,70,  2,3,11,0,  99 ,30,40,50
if __name__ == "__main__":
    main()


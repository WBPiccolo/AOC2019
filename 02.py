 #https://adventofcode.com/2019/day/2
 # opcode 1 a b c: x[c]=x[a]+x[b]
 # opcode 2 a b c: x[c]=x[a]*x[b]
 # opcode 99: break;
 # dopo aver letto un opcode, skippa avanti di 4
def main():
    input_filename="02input.txt"
    i = 0
    #esempio:
    x=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0
]
    #finchè opcode non è 99:
    while x[i] != 99:
        op=x[i]
        a=x[i+1]
        b=x[i+2]
        c=x[i+3]
        if op == 1:
            x[c]=x[a]+x[b]
        if op == 2:
            x[c]=x[a]*x[b]
        i += 4
    print(x)
    #dovrebbe essere 3500,9,10,70, 2,3,11,0, 99 ,30,40,50
if __name__ == "__main__":
    main()


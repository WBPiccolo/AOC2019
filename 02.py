 #https://adventofcode.com/2019/day/2
 # opcode 1 a b c: x[c]=x[a]+x[b]
 # opcode 2 a b c: x[c]=x[a]*x[b]
 # opcode 99: break;
 # dopo aver letto un opcode, skippa avanti di 4
def main():
    input_filename="02input.txt"
    with open(input_filename, 'r') as f:
        x = f.readlines()
    i=0;
    #finchè opcode non è 99:
    while x[i]!=99:
        if x[i]==1:
            #somma:
        if x[i]==2:
            #moltiplica
        i += 1


if __name__ == "__main__":
    main()


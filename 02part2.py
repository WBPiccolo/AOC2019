 #https://adventofcode.com/2019/day/2
 # opcode 1 a b c: x[c]=x[a]+x[b]
 # opcode 2 a b c: x[c]=x[a]*x[b]
 # opcode 99: break;
 # dopo aver letto un opcode, skippa avanti di 4
def main():
    input_filename="02input.txt"
    i = 0
    noun=0
    verb=0
    target = 19690720
    # Find the input noun and verb that cause the program to produce the output 19690720.
    # What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
    # Each of the two input values will be between 0 and 99, inclusive.
    # finchè opcode non è 99:
    for noun in range(0,100):
        for verb in range (0,100):
            x = [1, noun, verb, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 1, 19, 6, 23, 2, 23, 13, 27, 1, 27,
                 5, 31, 2, 31, 10, 35, 1, 9, 35, 39, 1, 39, 9, 43, 2, 9, 43, 47, 1, 5, 47, 51, 2, 13, 51, 55, 1, 55, 9, 59, 2,
                 6, 59, 63, 1, 63, 5, 67, 1, 10, 67, 71, 1, 71, 10, 75, 2, 75, 13, 79, 2, 79, 13, 83, 1, 5, 83, 87, 1, 87, 6,
                 91, 2, 91, 13, 95, 1, 5, 95, 99, 1, 99, 2, 103, 1, 103, 6, 0, 99, 2, 14, 0, 0]
            i=0
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
            #print(x)
            if x[0] == target:
                print(x)
                # What is 100 * noun + verb?
                print(100*x[1]+x[2])
    #dovrebbe essere 3500,9,10,70, 2,3,11,0, 99 ,30,40,50
if __name__ == "__main__":
    main()


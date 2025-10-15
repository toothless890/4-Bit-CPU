import sys

filename = sys.argv[1]
f = open(filename, "r")
linearr = f.read().split("\n")

opcodes = {"nop" : "0000", "halt" : "0001", "write":"0010", "read" : "0011", "add" : "0100", "sub" : "0101", "and" : "0110", "or" : "0111", 
           "xor" : "1000", "mov" : "1001", "movraw" : "1010", "cmp": "1011", "shift" : "1100", "jmp" : "1101"}

registers = {"r0" : "0000", "r1" : "0001", "r2":"0010", "r3" : "0011", "r4" : "0100", "r5" : "0101", "r6" : "0110", "r7" : "0111", 
             "invalid" : "1000", "invalid" : "1001", "invalid" : "invalid", "rc": "1011", "rsl" : "1100", "rsh" : "1101"}
lineCounter = 0

for line in linearr:
    if(line != ""):
        if (line.startswith("//")):
            # print("    ", end="")
            pass
        else: 
            
            splitLine = line.split()
            print(str(lineCounter) , "\t: " ,line.lower())
            lineCounter +=1
            for arg in splitLine:
                
                code = opcodes.get(arg, "err")
                if code == "err":
                    code = registers.get(arg, "err")
                else: 
                    code = arg

                print(code)
                
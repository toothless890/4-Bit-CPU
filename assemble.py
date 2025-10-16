import sys
verbose = False


filename = sys.argv[1]
f = open(filename, "r")
linearr = f.read().split("\n")

opcodes = {"nop" : "0000", "halt" : "0001", "write":"0010", "read" : "0011", "add" : "0100", "sub" : "0101", "and" : "0110", "or" : "0111", 
           "xor" : "1000", "mov" : "1001", "movraw" : "1010", "cmp": "1011", "shift" : "1100", "jmp" : "1101"}

registers = {"r0" : "0000", "r1" : "0001", "r2":"0010", "r3" : "0011", "r4" : "0100", "r5" : "0101", "r6" : "0110", "r7" : "0111", 
             "invalid" : "1000", "invalid register" : "1001", "invalid register" : "1010", "invalid register" : "1011", "invalid register" : "1100",
             "rc": "1101", "rsl" : "1110", "rsh" : "1111"}

functions = {}
lineCounter = 0

for argv in sys.argv:
    if argv == "-v":
        verbose = True

for line in linearr:
    if(line != ""):
        # redundant but preserves line count
        if (line.startswith("//")):
            if verbose:
                print(line)
        else: 
            
            splitLine = line.split()

            if (verbose): print("ROM ",str(lineCounter) , "\t: " ,line.lower(), sep="")
            
            for arg in splitLine:
                # redundant but will support inline comments
                if (arg.startswith("//")):
                    break
                elif (arg.startswith("def")):
                    functions.update({splitLine[1] : lineCounter})
                    # print(lineCounter)
                    break
                lineCounter +=1
                code = opcodes.get(arg, "err")
                if code == "err":
                    code = registers.get(arg, "err")
                if code == "err":
                    if functions.get(arg) != None:
                        code = functions.get(arg)
                    elif arg.startswith("0b"):
                        code = arg.removeprefix('0b')
                    elif (arg.isdigit== True):
                        code = format(int(arg), '04b')
                    
                    else: 
                        code = "ERROR"
                if verbose: print(code, end=" ")
                else: print(code)
            if (verbose): print("")
                    
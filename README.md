4-Bit Processor and custom assembler made with Sebastian Lague's Digital Logic Sim

Instructions: 
  1. Install Digital Logic Sim
  2. open data folder (Ctrl+Alt+Shift+O)
  3. Clone repository into current folder
  4. Rename repository to "Projects" overriding existing folder
  5. Open Project - cpu
  6. Open "Clocker" or "CPU" module
  7. Clear the memory, enable "begin program", cycle the clock once, disable "Begin program", cycle clock until program completes

Program can be altered by opening "256-4 ROM" and then editing "ROM 256x16" then pasting the results of the assembler as binary and saving the chip

Assemble.py takes in a file with assembly code, and an optional -v flag that enables detailed output of the program (with verbose mode, the output cannot be directly pasted into the cpu)

Assembler features include:

  * comments: adding // at any point in a line will allow the rest of the line to be ignored
  
  * opcodes: code names detailed both in test.txt and specs.txt will be converted into their binary representation
  
  * register names: using r1-r7 and rsh, rsl, rc will be converted into their binary representations
    
  * binary and decimal recognition: nubmers preceeded by "0b" will be treated as raw binary values. Other numbers will be interpreted as decimal and converted to binary
  
  * Functions: beginning a line with "def" and following it with a string will mark that location in the assemblers memory as a location to jump back to. using the function name as a location
              for the "jmpraw" operation will jump to the first instruction after the "def" line
    
    Currently, functions are only supported for jumping backwards and not for jumping forwards in code as it is parsed line-by-line and immediately converts function names to binary
  
<img width="1253" height="663" alt="{55447061-CD0F-4868-BA44-B2E9F49EE292}" src="https://github.com/user-attachments/assets/0c83b813-2a7a-47f7-88ee-ba87add2dc1d" />
<img width="829" height="614" alt="{F5D9920B-B4F8-44B6-B738-93A4E87AAAF1}" src="https://github.com/user-attachments/assets/bf3a7e78-0d33-46c5-bdfa-5a43bf07a500" />


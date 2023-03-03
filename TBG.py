# NOTE : to use this code the designe shoule be as folloing
# module <module_name> (bla, bla, bla);
# input size <name> <space> ;
# input <input name > = <input value>
# list the inputs
# output <output name > = <output value>
import sys

# Read in the design file
with open(sys.argv[1], 'r') as f:
    design_lines = f.readlines()

# for each in design_lines:
#     print(design_lines)

# Read in the test cases
with open(sys.argv[2], 'r') as f:
    test_cases = f.readlines()

# print(test_cases)

# Generate the testbench header
testbench = ['`timescale 1ns / 1ps\n']
testbench.append('module testbench;\n')

# Declare the inputs and outputs
for line in design_lines:
    if line.startswith('module'):
        moudelname = line.split()[1]
        # print(moudelname)
    if line.startswith('input'):
        testbench.append(' \n logic ' + line.split()[2]+';')
        # print(line)
    if line.startswith('output'):
        testbench.append('\n  logic ' + line.split()[2]+';')
        # print(line)
# print(design_lines)
# print(testbench)
testbench.append('\n')
# Instantiate the DUT
testbench.append(moudelname+' dut (')

for line in design_lines:
    if line.startswith('input'):
        testbench.append('    .' + line.split()[2] + '(' + line.split()[2] + '),')
        # print(line.split()[2])
    if line.startswith('output'):
        testbench.append('    .' + line.split()[2] + '(' + line.split()[2] + '_out)'+' ')
        testbench.append(' ,')
testbench.append('  );\n')
print(testbench[-2])
testbench.pop(-2)
# testbench.append('  );\n')
# testbench.remove(testbench[-1])


# Declare local variables
for line in design_lines:
    if line.startswith('input'):
        testbench.append('  reg ' + line.split()[2] + ';\n')
        # print("The inputs ",line.split()[1])
    if line.startswith('output'):
        testbench.append('  wire ' + line.split()[2] + '_out;\n')

# Add the initial block
testbench.append('  initial begin\n')

# Add the test cases
# print(test_cases)
for line in test_cases:
    if line.startswith('input'):
        testbench.append(line.split()[1]+'='+line.split()[3] + "\n")
    if line.startswith('output'):
        testbench.append('#1; \n')
    continue

# Close the initial block and the module
testbench.append('  end\n')
testbench.append('endmodule\n')

# Write the testbench to a file
with open('testbench.sv', 'w') as f:
    f.writelines(testbench)

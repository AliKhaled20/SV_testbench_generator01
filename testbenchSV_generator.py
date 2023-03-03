import sys
import random

# Read in the design file
with open(sys.argv[1], 'r') as f:
    design_lines = f.readlines()

# Generate the testbench header
testbench = ['`timescale 1ns / 1ps\n']
testbench.append('module testbench;\n')

# Declare the inputs and outputs
for line in design_lines:
    if line.startswith('input'):
        testbench.append('  ' + line)
    if line.startswith('output'):
        testbench.append('  ' + line)

# Instantiate the DUT
testbench.append('  DUT dut (')
for line in design_lines:
    if line.startswith('input'):
        testbench.append('    .' + line.split()[1] + '(' + line.split()[1] + '),')
    if line.startswith('output'):
        testbench.append('    .' + line.split()[1] + '(' + line.split()[1] + '_out),')
testbench.append('  );\n')

# Declare local variables
for line in design_lines:
    if line.startswith('input'):
        testbench.append('  reg ' + line.split()[1] + ';\n')
    if line.startswith('output'):
        testbench.append('  wire ' + line.split()[1] + '_out;\n')

# Add the initial block
testbench.append('  initial begin\n')

# Generate random test cases
for i in range(10):
    testbench.append('    #10 begin\n')
    for line in design_lines:
        if line.startswith('input'):
            testbench.append('      ' + line.split()[1] + ' = ' + str(random.randint(0, 1)) + ';\n')
    testbench.append('    end\n')

# Close the initial block and the module
testbench.append('  end\n')
testbench.append('endmodule\n')

# Write the testbench to a file
with open('testbench.sv', 'w') as f:
    f.writelines(testbench)

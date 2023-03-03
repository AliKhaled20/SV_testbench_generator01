import sys

with open(sys.argv[1], 'r') as f:
    design_lines = f.readlines()

with open(sys.argv[2], 'r') as f:
    test_cases = f.readlines()
# test_cases.append("hello")
testbench = ['']
# testbench.append("hi")
# print(test_cases)
for line in test_cases:
    if line.startswith('input'):
        # print(line)
        testbench.append(line.split()[3]+"\n")
    if line.startswith('output'):
        testbench.append('#1 \n')
        continue

print(testbench)

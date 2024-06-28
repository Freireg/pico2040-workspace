file = open('/logs/test.txt', 'w')
file.write('First Line\n')
file.close()

file = open('/logs/test.txt', 'r')
output = file.read()
print(output)
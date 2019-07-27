import re


my_file = open('C:\\Users\\mmohan2\\Test Data\\test.txt')
output = my_file.read()
for lines in output.split('\n'):
    line = re.search(r'(\d+).\s+(.+)', lines)
    if not line is None:
        print(line.group(1))
        print(line.group(2))

service = 'Safe/Block_Lists_Logs'
logname = service.title().replace(' ', '_').replace('/', '-').strip() + '_Test'
print(logname)
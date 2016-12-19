f = open('whoupclicklike.py', 'w')

for x in range(10):
    f.write(str(x + 1) + '. ' + input() + '\n')
    
f.close()
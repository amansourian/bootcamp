import os

if os.path.isfile('gimme_phi.txt'):
    print('Sorry, file exists.')
else:
    with open('gimme_phi.txt') as f:
        f.write('The golden ratio is ')
        f.write('{phi:.8f}'.format(phi=1.61803398875))

with open('data/1OLG.pdb', 'r') as f:
    #f_lines = f.readlines()
    #print('In the with block, is the file closed?', f.closed)
    for i, line in enumerate(f):
        print(line.rstrip())
        if i>= 10:
            break
#print('Out of the with block, is the file closed?', f.closed)

#print(f_lines[:3])

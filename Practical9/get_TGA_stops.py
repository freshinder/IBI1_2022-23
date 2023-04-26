# import re
# read file 'Sacchar...'
# create & write file 'TGA_genes.fa'
# modify the data in 'Sacchar...'
#   only extract the gene names
#   make gene sequence into a single line
# create a dictionary to store the modified data
# extract desired data and write them in 'TGA_genes.fa'


import re

# read data in 'Sachhar...'
# create & write 'TGA_genes.fa'
# create a dictionary
file_r = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file_w = open('TGA_genes.fa','x')
sequence = {}

# modify the data
#   only left the gene name
#   remove the line exchange in sequence to make them as single lines
# store them in a dictionary
for line in file_r:
    if line.startswith('>'):
        name = re.match('>(.*?)\s',line).group(1)
        sequence[name] = ''
    else:
        sequence[name] += re.sub('\n','',line)
file_r.close()

# find out sequences ends with 'TGA'
# write the selected data in 'TGA_genes.fa'
for i in sequence.keys():
    if sequence[i].endswith('TGA'):
        file_w.write(i)
        file_w.write('\n')
        file_w.write(sequence[i])
        file_w.write('\n')
file_w.close()





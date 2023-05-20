# Notice user to input stop codon
# Check and notify user the incorrect input
# Use re to remove the line exchange and make the sequences into a single line
# Create a dictionary to store the modified data
# For different stop codon create different fa file
# Select and store data in the dictionary with the target stop codon

# notice user to input the stop codon of interest
print('Please enter the your preferred stop codon (TAA,TAG,TGA)')
stop_codon = str(input())
L = ['TAA','TAG','TGA']

# check and notice user when they input incorrect stop codon
if stop_codon in L:
    det = True
else:
    det = False
while det == False:
    print('Incorrect stop codon\nPlease input correct stop codon (TAA,TGA,TAG)')
    stop_codon = str(input())
    if stop_codon in L:
        det = True


# create a dictionary to store the gene name and the corresponding sequence
# distinguish between gene name and sequence
# identify the gene name from the long list of data
# remove the line exchange and make the sequences into one line using re.sub
read = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
seq = {}
import re
for line in read:
    if line.startswith('>'):
        name = re.match('>(.*?)\s',line).group(1)
        seq[name] = ''
    else:
        seq[name] += re.sub('\n','',line)
read.close()

# create a fa file to store the wanted data
# select the wanted data from the dictionary
# condition: TAA
if stop_codon == 'TAA':
    TAA = open('TAA_stop_genes.fa','x')
    for i in seq.keys():
        if seq[i].endswith('TAA'):
            TAA.write(i)
            TAA.write('\n')
            TAA.write(seq[i])
            TAA.write('\n')
    TAA.close()
# condition: TAG
elif stop_codon == 'TAG':
    TAG = open('TAG_stop_genes.fa','x')
    for i in seq.keys():
        if seq[i].endswith('TAG'):
            TAG.write(i)
            TAG.write('\n')
            TAG.write(seq[i])
            TAG.write('\n')
    TAG.close()
# condition: TGA
elif stop_codon == 'TGA':
    TGA = open('TGA_stop_genes.fa','x')
    for i in seq.keys():
        if seq[i].endswith('TGA'):
            TGA.write(i)
            TGA.write('\n')
            TGA.write(seq[i])
            TGA.write('\n')
    TGA.close()
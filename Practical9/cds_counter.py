# import regular expression
# input seq value
# use re.findall
# since there is only one start codon then we find the number of stop codon

seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
import re

count = 0
# find the number of 'TGA' stop sequences
x = re.findall('TGA',seq)
count = count + len(x)
# find the number of 'TAA' stop sequences
y = re.findall('TAA',seq)
# sum the number of stop codons
count = count + len(y)
print('The total number of possible coding sequences is', count)
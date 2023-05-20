# call a function
# import re
# Check whether the sequence input is correct
# Find the proportion of DNA between start and stop codon in the whole sequence
#   start codon is 'ATG' & stop codon is 'TGA'
#   use re.search & calculate the length of the sequence
#   remind that codon is triplets
#   able to treat both lower, upper case input
# Compare
#   if the proportion is > 50%, return protein-coding
#   if the proportion is < 10%, return non-coding
#   if the proportion is between 10% & 50%, return unclear

def cal(DNA_sequence):
    import re
    check = re.search('[^ATCGatcg]',DNA_sequence)
    if check:
        return 'Incorrect DNA sequence'
    DNA_sequence = DNA_sequence.upper()
    p = re.compile('ATG(...)*?TGA')
    seq = p.search(DNA_sequence)
    if seq:
        proportion = len(seq.group())/len(DNA_sequence)
        if proportion > 0.5:
            return 'protein-coding'
        elif proportion < 0.1:
            return 'non-coding'
        else:
            return 'unclear'
    else:
        return "There is no start codon or stop codon or both"

# Example
DNA_sequence = 'AAAATGGCTAGAACGTGATTGACG'
a = cal(DNA_sequence)
print(a)
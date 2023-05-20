# import blosum as bl
# matrix is blosum(62)
# call functions to find the alignment score, edit distance and identity
#   alignment
#        compare the alignment and obtain a score
#        sum the score to acquire the alignment score
#   edit distance
#        if there is a mismatch edit distance plus 1
#   identity
#        (total length - edit distance)/total distance
# read the files
# extract sequence using called functions
# store them in variable
# there are 3 combination for each case
#   use the called functions to find the alignment score, edit distance and identity
# print out the results


import blosum as bl
matrix = bl.BLOSUM(62)

# called a function to extract the sequence
def find_seq(seq):
    for line in seq:
        if not line.startswith('>'):
            x = line
    return x

# called a function to calculate the alignment score using BLOSUM and the edit distance and the identity
def BLOSUM(seq1,seq2):
    score = 0
    for i in range(len(seq1)):
        val = matrix[seq1[i]][seq2[i]]
        if val >= 0: # positive value added
            score += val
    edit_distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            edit_distance += 1 # edit distance increase by one for each misalignment
    id = '%.4g' % ((len(seq1) - edit_distance) / len(seq1) * 100) + '%'
    # 4 significance figure
    L = [score,edit_distance,id]
    return L

# read files
read_h = open('ACE2_human.fa','r')
read_c = open('ACE2_cat.fa','r')
read_m = open('ACE2_mouse.fa','r')
# find the sequence and store in a variable
seq_h = find_seq(read_h)
seq_c = find_seq(read_c)
seq_m = find_seq(read_m)
# close files
read_h.close()
read_c.close()
read_m.close()

# find the edit distance and the identity of 3 different combinations
result_h_c = BLOSUM(seq_h,seq_c)
result_m_c = BLOSUM(seq_m,seq_c)
result_h_m = BLOSUM(seq_m,seq_h)

# print out the results
print('The analysis of sequence of HUMAN and CAT:\n','  The alignment score:', result_h_c[0], '\n   The edit distance:',result_h_c[1], '\n   The identity:',result_h_c[2])
print('The analysis of sequence of MOUSE and CAT:\n','  The alignment score:', result_m_c[0], '\n   The edit distance:',result_m_c[1], '\n   The identity:',result_m_c[2])
print('The analysis of sequence of HUMAN and MOUSE:\n','  The alignment score:', result_h_m[0], '\n   The edit distance:',result_h_m[1], '\n   The identity:',result_h_m[2])
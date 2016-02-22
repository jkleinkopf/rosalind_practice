#given two strings, s and t, of equal length
#find the Hamming distance between s and t denoted d(s,t)
#hamming distance is the number of differences between s and t

s = "TGGCTCTGGTCTGTGCCGACGCCTTGGTACTCAGGGCCTACTTCTACTATCTAGTACCCGGCATGAACACCACCATGGCTCCACCGATGCGCTTTTGTATAACATATTTGTTGAAGACGCAGACGCGAACTCAGGTGATCATTCGGAATCCTTCACCCATAAAGACTCCACGTGCACCAATACAAAAGTAGCCATTTTACGGTACTCTGTAAAAGGTCCAAAGTTAGAGTCGAACAGCACCAAAAGTGAGCCACACTTCCAAATCGGCCTTCATTTTTTCTAGCGACTCTGGGAAATCTGGTGCATCGACCCGCTTCATTTGCCAAGTCCGAACAAGTGTCTGCGCCTCCTCCTTAGTGTTTCAGTTAGATTCCCCCGAGGTCTGTTTATGGGAGGCATCCGGTCATTCTGGACGTTCCCATCGATTCGCGTCGCTGGCTGTGACAGATCCACGACACTGCATTGGCAAACATGAGCACAAAGGTCCAGTTGCCGCAGGTAAAAGCGATTGTCTAGATGGTCAAAGGTTAGCACTATAGCGTCAATGGGCTCGGCGTAGAAAACGTAACTTACGGCCGCGGCAAGTTGGGGTCGAGTGAGTACCCTCACGAGTCGCTAACAGGAGTTATGCAAATCAGCCCGCGCTTGAGTTAGGCTCGTCGTGCGCTGTGTTCCCGGAGAATGGACTACACAGCAACGGAATGCGGGGTTAATTTATTAGTTGGTCGCAAAGACGTCACTTCATGGTCTTCAAGACTGGGCGCGGCACGTGATGATATGCTTAAAAAACGTGTGCGGAGCGCCAGCACAGCGGCCATGGTCACCCGAAGGCTGGAGTTATACCGGGTAGCAACGCTATGACGCGTGTAAGTGCGCCCCGAAGCTAGTCATCGACGACAATAGCT"
t = "TGCATGGGCTCTGTGCCCCGGTTTCTACACTTCGAGCGGACATCCACTTTAAAGTCGACGGAATCCTCTTCTCCATGGCTAAGGAGTTCCGCTTTTATTATATTTCATTGTTGATAACTCGCCCGTACGCTATGTCAACCAGAGGACTTGGTCGGCCGGTACATACTTGTTTTGGACTGATACCGCTAGGTCCCGTGTCCGGGCCGATGTAAAAGGTACAGAGTTAAGGTTTGACTGCACGTAAGGTGAGTCAAACTGTCAAAGTGTGACACAGTCTTGAAACCCATTCCGGGAAAGCAGCCGCCGGTGCTGGGTTCGTTAACAACGTGCTCACTTTTGATAGTTCCTACCTGGTCGAGCTCTCGATATTGTAAGCCGGCTGTTTTGTGATGAGCGCATCCGTTCTAGGAAGATTCTCCCGTAAAGAGTCTTTCCTGCATCCGCAAGGCTTACCGGTCTGGAACGGCCTCAATGCGCTGATTTTTACTGTCGATCCGCGTAAACCTGATTTTCAAGAGTCTCATAGATTAGAAACAAGATGCCAACAGGCCGGGCCTCGGAAGAGAAGGTTACGGCAAGTGGAGACTGTGCCGCATTCCGGTGACTGCTGGGTTGCTGCGCGCGAGGAAAACTGAAAGTCCTTGTCTGATTTAAGTGGCTGACCTGTTCTCGTCCTTACCCTAGTAGCACACAACAACCGCCTACGGAGGTTATCCACATGGTGACCCACACCATGGCTCTTCATGCTCTTGGAGGCAGGTTCAGAGGCGAAAAGTCCCTTTCAAGTAACACGAGTGAAGTGCTACCACCCCGTTTTTCGTGTGGAATAGGCTGGTTACCAACTCTATGCAGCGAGCCTGACCGGAAGATGAGCTCCGTCCAGCTTGCTATGGTCGACTCCTCCT"

s_list = list(s)
t_list = list(t)

hd = 0 #hamming distance, or number of differences between string s and t

for i in range(len(s)):
	if s_list[i] == t_list[i]:
		hd += 0 #if s and t are the same at index i, don't add to hamming distance
	else:
		hd += 1 #if s and t are not the same at index i, add 1 to hamming distance
		
print "Hamming distance for these two strings is: ", hd
		
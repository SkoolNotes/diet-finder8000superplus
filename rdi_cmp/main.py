import numpy as np

weight_of_protein_eaten = 60
weight_of_human = 60 # kg
amino_acid_comp = ['''Ala (A)  26	 18.1%
Arg (R)   2	  1.4%
Asn (N)   3	  2.1%
Asp (D)   9	  6.2%
Cys (C)   0	  0.0%
Gln (Q)   5	  3.5%
Glu (E)   8	  5.6%
Gly (G)   6	  4.2%
His (H)   2	  1.4%
Ile (I)   4	  2.8%
Leu (L)  13	  9.0%
Lys (K)  14	  9.7%
Met (M)   1	  0.7%
Phe (F)   8	  5.6%
Pro (P)   5	  3.5%
Ser (S)  11	  7.6%
Thr (T)   7	  4.9%
Trp (W)   2	  1.4%
Tyr (Y)   3	  2.1%
Val (V)  15	 10.4%
Pyl (O)   0	  0.0%
Sec (U)   0	  0.0%
''', '''Ala (A)  36	 12.5%
Arg (R)   7	  2.4%
Asn (N)  10	  3.5%
Asp (D)  17	  5.9%
Cys (C)   1	  0.3%
Gln (Q)   4	  1.4%
Glu (E)  13	  4.5%
Gly (G)  20	  7.0%
His (H)  16	  5.6%
Ile (I)   0	  0.0%
Leu (L)  37	 12.9%
Lys (K)  24	  8.4%
Met (M)   5	  1.7%
Phe (F)  17	  5.9%
Pro (P)  10	  3.5%
Ser (S)  18	  6.3%
Thr (T)  14	  4.9%
Trp (W)   3	  1.0%
Tyr (Y)   5	  1.7%
Val (V)  30	 10.5%
Pyl (O)   0	  0.0%
Sec (U)   0	  0.0%
''']
# from https://web.expasy.org/cgi-bin/protparam/protparam1?P02238@noft@
# add one multiline string for each amino acid to concat

amino_acid_rdis = np.array([0, 0, 0, 5, 0, 0, 0, 14, 19, 43, 38, 19, 33, 0, 0, 0, 20, 5, 15, 24, 0, 0], dtype='float64')    # mg per kg of human
# from original diet_finder

names = '''
Ala (A)
Arg (R)
Asn (N)
Asp (D)
Cys (C)
Gln (Q)
Glu (E)
Gly (G)
His (H)
Ile (I)
Leu (L)
Lys (K)
Met (M)
Phe (F)
Pro (P)
Ser (S)
Thr (T)
Trp (W)
Tyr (Y)
Val (V)
Pyl (O)
Sec (U)
'''.strip().split('\n')

amino_acid_rdis *= weight_of_human/1000 # get rdi grams for each amino acid

out = np.zeros((len(amino_acid_comp), len(names)))

for index, protein in enumerate(amino_acid_comp):
    out[index] = np.asarray(list(map(lambda row: float(row.strip().split(' ')[-1][:-1]), protein.strip().split('\n'))), dtype=np.float32)
    out[index] /= len(amino_acid_comp)*100 # convert back to percentage
    out[index] *= weight_of_protein_eaten  # get absolute weight
    out[index] /= amino_acid_rdis          # get ratio to rdi
    out[index] *= 100                      # convert to percentage rdi

np.set_printoptions(precision=3)
for i,a in enumerate(out.T):
    print(names[i], a)


import search_ba as ba
import search_naive as na
import matplotlib.pyplot as plt 
import os
import time
import simulate_fasta as sf
import numpy as np 

Ns = [10000, 30000, 50000, 80000, 100000,150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
Ms = [2, 100, 1000]

# Ns = [500, 1000, 5000]
# Ms = [10,50,100]

tries = 10

naive_search_times = {Ms[0]:{},Ms[1]:{},Ms[2]:{}}
border_search_times = {Ms[0]:{},Ms[1]:{},Ms[2]:{}}

for _ in range(tries):
    for n in Ns:
        random_string =  sf.simulate_string(n)
        # best_case_string = "A"*n
        # worse_case_string = "".join("b" for _ in range(n-1)) 

        for m in Ms:
            print("in iteration ", n)
            random_pattern = sf.simulate_string(m)
            # case_pattern = "".join("b" for _ in range(m-1))

            start_time_exact = time.time()
            na.exact(random_string, random_pattern)
            naive_search_time = time.time() - start_time_exact
            if n in naive_search_times[m]:
                naive_search_times[m][n] += [naive_search_time]
            else:
                naive_search_times[m][n] = [naive_search_time]

            # ba_best_string = (("A"*m)+"B")*n
            # ba_best_pattern = "A"*m
            
            start_time_ba = time.time()
            ba.ba_search(random_string, random_pattern)      
            border_search_time = time.time() - start_time_ba

            if n in border_search_times[m]:
                border_search_times[m][n] += [border_search_time]
            else:
                border_search_times[m][n] = [border_search_time]





naive_search_times[Ms[0]] = {k: np.mean(naive_search_times[Ms[0]][k]) for k in naive_search_times[Ms[0]]}
border_search_times[Ms[0]] = {k: np.mean(border_search_times[Ms[0]][k]) for k in border_search_times[Ms[0]]}
naive_search_times[Ms[1]] = {k: np.mean(naive_search_times[Ms[1]][k]) for k in naive_search_times[Ms[1]]}
border_search_times[Ms[1]] = {k: np.mean(border_search_times[Ms[1]][k]) for k in border_search_times[Ms[1]]}
naive_search_times[Ms[2]] = {k: np.mean(naive_search_times[Ms[2]][k]) for k in naive_search_times[Ms[2]]}
border_search_times[Ms[2]] = {k: np.mean(border_search_times[Ms[2]][k]) for k in border_search_times[Ms[2]]}

x_gl0 = []
y_gl0 = []
x_gl1 = []
y_gl1 = []
x_gl2 = []
y_gl2 = []

x_ba0 = []
y_ba0 = []
x_ba1 = []
y_ba1 = []
x_ba2 = []
y_ba2 = []

for i in naive_search_times[Ms[0]].keys():
    x_gl0.append(i)
    y_gl0.append(naive_search_times[Ms[0]][i])

for i in naive_search_times[Ms[1]].keys():
    x_gl1.append(i)
    y_gl1.append(naive_search_times[Ms[1]][i])

for i in naive_search_times[Ms[2]].keys():
    x_gl2.append(i)
    y_gl2.append(naive_search_times[Ms[2]][i])

####################################################
####################################################

for i in border_search_times[Ms[0]].keys():
    x_ba0.append(i)
    y_ba0.append(border_search_times[Ms[0]][i])

for i in border_search_times[Ms[1]].keys():
    x_ba1.append(i)
    y_ba1.append(border_search_times[Ms[1]][i])

for i in border_search_times[Ms[2]].keys():
    x_ba2.append(i)
    y_ba2.append(border_search_times[Ms[2]][i])


plt.plot(x_gl0, y_gl0, label = str(Ms[0]))
plt.plot(x_gl0, y_gl1, label = str(Ms[1]))
plt.plot(x_gl0, y_gl2, label = str(Ms[2]))
plt.title('naive search for random strings')
plt.xlabel('n')
plt.ylabel('runtime (s)')
plt.legend()
plt.savefig('naive_search_runtimes_worstcase.png', bbox_inches='tight')
plt.show()
plt.clf()

##############################################
############################################

plt.plot(x_ba0, y_ba0, label = str(Ms[0]))
plt.plot(x_ba0, y_ba1, label = str(Ms[1]))
plt.plot(x_ba0, y_ba2, label = str(Ms[2]))
plt.title('border search for random strings')
plt.xlabel('n')
plt.ylabel('runtime (s)')
plt.legend()
plt.savefig('border_search_runtimes_worstcase.png', bbox_inches='tight')
plt.show()
plt.clf()
def generate_subsets(some_set):
    n = len(some_set)
    for i in range(1,2 ** n-1):
        subset = [some_set[j] for j in range(n) if (i & (1 << j)) > 0]
        yield subset
 
def complement(original_list, reference_list):
    return [x for x in reference_list if x not in original_list]

dm = ( # distance matrix
( 0,86,49,57,31,69,50),
(86, 0,68,79,93,24, 5),
(49,68, 0,16, 7,72,67),
(57,79,16, 0,90,69, 1),
(31,93, 7,90, 0,86,59),
(69,24,72,69,86, 0,81),
(50, 5,67, 1,59,81, 0))
n = len(dm) #how many cities
V = range(n) # set of cities
lv = [V]
E = [(i,j) for i in V for j in V if (i!=j and dm[i][j]>0)]

print("there are %d cities"%n)

from pymprog import *
begin('subtour elimination')
x = var('x', E, bool)
maximize(sum(dm[i][j]*x[i,j] for (i,j) in E), 'dist')
for (k,i) in E:
            st(x[k,i] + x[i,k]<=1)
for f in generate_subsets(V):
        for w in f:
            for q in complement(f,V):
                st(sum(x[a,b] for (a,b) in E if a in f and b in complement(f,V)) + sum (x[a,b] for (a,b) in E if b in f and a in complement(f,V)) >=2*(sum(x[w,h] for (w,h) in E)+sum(x[g,q] for (g,q) in E)-1))
solver(float, msg_lev=glpk.GLP_MSG_OFF)
solver(int, msg_lev=glpk.GLP_MSG_OFF)

solve() #solve the IP problem

def tour(x):
   succ = 0
   subt = [succ] #start from node 0
   while True:
      succ=sum(x[succ,j].primal*j 
               for (succ,j) in E)
      if succ == 0: break #tour found
      subt.append(int(succ+0.5))
   return subt

subt = tour(x)
print("Optimal tour length: %g"%vobj())
print("Optimal tour:"); print(subt)
end()
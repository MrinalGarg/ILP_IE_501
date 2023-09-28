import mip
def generate_subsets(some_set):
    n = len(some_set)
    for i in range(1,2 ** n-1):
        subset = [some_set[j] for j in range(n) if (i & (1 << j)) > 0]
        yield subset
 
def complement(original_list, reference_list):
    return [x for x in reference_list if x not in original_list]
d = ((0,3,3,-1000,-1000,-1000),
	 (3,0,3,-1000,-1000,-1000),
	 (3,3,0,3,-1000,-1000),
	 (-1000,-1000,3,0,3,4),
	 (-1000,-1000,0,3,0,3),
	 (-1000,-1000,-1000,4,3,0))

n = len(d) #how many cities
V = range(n) # set of cities
m = mip.Model(solver_name="CBC")

x = [[m.add_var(var_type=mip.BINARY, name=f'x_{i}_{j}') for j in range(n)] for i in range(n)]
wout = [m.add_var(var_type=mip.BINARY, name=f'wout_{i}') for i in range(n)]
win = [m.add_var(var_type=mip.BINARY, name=f'win_{i}') for i in range(n)]
for i in V:
    for j in V:
        if (d[i][j] > 0):
            m += x[i][j] + x[j][i] <= 1

for i in V:
	m += (mip.xsum(
    x[i][j]
    for j in range(n)) == wout[i])
for i in V:
	m += (mip.xsum(
    x[j][i]
    for j in range(n)) == win[i])
for subs in generate_subsets(V):
	m+=(sum(x[a][b] for a in subs for b in complement(subs,V)) 
				== sum (x[a][b] for b in subs for a in complement(subs,V) ))
for subs in generate_subsets(V):
	for h in subs:
		for k in complement(subs,V):
			m+=(sum(x[a][b] for a in subs for b in complement(subs,V))>=wout[h]+win[k]-1)
m.objective = mip.maximize(mip.xsum(
    d[i][j] * x[i][j]
    for i in range(n) for j in range(n)
))



solver_status = m.optimize()
objective_value= m.objective_value
print(f"Estimated future profit: {objective_value}")
# Assuming you have a variable var, and you want to print its value:
for i in range(n):
	for j in range(n):
		var_value = m.var_by_name(f'x_{i}_{j}').x  # Replace 'var_name' with the actual name of your variable
		print(f"Value of var_name: {var_value} _ {i}_ {j}")

from z3 import Solver, BitVec

inp = [BitVec('inp_%i' % i, 8) for i in range(4)]
s = Solver()
s.add(inp[0] > 5)
s.add(inp[0] ^ inp[1] == 3)

s.check()
m = s.model()
sol = [0] * 32
for x in m:
    c = str(x())
    if not '_' in c: continue
    idx = int(c.split('_')[1])
    sol[idx] = str(m[x])
sol = map(lambda x: '%x' % int(x), sol)
sol = ''.join(sol)
print(sol)

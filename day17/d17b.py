from datetime import datetime

lines = [[c for c in n.strip()] for n in open('d17in.txt').read().splitlines()]
active = {(ix, iy, 0, 0) for iy, row in enumerate(lines) for ix, cube in enumerate(row) if cube == '#'}

def neighbors(cube):
    bounds = [range(cube[x]-1, cube[x]+2) for x in range(4)]
    return {(ix, iy, iz, iw) for ix in bounds[0] for iy in bounds[1] for iz in bounds[2] for iw in bounds[3] if cube != (ix, iy, iz, iw)}

def cube_range():
    values = [{c[i] for c in active} for i in range(4)]
    bounds = [range(min(v)-1, max(v)+2) for v in values]
    return [(ix, iy, iz, iw) for ix in bounds[0] for iy in bounds[1] for iz in bounds[2] for iw in bounds[3]]

def cube_becomes_active(cube):
    i_am_active = cube in active
    around_me = len(active & neighbors(cube))
    return (i_am_active and around_me in [2, 3]) or (not i_am_active and around_me == 3)

start = datetime.now()

for _ in range(6):
    active = {c for c in cube_range() if cube_becomes_active(c)}

end = datetime.now()

print(len(active))
print(end-start)

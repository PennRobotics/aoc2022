# For Part B, if there is only one possible beacon position, it
# is going to be one distance greater than the rejection range
# of at least one beacon. Hopefully, this will be around the
# border of multiple rejection regions (or it is one of the
# corners). I would calculate the intersection(s), if existing,
# for each "border plus one" line segment, put these into a
# priority queue, and check if each candidate is inside a
# rejection region.
#
# There's possibly something wrong with my intersection code.
# I'll possibly use a third-party library to simplify this.
# If all of the candidate points are rejected (which the
# rejection code still needs to be implemented, TODO) then
# one thought is to include the nine surrounding points for
# every point, in case there's an off-by-one error somewhere.
#
# Once these changes are implemented, the solution should arrive.

manhattan = lambda v1, v2: abs(v2[0]-v1[0]) + abs(v2[1]-v1[1])
dist_to_2MM = lambda v: abs(v[1]-2000000)

class Endpoints:
    def __init__(self, sc, md):
        self.intop = (sc[0], sc[1] - md)
        self.inbot = (sc[0], sc[1] + md)
        self.inlef = (sc[0] - md, sc[1])
        self.inrig = (sc[0] + md, sc[1])
        self.area = 2 * md**2

        self.top = (sc[0], sc[1] - md - 1)
        self.bot = (sc[0], sc[1] + md + 1)
        self.lef = (sc[0] - md - 1, sc[1])
        self.rig = (sc[0] + md + 1, sc[1])

    def __str__(self):
        return f'Top: {self.top}, Left: {self.lef}, Bottom: {self.bot}, Right: {self.rig}, Area: {self.area}'

    def check_point_contained(self, pt):
        # There's this trick:
        #   1. Get the area of the existing region (done during class init)
        #   2. Get the area of the four triangles made by connecting each adjacent endpoint pair and candidate point.
        #   3. If these are equal(-ish), the point is contained. Otherwise, the point is outside the region.
        tri_area = lambda pA, pB, pC: abs((pA[0]*pB[1] + pB[0]*pC[1] + pC[0]*pA[1] - pA[1]*pB[0] - pB[1]*pC[0] - pC[1]*pA[0]) // 2)
        cand_area = tri_area(self.intop, self.inlef, pt) +\
                tri_area(self.intop, self.inrig, pt) +\
                tri_area(self.inbot, self.inrig, pt) +\
                tri_area(self.inbot, self.inlef, pt)
        return self.area == cand_area

    def _seg_inter(self, seg1, seg2):
        (p0, p1), (p2, p3) = seg1, seg2
        s10x = p1[0] - p0[0]
        s10y = p1[1] - p0[1]
        s32x = p3[0] - p2[0]
        s32y = p3[1] - p2[1]

        den = s10x * s32y - s32x * s10y

        if den == 0:
            return None  # Collinear

        is_pos = den > 0

        s02x = p0[0] - p2[0]
        s02y = p0[1] - p2[1]

        s = s10x * s02y - s10y * s02x
        if (s < 0) == is_pos:  return None
        t = s32x * s02y - s32y * s02x
        if (t < 0) == is_pos:  return None
        if (s > den) == is_pos or (t > den) == is_pos:  return None
        t /= den
        return tuple(map(int, (p0[0] + t*s10x, p0[1] + t*s10y)))

    def ccw(self,A,B,C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[1]-A[1])

    def isec(self,A,B,C,D):
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)

    def intersection(self, other):
        inter_list = []
        if r := self._seg_inter((self.top, self.lef), (other.top, other.lef)):  inter_list.append(r)  # UL vs UL
        if r := self._seg_inter((self.top, self.lef), (other.top, other.rig)):  inter_list.append(r)  # UL vs UR
        if r := self._seg_inter((self.top, self.lef), (other.bot, other.rig)):  inter_list.append(r)  # UL vs LR
        if r := self._seg_inter((self.top, self.lef), (other.bot, other.lef)):  inter_list.append(r)  # UL vs LL
        if r := self._seg_inter((self.top, self.rig), (other.top, other.lef)):  inter_list.append(r)  # UR vs UL
        if r := self._seg_inter((self.top, self.rig), (other.top, other.rig)):  inter_list.append(r)  # UR vs UR
        if r := self._seg_inter((self.top, self.rig), (other.bot, other.rig)):  inter_list.append(r)  # UR vs LR
        if r := self._seg_inter((self.top, self.rig), (other.bot, other.lef)):  inter_list.append(r)  # UR vs LL
        if r := self._seg_inter((self.bot, self.lef), (other.top, other.lef)):  inter_list.append(r)  # LR vs UL
        if r := self._seg_inter((self.bot, self.lef), (other.top, other.rig)):  inter_list.append(r)  # LR vs UR
        if r := self._seg_inter((self.bot, self.lef), (other.bot, other.rig)):  inter_list.append(r)  # LR vs LR
        if r := self._seg_inter((self.bot, self.lef), (other.bot, other.lef)):  inter_list.append(r)  # LR vs LL
        if r := self._seg_inter((self.bot, self.rig), (other.top, other.lef)):  inter_list.append(r)  # LL vs UL
        if r := self._seg_inter((self.bot, self.rig), (other.top, other.rig)):  inter_list.append(r)  # LL vs UR
        if r := self._seg_inter((self.bot, self.rig), (other.bot, other.rig)):  inter_list.append(r)  # LL vs LR
        if r := self._seg_inter((self.bot, self.rig), (other.bot, other.lef)):  inter_list.append(r)  # LL vs LL
        return inter_list

    def det(self, dx, dy):
        return dx[0] * dy[1] - dx[1] * dy[0]


v = ['',] * 10
x_reject_segs = []
endpoints_list = []
beacon = None
with open('input15', 'r') as file:
    for line in file:
        for i, word in enumerate(line.split()):
            v[i] = ''.join(n for n in word if n in '-0123456789')
        sx, sy, bx, by = map(int, (v[2], v[3], v[8], v[9]))
        s, b = (sx, sy), (bx, by)
        spread = manhattan(s, b)
        offset = dist_to_2MM(s)
        endpoints_list.append(Endpoints(s, spread))
        if offset > spread:
            continue  # Not in range
        rem = spread - offset  # Remaining x span
        x_reject_segs.append([s[0] - rem, s[0] + rem])

i_list = []
for i, e0 in enumerate(endpoints_list[:-1]):
    for j, e1 in enumerate(endpoints_list[i+1:], i+1):
        i_list.append(e0.intersection(e1))
flattened = [x for y in i_list for x in y]
flattened.sort()
for pt in flattened:
    if pt[0] < 0 or pt[1] < 0 or pt[0] > 4000000 or pt[1] > 4000000:
        continue
    if not any([e.check_point_contained(pt) for e in endpoints_list]):
        beacon = pt
        break

x_reject_segs.sort()
x_reject = [x_reject_segs[0]]

for seg in x_reject_segs:
    xr_tail = x_reject[-1]
    if seg[0] <= xr_tail[1]:
        xr_tail[1] = max(xr_tail[1], seg[1])
    else:
        x_reject.append(seg)

rejected = sum([e - s for s, e in x_reject])

print(f'Part A: {rejected}')
print(f'Part B: {4000000*beacon[0]+beacon[1]}')

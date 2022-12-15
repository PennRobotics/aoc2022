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
        self.top = (sc[0], sc[1] - md - 1)
        self.bot = (sc[0], sc[1] + md + 1)
        self.lef = (sc[0] - md - 1, sc[1])
        self.rig = (sc[0] + md + 1, sc[1])

    def __str__(self):
        return f'Top: {self.top}, Left: {self.lef}, Bottom: {self.bot}, Right: {self.rig}'

    def check_point_contained(self, pt):
        # There's this trick:
        #   1. Get the area of the top half triangle and bottom half triangle using four endpoints.
        #   2. Get the area of the four triangles made by connecting each adjacent endpoint pair and candidate point.
        #   3. If these are equal, the point is contained. Otherwise, the point is outside the region.

        # TODO
        pass

    def _seg_inter(self, seg1, seg2):
        (A,B),(C,D) = seg1, seg2
        if not self.isec(A,B,C,D):
            return None
        dx = (seg1[0][0] - seg1[1][0], seg2[0][0] - seg2[1][0])
        dy = (seg1[0][1] - seg1[1][1], seg2[0][1] - seg2[1][1])
        print((dx, dy))
        div = self.det(dx, dy)
        print(div)
        if div == 0:
            return None
        d = (self.det(*seg1), self.det(*seg2))
        x = self.det(d, dx) // div
        y = self.det(d, dy) // div
        return (x, y)

    def ccw(self,A,B,C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[1]-A[1])

    def isec(self,A,B,C,D):
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)

    def intersection(self, other):
        inter_list = []
        r = self._seg_inter((self.top, self.lef), (other.top, other.lef))  # UL vs UL
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.top, self.lef), (other.top, other.rig))  # UL vs UR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.top, self.lef), (other.bot, other.rig))  # UL vs LR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.top, self.lef), (other.bot, other.lef))  # UL vs LL
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.top, self.rig), (other.top, other.lef))  # UR vs UL
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.top, self.rig), (other.top, other.rig))  # UR vs UR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.top, self.rig), (other.bot, other.rig))  # UR vs LR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.top, self.rig), (other.bot, other.lef))  # UR vs LL
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.lef), (other.top, other.lef))  # LR vs UL
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.lef), (other.top, other.rig))  # LR vs UR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.lef), (other.bot, other.rig))  # LR vs LR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.lef), (other.bot, other.lef))  # LR vs LL
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.rig), (other.top, other.lef))  # LL vs UL
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.rig), (other.top, other.rig))  # LL vs UR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.rig), (other.bot, other.rig))  # LL vs LR
        if r:
            inter_list.append(r)
        r = self._seg_inter((self.bot, self.rig), (other.bot, other.lef))  # LL vs LL
        if r:
            inter_list.append(r)
        return inter_list

    def det(self, dx, dy):
        return dx[0] * dy[1] - dx[1] * dy[0]


v = ['',] * 10
x_reject_segs = []
endpoints_list = []
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
        print('---')
        print((i,j))
        print(e0)
        print(e1)
        i_list.append(e0.intersection(e1))
flattened = [x for y in i_list for x in y]
flattened.sort()
for pt in flattened:
    print(pt)

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
print(f'Part B: {0}')

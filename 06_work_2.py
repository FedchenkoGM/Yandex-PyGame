def intersect(p11, p12, p21, p22):
    return p11 <= p21 <= p12 or p21 <= p11 <= p22


x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())
print('YES' if intersect(x1, x1 + w1, x2, x2 + w2) and intersect(y1, y1 + h1, y2, y2 + h2) else 'NO')
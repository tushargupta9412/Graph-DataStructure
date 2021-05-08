import math

mod = (10 ** 9) + 7
maxn = (10 ** 5) + 7

tree = [[0, 1] for i in range(4*maxn)]
v = [0]


def build(node, start, end):
    if start == end:
        tree[node][0] = math.log10(float(v[start]))
        tree[node][1] = v[start]
        # print(tree[node][1])

    else:
        mid = (start + end) // 2
        left = (2 * node) + 1
        right = (2 * node) + 2
        build(left, start, mid)
        build(right, mid+1, end)

        tree[node][0] = tree[left][0] + tree[right][0]
        tree[node][1] = (tree[left][1] * tree[right][1]) % mod


def update(node, start, end, idx, val):
    if start == end:
        v[idx] = val
        tree[node][0] = math.log10(float(v[idx]))
        tree[node][1] = v[idx]
    else:
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        if start <= idx <= mid:
            update(left, start, mid, idx, val)
        else:
            update(right, mid + 1, end, idx, val)
        tree[node][0] = tree[left][0] + tree[right][0]
        tree[node][1] = (tree[left][1] * tree[right][1]) % mod


def query(node, start, end, l, r):
    if r < start or end < l:
        return [0, 1]
    if l <= start and end <= r:
        return tree[node]

    mid = (start + end) // 2
    left = 2 * node + 1
    right = 2 * node + 1

    p1 = query(left, start, mid, l, r)
    p2 = query(right, mid + 1, end, l, r)

    res = [p1[0] + p2[0], (p1[1] * p2[1]) % mod]

    return res


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    v = x
    build(0, 0, n - 1)
    print(v)
    print(tree)
    for i in range(int(input())):
        o = list(map(int,input().split()))
        if o[0] == 1:
            update(0, 0, n-1, o[1], o[2])
        else:
            t = query(0, 0, n-1, o[1]-1, o[2]-1)

            dig = int(10**(t[0]-math.floor(t[0])))
            print(t[1], dig)

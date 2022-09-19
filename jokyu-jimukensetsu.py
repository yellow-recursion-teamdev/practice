from collections import deque

def largestRectangle(h):
    # 関数を完成させてください
    ans = -1
    for width in range(1, len(h)+1):
        d = deque()
        for i in range(width):
            while len(d) != 0 and h[i] < h[d[-1]]:
                d.pop()
            d.append(i)
        area = h[d[0]] * width
        ans = max(area, ans)
        for i in range(width, len(h)):
            if d[0] + width <= i:
                d.popleft()
            while len(d) != 0 and h[i] < h[d[-1]]:
                d.pop()
            d.append(i)
            print(i, width, h[d[0]], d)
            area = h[d[0]] * width
            ans = max(area, ans)
    return ans


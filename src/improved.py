def max_area(height):
    max_area = 0
    n = len(height)

    l = 0
    r = n - 1
    while(l < r):
        max_area = max(max_area, (r - l) * min(height[r], height[l]))
        if(height[l] <= height[r]):
            l = l + 1
        else:
            r = r - 1
    return max_area

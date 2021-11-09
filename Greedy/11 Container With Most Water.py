def maxArea(self, height):
    """
    11. Container With Most Water
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
    lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together
    with the x-axis forms a container, such that the container contains the most water.
    Notice that you may not slant the container.

    :param self:
    :param height:
    :return:
    """
    left=0
    right=len(height)-1
    result=0
    while left<right:
        result=max(result,(right-left)*min(height[left],height[right]))
        if  height[left]<height[right]:
            left+=1
        else:
            right-=1
    
    return result
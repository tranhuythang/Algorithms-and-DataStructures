"""
* Problem: 735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving
in the same direction will never meet.
Example 1: Input: asteroids = [5,10,-5] -> Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2: Input: asteroids = [8,-8] -> Output: []
Explanation: The 8 and -8 collide exploding each other.
* Algorithm: Using stack
Create a stack, for each current_asteroid in the input row:
 while the current_asteroid < 0 < the stack's top there will be collision.
    + if top > - current_asteroid: move to the next asteroid
    + if top = - current_asteroid: pop the stack's top and move to the next asteroid
    + if top < - current_asteroid: pop the stack's top and push the current_asteroid to the stack
* Time-complexity: in the worst case O(n)
* Space-complexity: in the worst case O(n)
"""
import collections
def asteroidCollision(asteroids):
    stack = collections.deque()
    for current_asteroid in asteroids:
        while len(stack) > 0 and stack[-1] > 0 > current_asteroid:
            if stack[-1] == - current_asteroid:
                stack.pop()
                break
            elif stack[-1] > - current_asteroid:
                break
            else:
                stack.pop()
        else:
            stack.append(current_asteroid)
    return list(stack)






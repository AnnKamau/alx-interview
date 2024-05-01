#!/usr/bin/python3
"""
Write a method that determines if all the boxes can be opened.
"""
def canUnlockAll(boxes):
    """
    Lockboxes

    Arguments:
    n (int): number of locked boxes in front of you

    Return:
    True if all boxes can be opened, else return False
    """
    
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

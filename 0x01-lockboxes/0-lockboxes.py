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
  if not boxes:
    return False
  
  keys = set([0])
  new_keys = set([0])

  while new_keys:
    next_keys = set()
    for key in new_keys:
      next_keys.update(set(boxes[key]) - keys)
    keys.update(new_keys)
    new_keys = next_keys - keys

  return len(keys) == len(boxes)

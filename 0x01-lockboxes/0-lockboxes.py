#!/usr/bin/python3
"""
Lockboxes
"""
def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    opened = set([0])
    keys = [0]  

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in opened and key < n:
                opened.add(key)
                keys.append(key)

    return len(opened) == n

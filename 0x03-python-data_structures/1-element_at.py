#!/usr/bin/python3
def element_at(mylist, idx):
    if idx < 0:
        return (None)
    if len(mylist) < idx:
        return (None)

    return (mylist[idx])

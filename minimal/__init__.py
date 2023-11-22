def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y

def ternas(n):
    t= []
    for x in range(1,n):
      for y in range(x+1,n):
        for z in range(y+1,n):
          if x**2+y**2== z**2:
            t.append((x,y,z))
    return t

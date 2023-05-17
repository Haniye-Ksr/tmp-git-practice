import numpy as np

from utils import add

print(add(3,4))
print('Branch master!')

def main():
    a = 10
    b = 20
    c = add(a,b)
    print(c)

if __name__ == '__main__':
    main()
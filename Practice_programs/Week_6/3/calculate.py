import sys
from shapes import area

if sys.argv[1] == 'circle':
    print(area.circle(float(sys.argv[2]) if len(sys.argv) == 3 else 'incorrect no. of args'))
elif sys.argv[1] == 'rect':
    print(area.rect(float(sys.argv[2]), float(sys.argv[3])) if len(sys.argv) == 4 else 'incorrect no. of args')
elif sys.argv[1] == 'tri':
    print(area.rect(float(sys.argv[2]), float(sys.argv[3])) if len(sys.argv) == 5 else 'incorrect no. of args')

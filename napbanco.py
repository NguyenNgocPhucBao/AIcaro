import numpy
from caro import caro

def naphinhco(cr):
    f = open("banco.txt", "r")
    data = f.readlines()
    f.close()

    diagram = []
    for i in data:
        i = i.split()
        for j in range(len(i)):
            i[j] = int(i[j])
        diagram.append(i)

    print(numpy.array(diagram))

    cr.load_diagram(diagram)
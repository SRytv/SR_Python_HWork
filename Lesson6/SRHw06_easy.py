# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class Polygon:
#примает, хранит и обрабатывает координаты вершин многоугольника
#в виде кортежей (x,y),
#  начиная от первой самой левой и нижней и далее по часовой чтрелке
    polygon_vertices = ()
    def __init__(self, *vertices):
        #сохранение координат вершин многоугльника
        self.polygon_vertices = vertices
        print ('0 -', self.polygon_vertices, len(self.polygon_vertices))

    def sidesize(self, vert1, vert2):
        #print('Ptint_A - ', vert1, vert2)
        #вычисление длины стороны многоугольнка между вершинами 1 и 2
        #vetr1, vetr2, кординаты вершин 1 и 2 в виде (x,y)
        #print ('print_B', math.sqrt((vert1[0]-vert2[0])**2 + (vert1[1] - vert2[1])**2))
        return math.sqrt((vert1[0]-vert2[0])**2 + (vert1[1] - vert2[1])**2)

    def polygon_perimeter(self):
        self.perimeter = 0
        vetr_numb = len(self.polygon_vertices)
        print ('Ptint_C - ', vetr_numb)
        for i in range(vetr_numb-1):
            self.perimeter += Polygon.sidesize(self, self.polygon_vertices[0], self.polygon_vertices[i])
            self.perimeter += Polygon.sidesize(self, self.polygon_vertices[i], self.polygon_vertices[i+1])
        perimetr += Polygon.sidesize(self, self.polygon_vertices[vetr_numb], self.polygon_vertices[0])
        print ('print_0', self.perimeter, self.polygon_vertices[0])
        return self.perimeter

class Triangle(Polygon):
    side1 = 0
    side2 = 0
    side3 = 0
    def triangle_area(self):
        # вычисление площади треугольника по формуле Герона
        half_perimeter = Polygon.polygon_perimeter(self)/2
        self.side1 = Polygon.sidesize(self, self.polygon_vertices[0], self.polygon_vertices[1])
        self.side2 = Polygon.sidesize(self, self.polygon_vertices[1], self.polygon_vertices[2])
        self.side3 = Polygon.sidesize(self, self.polygon_vertices[2], self.polygon_vertices[0])
        return math.sqrt(half_perimeter*(half_perimeter-side1)*(half_perimeter-side2)*(half_perimeter-side3))

    def triangl_height(self):
        return (self.triangle_area*2)/self.side1

#============================================================================================================
class Isosceles_Tapezoid(Polygon):
    side1 = 0 # левая боковая сторна
    side2 = 0 # верхнее основание
    side3 = 0 # правая боковая сторона
    side4 = 0 # нижнее основание
    area  = 0
    hight = 0
    Tapezoid_perimeter = 0
    self.side1 = Polygon.sidesize(self, self.polygon_vertices[0], self.polygon_vertices[1])
    self.side2 = Polygon.sidesize(self, self.polygon_vertices[1], self.polygon_vertices[2])
    self.side3 = Polygon.sidesize(self, self.polygon_vertices[2], self.polygon_vertices[3])
    self.side4 = Polygon.sidesize(self, self.polygon_vertices[3], self.polygon_vertices[0])
    if self.side1  != self.side3:
        check = False

    else:
        check= True
        self.Tapezoid_perimeter = Polygon.polygon_perimeter(self)
        self.area = ((self.side2+self.side4)/2)* math.sqrt(self.side1**2 - ((self.side2 - self.side4)**2)/4)
        self.hight = self.area / ((self.side2+self.side4)/2)



if __name__ == '__main__':
    tri1 = Triangle((0,0),(3,4),(6,0),)
    print (tri1.polygon_perimeter, tri1.triangle_area, tri1.triangl_height)
    #IsoTrap = Isosceles_Tapezoid((0,0), (3,4), (9,4), (12,0),)
    #print(IsoTrap.area, IsoTrap.hight, IsoTrap.area.Tapezoid_perimeter)




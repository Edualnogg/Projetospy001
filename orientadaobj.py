class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def sum_triangle(self):
        return self.angle1 + self.angle2 + self.angle3

    def check_angles(self):
        if(self.triangle() == 180):
            return True
        else:
            return False

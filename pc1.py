import unittest
import math

class XYPolar:
    def __init__(self):
        pass
    def polartoc(self,r,t):
        x = round(r*math.cos(t),2)
        y = round(r*math.sin(t),2)
        return (x,y)

    def ctopolar(self,x,y):
        r = round(math.sqrt(x*x + y*y),2)
        t = math.asin(y/r)
        return (r,t)

class testeo(unittest.TestCase):
    def test_polartoc(self):
        complejo = XYPolar()        
        xy = complejo.polartoc(4*math.sqrt(2),math.pi/4)
        xyresul = (4,4)
        self.assertEqual(xy,xyresul, "Funciona")

    def test_ctopolar(self):
        complejo = XYPolar()        
        polar = complejo.ctopolar(1,math.sqrt(3))        
        polarresul = (2,math.pi/3)
        self.assertEqual(polar,polarresul, "Funciona")

if __name__ == '__main__':
    unittest.main()

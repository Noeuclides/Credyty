from math import sin, cos, pi, radians, pi

def pitagorasTriplet():
    """
    Method to get the Pythagorean Triplet such that a +b + c = 1000.
    Base on the Pythagoras Theorem.
    """
    angle = 5

    for c in range(334, 500):
        #round function to get a 'integer' number
        a = round(c * sin(radians(angle)))
        b = round(c * cos(radians(angle)))

        while a < b < c:
            #Check for Pythagoras Theorem
            if a ** 2 + b ** 2 == c ** 2:
                if a + b + c == 1000:
                    print("a = {}".format(a))
                    print("b = {}".format(b))
                    print("c = {}".format(c))
                    print("Triplet Angle: {}".format(angle))
                    print("{}^2 + {}^2 = {}^2 => {} + {} = {}".format(a, b, c, a**2, b**2, c**2))                    
                    return("Product a*b*c = {}".format(a*b*c))
        
            angle += 1
            a = round(c * sin(radians(angle)))
            b = round(c * cos(radians(angle)))

        angle = 5



pitagoras = pitagorasTriplet()
print(pitagoras)
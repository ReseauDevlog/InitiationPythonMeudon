class A:
    def x(self):
        print("<A>")
        print("</A>")
    
class B1(A):
    def x(self):
        print("<B1>")
        super().x()
        print("</B1>")

class B2(A):
    def x(self):
        print("<B2>")
        super().x()
        print("</B2>")
    
class C(B1,B2):
    def x(self):
        print("<C>")
        super().x()
        print("</C>")

c = C()
c.x()

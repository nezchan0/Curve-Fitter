import numpy as np
class solving_eq():
    def Straight_line(self,Val):
        self.A=[[Val[1],Val[0]],[Val[3],Val[1]]]
        self.B=[Val[2],Val[4]]
        self.G=np.linalg.inv(self.A).dot(self.B)
        self.ABC=[self.G[0],self.G[1],self.G[1]]
        return self.ABC
    def Parabola_eq(self,Val):
        self.A=[[Val[3],Val[1],Val[0]],[Val[4],Val[3],Val[1]],[Val[5],Val[4],Val[3]]]
        self.B=[Val[2],Val[6],Val[7]]
        self.G=np.linalg.inv(self.A).dot(self.B)
        return self.G
    def Geometric_eq(self,Val):
        self.A=[[Val[0],Val[1]],[Val[1],Val[3]]]
        self.B=[Val[2],Val[4]]
        self.G=np.linalg.inv(self.A).dot(self.B)
        self.G[0]=np.exp(self.G[0])
        self.ABC=[self.G[0],self.G[1],0]
        return self.ABC


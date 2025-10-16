import matplotlib.pyplot as plt
import numpy as np

class MakingGraph():
    def __init__(self,x_coordinates,y_coordinates):
        self.size=x_coordinates.size
        self.x_coordinates=x_coordinates
        self.y_coordinates=y_coordinates
    def Plotting_straightLine(self,ABval):
        self.x=np.linspace(0,self.x_coordinates[self.size-1],30)
        self.y=ABval[0]*self.x+ABval[1]

        equation="y = "+str(round(ABval[0],4))+"x + "+str(round(ABval[1],4))
        plt.text(0,self.y[27], equation,fontsize = 11, style='italic', bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad':3})
        plt.scatter(self.x_coordinates,self.y_coordinates,color = '#ff0000')
        plt.grid(color = 'green', linestyle = '--')
        plt.plot(self.x,self.y)
        plt.title("Curve Fitting: Straight Line")
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.show()
    def Plotting_Parabola(self,ABCval):
        self.x=np.linspace(0,self.x_coordinates[self.size-1],30)
        self.y=ABCval[0]*(self.x**2)+ABCval[1]*self.x+ABCval[2]

        equation="$y = "+str(round(ABCval[0],4))+"x^2$ + "+str(round(ABCval[1],4))+"x + "+str(round(ABCval[2],4))
        plt.text(0,self.y[27], equation,fontsize = 11, style='italic', bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad':3})
        plt.scatter(self.x_coordinates,self.y_coordinates,color = '#ff0000')
        plt.grid(color = 'green', linestyle = '--')
        plt.plot(self.x,self.y)
        plt.title("Curve Fitting: Parabola")
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.show()
    def Plotting_GeomwtriCurve(self,ABval):
        self.x=np.linspace(0,self.x_coordinates[self.size-1],30)
        self.y=ABval[0]*(self.x**ABval[1])
      
        equation="y= "+str(round(ABval[0],4))+"x^("+str(round(ABval[1],4))+")"
        plt.text(0,self.y[27], equation,fontsize = 11, style='italic', bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad':3})
        plt.scatter(self.x_coordinates,self.y_coordinates,color = '#ff0000')
        plt.grid(color = 'green', linestyle = '--')
        plt.plot(self.x,self.y)
       
        plt.title("Curve Fitting: Geometric Curve")
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.show()
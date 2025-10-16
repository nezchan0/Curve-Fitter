import numpy as np
import pandas as pd
class table_values():
    def __init__(self,x,y):
        self.x=np.array(x)
        self.y=np.array(y)
        self.size=self.x.size
        self.sum_x=np.sum(self.x)
        self.sum_y=np.sum(self.y)
    def For_straight_line(self):
        self.x2=self.x**2
        self.xy=self.x*self.y
        self.sum_x2=np.sum(self.x2)
        self.sum_xy=np.sum(self.xy)

        data={
            "x":self.x,
            "y":self.y,
            "x\u00b2":self.x2,
            "xy":self.xy
        }
        
        df=pd.DataFrame(data,index=np.array(range(1,self.size+1)))
        df.loc["Sum->"]=[self.sum_x,self.sum_y,self.sum_x2,self.sum_xy]
        df.index.name="Index" 
        print("---------Curve Fitting: Straight Line---------\n")
        print(df)

        Values=[self.size,self.sum_x,self.sum_y,self.sum_x2,self.sum_xy]
        return Values
    def For_parabola(self):
        self.x2=self.x**2
        self.x3=self.x**3
        self.x4=self.x**4
        self.xy=self.x*self.y
        self.x2y=self.x2*self.y
        self.sum_x2=np.sum(self.x2)
        self.sum_x3=np.sum(self.x3)
        self.sum_x4=np.sum(self.x4)
        self.sum_xy=np.sum(self.xy)
        self.sum_x2y=np.sum(self.x2y)

        data={
            "x":self.x,
            "y":self.y,
            "x\u00b2":self.x2,
            "x\u00b3":self.x3,
            "x\u00b4":self.x4,
            "xy":self.xy,
            "x\u00b2y":self.x2y
        }
        df=pd.DataFrame(data,index=np.array(range(1,self.size+1)))
        df.loc["Sum->"]=[self.sum_x,self.sum_y,self.sum_x2,self.sum_x3,self.sum_x4,self.sum_xy,self.sum_x2y]
        df.index.name="Index" 
        print("------------------Curve Fitting: Parabola-----------------\n")
        print(df)

        Values=[self.size,self.sum_x,self.sum_y,self.sum_x2,self.sum_x3,self.sum_x4,self.sum_xy,self.sum_x2y]
        return Values
    def For_geometriCurve(self):
        self.logx=np.log(self.x)
        self.logy=np.log(self.y)
        self.logx2=self.logx**2
        self.logxlogy=self.logx*self.logy
        self.sum_logx=np.sum(self.logx)
        self.sum_logy=np.sum(self.logy)
        self.sum_logx2=np.sum(self.logx2)
        self.sum_logxlogy=np.sum(self.logxlogy)

        data={
            "x":self.x,
            "y":self.y,
            "log(x)":self.logx,
            "log(y)":self.logy,
            "(log(x))\u00b2":self.logx2,
            "log(x).log(y)":self.logxlogy
        }
        df=pd.DataFrame(data,index=np.array(range(1,self.size+1)))
        df.loc["Sum->"]=[self.sum_x,self.sum_y,self.sum_logx,self.sum_logy,self.sum_logx2,self.sum_logxlogy]
        df.index.name="Index" 
        print("------------------Curve Fitting: Geometric Curve------------------\n")
        print(df)

        Values=[self.size,self.sum_logx,self.sum_logy,self.sum_logx2,self.sum_logxlogy]
        return Values
        

    
from . import class_for_for_getting_table_values
from . import class_for_solving_equations
from . import class_for_plotting_graph

class Calling_():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Calling_StraightLine(self):
        object1=class_for_for_getting_table_values.table_values(self.x,self.y)
        TableValues=object1.For_straight_line()
        
        object2=class_for_solving_equations.solving_eq()
        ABvalues=object2.Straight_line(TableValues)

        object3=class_for_plotting_graph.MakingGraph(self.x,self.y)
        object3.Plotting_straightLine(ABvalues)
    def Calling_Parabola(self):
        object1=class_for_for_getting_table_values.table_values(self.x,self.y)
        TableValues=object1.For_parabola()
        
        object2=class_for_solving_equations.solving_eq()
        ABvalues=object2.Parabola_eq(TableValues)

        object3=class_for_plotting_graph.MakingGraph(self.x,self.y)
        object3.Plotting_Parabola(ABvalues)
    def Calling_GeometicCurve(self):
        object1=class_for_for_getting_table_values.table_values(self.x,self.y)
        TableValues=object1.For_geometriCurve()
        
        object2=class_for_solving_equations.solving_eq()
        ABvalues=object2.Geometric_eq(TableValues)
    
        object3=class_for_plotting_graph.MakingGraph(self.x,self.y)
        object3.Plotting_GeomwtriCurve(ABvalues)

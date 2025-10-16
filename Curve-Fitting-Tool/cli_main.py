## THIS IS A CLI TOOL

import curve_fitter.class_for_calling as cc
import numpy as np

print("\nEnter the Values of the X and Y coordinates ")

x=np.array(list(map(float, input("X values: ").split())))
y=np.array(list(map(float, input("Y values: ").split())))

if(x.size!=y.size):
    print("Enter equal number of values for X and Y values")
    exit()

object=cc.Calling_(x,y)

while(True):
    print("\n")
    print("Enter the type of curve you want to fit for the given data: ")
    print("Press 1: Straight Line")
    print("Press 2: Parabola")
    print("Press 3: Geometric Curve")
    print("Press 123: To Exit")
    choice=int(input("\nEnter your choice: "))
    print("\n")

    match choice:
        case 1:
            object.Calling_StraightLine()

        case 2:
           object.Calling_Parabola()

        case 3:
           object.Calling_GeometicCurve()

        case 123:
            print("\n ******Exiting*******\n")
            break
        case default:
            print("Invalid choice. Enter valid Choice")


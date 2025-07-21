# def greet():
#     print("hello")
#     print("hello")
#     print("hello")
# greet()
#
# # function with parameter
# def withname(name) :
#     print(f"welcome {name}")
# withname("abinesh")
#
# # function with multiple parameters
# def address(name,location):
#     print(f"your name {name} and your location is {location}")
#
# address("abinesh","aralvaimozhi")
#

# calculate the number of can need for the wall
def calofpaint(h,w):
    Area=h*w
    numofcan=round(Area/5)
    print(f"the {numofcan} can need for cover the area")

h=int(input("enter the height of the wall"))
w=int(input("enter the width of the wall"))
calofpaint(h,w)

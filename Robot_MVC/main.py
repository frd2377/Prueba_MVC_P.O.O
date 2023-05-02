#FRD
from model import Robot
from controller import Robot_Controller
from view import Robot_View

robot = Robot([0,0,0],[0,0,0])
view = Robot_View()
controller = Robot_Controller(robot,view)
view.controller = controller
view.main()






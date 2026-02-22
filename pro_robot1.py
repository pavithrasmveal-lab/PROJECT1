class World:
    def __init__(self, x, y, direction,battery):
        self.x=x
        self.y=y
        self.direction=direction
        self.battery=battery
    def rotatet(self):
        direction=["N","E","S","W"]
        idx=direction.index(self.direction)
        self.direction=direction[(idx+1)%4]
        print(f"The robot rotate right and in direction {self.direction}")
    def rotatel(self):
        direction=["N","E","S","W"]
        idx=direction.index(self.direction)
        self.direction=direction[(idx-1)%4]
        print(f"The robot rotate right and in direction {self.direction}")
    def movement(self,n) :
        new_x,new_y=self.x,self.y
        for i in range(abs (n)):
            if(self.battery==0):
                print("No battery")
                break;
            if(n>0):
                if(self.direction=="N" and self.battery!=0):
                    new_y+=1
                elif(self.direction=="S"and self.battery!=0):
                    new_y-=1
                elif(self.direction=="E"and self.battery!=0):
                    new_x+=1
                elif(self.direction=="W"and self.battery!=0):
                    new_x-=1
            if(n<0):
                if(self.direction=="N"and self.battery!=0):
                    new_y-=1 
                elif(self.direction=="S"and self.battery!=0): new_y+=1
                elif(self.direction=="E"and self.battery!=0): new_x-=1 
                elif(self.direction=="W"and self.battery!=0): new_x+=1
            if((0<=new_x<=1000) and (0<=new_y<=1000)):  
                self.x=new_x 
                self.y=new_y
                self.battery-=1
                print(f"The robot move forward and current position {self.x}, {self.y} and in direction {self.direction} and battery is{self.battery}")
            else:
                print("Movemnt blocked")
                break;
    def charge(self):
        self.battery=100
        print("Battery full")

run=True
while(run):
    
    print("Toy Robot Simulator")
    print("1) Place robot")
    print("2) Move (forward/back)")
    print("3) Rotate (left/right) ")
    print("4) Charge battery ")
    print("5) Report status ")
    print("8) Exit")
    choice=int(input("Enter:"))
    if(choice==1):
        print("Initial x,y coordinate ,direction,battery") 
        a=int(input("Enter x(width):"))
        b=int(input("Enter y(height):")) 
        c=input("Enter direction (in this format'A'):")
        d=int(input("Enter battery level:"))
        w1=World(a,b,c,d)
        
    elif (choice==2): 
        a=int(input("Enter forward(1) or backward((2):"))
        if(a==1):
            b=int(input("Enter no of steps:")) 
            w1.movement(b)
        if(a==2):
            b=int(input("Enter no of steps(negnative):"))
            w1.movement(b)
    elif(choice==3): 
        a=int(input("Enter left(1) or right(2)")) 
        if(a==1): 
            w1.rotatel() 
        if(a==2): 
            w1.rotatet() 
    elif(choice==4):
        print(f"The current battery is {w1.battery}") 
    elif(choice==5): 
        print(f"The position is {w1.x} and {w1.y} and direction is [{w1.direction} and battery of{w1.battery}") 
    elif(choice==8):
        print("exit")
        run=False
               


# Print the details of a movie by getting various arbitrary keyword
# arguments
def myFunction(**movies):
    print("The movie name is " + movies["moviename"] + " and the actor is " + movies["actor"])


myFunction(moviename="A box of faith", actor="Tony")
myFunction(moviename="A box of success", actor="Stark")
myFunction(moviename="A box of joy", actor="Tony Stark")
myFunction(moviename="A box of compassion", actor="Stark Tony")

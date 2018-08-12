import AppIface
from Todo import Todo

def start():
    #fileobj = open("a.txt", "w")
    #print type(fileobj)
    app = Todo()
    app.start()
    app.stop()

if __name__ == "__main__":
    start()
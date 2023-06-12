# Modules
import eel # For GUI


# main() function will be in threads in order to run the eel and this function in async
def main():
    eel.window_ready()()

# Validation that the code is ran from this file
if __name__ == "__main__":
    eel.spawn(main)
    eel.init("app")
    eel.start('tasks.html', port=20171, size=(1440, 950))

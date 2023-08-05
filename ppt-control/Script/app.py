from function_module import *
from GUI import *

def main()->None:
    '''
    The main function
    '''
    root = tk.Tk()
    app = GUI(master=root)
    app.mainloop()
    return None

if __name__ == "__main__":
    main()
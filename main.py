import River
#This is a library for the GUI i have used for output
import tkinter as tk

# THe GUI Window
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (800, 600, 0, 0))
# the title of the window
root.title("The River Problem                    Name: Bikal Lamichhane ID: 1481000 ©")
# The label for the north shore and the south shore in row 0 and row 2 from the grid layout
label = tk.Label(root, text = "Please choose the state for the South shore and North Shore")
label.grid(row=0,columnspan=4)
indexL = tk.Label(root, text = "Index:: F-Farmer, W-Wolf, D-Duck, C-Cabbage ")
indexL.grid(row=1,columnspan=4)
label_1 = tk.Label(root, text = "The South Shore")
label_1.grid(row=2)
label_2 = tk.Label(root, text = "The North Shore")
label_2.grid(row=4)
#using the option menu for choosing the states
# The options for the states of north shore and south shore in row 1 and row 3
sOptions1 = tk.StringVar(root)
sOptions1.set('F')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, sOptions1, *choices)
option.grid(row=3, column=0)

sOptions2 = tk.StringVar(root)
sOptions2.set('W')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, sOptions2, *choices)
option.grid(row=3, column=1)

sOptions3 = tk.StringVar(root)
sOptions3.set('D')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, sOptions3, *choices)
option.grid(row=3, column=2)

sOptions4 = tk.StringVar(root)
sOptions4.set('C')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, sOptions4, *choices)
option.grid(row=3, column=3)

# options for the north shore
nOptions1 = tk.StringVar(root)
nOptions1.set('')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, nOptions1, *choices)
option.grid(row=5, column=0)

nOptions2 = tk.StringVar(root)
nOptions2.set('')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, nOptions2, *choices)
option.grid(row=5, column=1)

nOptions3 = tk.StringVar(root)
nOptions3.set('')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, nOptions3, *choices)
option.grid(row=5, column=2)

nOptions4 = tk.StringVar(root)
nOptions4.set('')
choices = ['F','W','D','C','']
option = tk.OptionMenu(root, nOptions4, *choices)
option.grid(row=5, column=3)

# This is the text field where the ouput can be seen
T = tk.Text(root,height =50, width=100)
T.grid(row=7,columnspan=4)




#initializing the river problem to the state
# provided by the user in the GUI




#This function finds the path taken to get to the goal node
def path_finder(iter,RP):
    path = []
    initial = RP
    path.append(iter)
    p = iter.parent
    path.append(p)
    while not(p==initial):
        p = p.parent
        path.append(p)
    return path



# This function is for printing the path towards the goal node
def printWindow():
    # Exception Handler to handle errors
    try:
        counter = 0
        RP = River.State([sOptions1.get(), sOptions2.get(), sOptions3.get(), sOptions4.get()],
                         [nOptions1.get(), nOptions2.get(), nOptions3.get(), nOptions4.get()])
        iter = River.BFS(RP)
        Path = path_finder(iter,RP)
        # the statement below clears the screen before printing anything
        # to the output window
        T.delete('1.0','end')
        final = River.State(['','','',''],['F','W','D','C'])

        for i in reversed(Path):
            i.sShore = list(set(i.sShore))
            i.nShore = list(set(i.nShore))
            i.sShore.sort()
            i.nShore.sort()
            i.sShore = list(i.sShore)
            i.nShore = list(i.nShore)
            T.insert('end','South Shore::')
            T.insert('end', i.sShore)
            T.insert('end', '\t\t\t\t\t\t\tNorth Shore::')
            T.insert('end',i.nShore)
            T.insert('end','\n')

            if not(i==final):
                if 'F' in i.sShore:
                    T.insert('end',"\t\t>>>----------------\_/--------- To North->>>")
                if 'F' in i.nShore:
                    T.insert('end',"\t\t<<<-------To South----------\_/----------<<<")
            T.insert('end','\n')
    except AttributeError:
        T.delete('1.0', 'end')
        T.insert('end','Please input valid state')
    except TypeError:
        T.delete('1.0', 'end')
        T.insert('end','Please input valid state')

#Button for finding the solution
button = tk.Button(root, text="Find the solution!!", command=printWindow)
button.grid(row=6, columnspan=4)


root.mainloop()
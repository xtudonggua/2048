from tkinter import *
import logic

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }
FONT = ("Verdana", 40, "bold")

class Chess(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("2048")
        self.master.bind("<Key>", self.key_down)

        self.commands = { 
                "'w'":"up", "'s'":"down", "'a'":"left", "'d'":"right",
            }
        self.over = False

        self.grid()
        self.grid_cells = []
        self.init_grid()

        self.matrix = logic.init_matrix()

        self.update()
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()
        self.background = background
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE/GRID_LEN, height=SIZE/GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def update(self): #matrix=[4][4]
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                n = self.matrix[i][j]
                t = self.grid_cells[i][j]
                if n==0:
                    self.grid_cells[i][j].config(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].config(text=str(n), bg=BACKGROUND_COLOR_DICT[n], fg=CELL_COLOR_DICT[n])

    def key_down(self, event):
        if self.over: return
        key = repr(event.char)
        if key in self.commands:
            done = logic.move(self.matrix, self.commands[key])
            if done:
                logic.add_new(self.matrix)
                self.update()
                if logic.is_win(self.matrix):
                    self.over = True
                    result = Label(master=self.background, text="You Win", height=2)
                    result.grid()
                elif logic.game_over(self.matrix):
                    self.over = True
                    result = Label(master=self.background, text="Game Over", height=2)
                    result.grid()



def main():
    chess = Chess()
    
if __name__=="__main__":
    main()

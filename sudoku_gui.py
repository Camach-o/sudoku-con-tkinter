from tkinter import *
from board_gestore import *

class SudokuGui(Tk, LogicalBoard):
    def __init__(self):

        # root
        self.windows = Tk()
        self.windows.title("Sudoku Game")
        self.windows.resizable(0, 0)

        # background
        self.back_frame = Frame(self.windows)
        self.back_frame.pack()
        self.start_menu_img = PhotoImage(file="image.png")

        # menu
        self.menu_bar = Menu(self.windows)
        self.windows.config(menu=self.menu_bar)
        self.difficulties = Menu(self.menu_bar, tearoff=0)
        self.difficulties.add_command(label="Fácil", command=lambda: self.create_board(1))
        self.difficulties.add_command(label="Medio", command=lambda: self.create_board(2))
        self.difficulties.add_command(label="Difícil", command=lambda: self.create_board(3))
        self.difficulties.add_command(label="Inicio", command=self.start_menu)
        self.menu_bar.add_cascade(label="Dificultades", menu=self.difficulties)

    def start_menu(self):
        self.back_frame.destroy()
        self.back_frame = Frame(self.windows)
        self.back_frame.pack()

        self.bground = Label(self.back_frame, image=self.start_menu_img)
        self.bground.pack()

        easy_button = Button(self.bground, width=10, font=("Alexandria", 15), 
                             text="Fácil", command=lambda: self.create_board("20"))
        easy_button.place(x=35, y=60)

        medium_button = Button(self.bground, width=10, font=("Alexandria", 15), 
                               text="Medio", command=lambda: self.create_board(30))
        medium_button.place(x=35, y=160)
        
        hard_button = Button(self.bground, width=10, font=("Alexandria", 15), 
                             text="Difícil", command=lambda: self.create_board(40))
        hard_button.place(x=35, y=260)

    def create_board(self, dificulty):

        box_frame_list = []
        box_list = []

        self.back_frame.destroy()
        self.back_frame = Frame(self.windows, bd=2)
        self.back_frame.pack()

        for col in range(3):
            for r_ow in range(3):
                box_frame = Frame(self.back_frame, bd=2)
                box_frame.grid(row=r_ow, column=col)
                box_frame_list.append(box_frame)

        for box_f in box_frame_list:
            for col in range(3):
                for r_ow in range(3):
                    box = Entry(box_f, width=2, font=("Arial", 20), justify="center")
                    box.grid(row=r_ow, column=col)
                    box_list.append(box)

        print("ok")
        self.__resetBoard()
        self.generateGameBoard(dificulty)
        #print("ok")
        #string_board = self.boardAsString()
#
        #for i, entry in enumerate(box_list):
        #    entry.insert(0, string_board[i])

       

    

if __name__ == "__main__":

    sudoku = SudokuGui()
    sudoku.start_menu()
    sudoku.windows.mainloop()
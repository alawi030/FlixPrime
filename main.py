import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        # self.root.geometry("1920x1080")
        self.root.attributes("-fullscreen", True)
        self.root.title("FlixPrime")

        self.default_font = ("Courier", 22)
        self.dark_purple = "#A105CA"
        self.light_purple = "#E78DFF"
        self.white = "white"

        self.addWidgets()

    def addWidgets(self):
        self.topFrame()
        self.leftFrame()
        self.rightFrame()

    def topFrame(self):
        frame = tk.Frame(self.root, bg=self.dark_purple, height=180)
        frame.place(x=0, y=0, relwidth=1, anchor="nw")

        self.logo(frame)
        self.searchBar(frame)
        self.searchButton(frame)

    def leftFrame(self):
        frame = tk.Frame(self.root, bg=self.dark_purple, width=260, height=900)
        frame.place(x=0, y=180)

        self.titles(frame)

    def rightFrame(self):
        frame = tk.Frame(self.root, bg=self.light_purple, width=1660, height=900)
        frame.place(x=260, y=180)

        self.movieFrames(frame)
        self.pageNumbers(frame)

    def logo(self, frame):
        logo_img = tk.PhotoImage(file="logo.png")
        label = tk.Label(frame, image=logo_img, border=0)
        label.image = logo_img
        label.place(x=60, y=30)

    def searchBar(self, frame):
        entry = tk.Entry(frame, font=self.default_font, bg=self.white)
        entry.place(x=446.5, y=54, width=1085, height=75)
        entry.insert(tk.END, "Search for a movie...")

    def searchButton(self, frame):
        button = tk.Button(frame, text="search", font=self.default_font, bg=self.light_purple, fg=self.dark_purple)
        button.place(x=1542, y=54, width=175, height=75)

    def titles(self, frame):
        titles = ["Home", "Genre", "Country", "Movies", "TV Shows", "Top IMDB"]
        y = 40

        for title in titles:
            label = tk.Label(frame, text=title, font=self.default_font, bg=self.dark_purple, fg=self.white)
            label.place(x=0, y=y, width=260, height=50)
            y += 85

    def movieFrames(self, frame):
        positions = [(75, 40), (335, 40), (595, 40), (855, 40), (1115, 40), (1375, 40),
                     (75, 415), (335, 415), (595, 415), (855, 415), (1115, 415), (1375, 415)]
        size = (210, 360)
        color = self.white

        for pos in positions:
            movie_frame = tk.Frame(frame, bg=color)
            movie_frame.place(x=pos[0], y=pos[1], width=size[0], height=size[1])

    def pageNumbers(self, frame):
        positions = [(410, 825), (570, 900), (830, 900), (1090, 900), (1350, 900), (1610, 900)]
        size = (210, 50)
        color = self.dark_purple

        for pos in positions:
            page_number = tk.Label(frame, text="Page", font=self.default_font, bg=color, fg=self.white)
            page_number.place(x=pos[0], y=pos[1], width=size[0], height=size[1])

    def mainLoop(self):
        self.root.mainloop()

def main():
    gui = GUI()
    gui.mainLoop()

if __name__ == '__main__':
    main()
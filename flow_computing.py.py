# Name: Janidu Hettiarachchi
# Date: 2024-06-10
# Purpose: a simple math program for kids to learn algebra and other math concepts in a fun way.
# File name: flow_computing.py.py
import tkinter as tk
from tkinter import messagebox
import random
import os
from fractions import Fraction 

# This is the file location for the scores.txt file and images. It is set to the directory of this script.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("====================================")
print("BASE_DIR =", BASE_DIR)
print("Files in folder:")
print(os.listdir(BASE_DIR))
print("====================================")

# This is the file location for the scores.txt file and images. It is set to the directory of this script.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# This is the main window size and colours used in the program. You can change these values to customize the appearance of the program.
WINDOW_W, WINDOW_H = 600, 800 
BG        = "#0A0A2A"
CYAN      = "#00F5FF"
WHITE     = "#FFFFFF"
DARK_CARD = "#0D1B4B"
STAR_COL  = "#FFFFFF"
HEART     = "🚀"
SCORES_FILE = "scores.txt"

# These are the fonts that is been used to my program.
FONT_TITLE  = ("Courier", 26, "bold")
FONT_HEAD   = ("Courier", 18, "bold")
FONT_BODY   = ("Courier", 12)
FONT_SMALL  = ("Courier", 10)
FONT_BTN    = ("Courier", 14, "bold")
# This is the maximum number of lives a player can have. 
MAX_LIVES = 3 # change this if needed

# This function loads an image from the given filename and resizes it to the given size. 
def load_image(filename, size=None):
    # This function starts a try block if anything goes wrong it will print the error message and return None.
    try: 
        from PIL import Image, ImageTk
        # This full file path by joining the ffolder location with the filename. This is to make sure that the image can be found even if the program is run from a different directory.
        full_path = os.path.join(BASE_DIR, filename)
        # This opens the image file and converts it to RGBA format. It then gets the pixel data of the image and creates a new list of pixel data where the white pixels are replaced with transparent pixels. It then puts the new pixel data back into the image and resizes it if a size is given. 
        img = Image.open(full_path).convert("RGBA")
        # Gets every single pixel in the image as a list.
        data = img.getdata()
        # Creates a new list of pixel data where the white pixels are replaced with transparent pixels. It then puts the new pixel data back into the image and resizes it if a size is given.
        new_data = []
        for r, g, b, a in data:
            if r > 180 and g > 180 and b > 180: # remove white bg
                new_data.append((0, 0, 0, 0))
            else:
                new_data.append((r, g, b, a))
        img.putdata(new_data)
        if size:
            img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Image load failed for {filename}: {e}") # annoying
        return None
# This function saves a player's score and takes username and score.
def save_score(username: str, score: int):
    try:
        # This opens the scores.txt file in append mode means it adds to the end of the file without removing any existing scores.
        with open(SCORES_FILE, "a") as f:
            f.write(f"{username},{score}\n")
            # If the file cannot be opened or written to, it sliently does nothing instead of crashing the program.    
    except IOError:
        pass # whatever
# This helps tto define the function that reads all the scores from the file and returns the top 10
def load_scores():
    # This functions makes a empty list to store all the scores.
    entries = []
    try:
        # Opens scores.txt file in read mode.
        with open(SCORES_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if "," in line:
                    parts = line.rsplit(",", 1)
                    # Converts the score from string to an integer and appends the username and score as a tuple to the entries list. If the score cannot be converted to an integer, it skips that line.
                    try:
                        entries.append((parts[0], int(parts[1])))
                    except ValueError:
                        pass # skip broken lines
    except FileNotFoundError:
        pass
    entries.sort(key=lambda x: x[1], reverse=True)
    return entries[:10]

# this took me way too long
def generate_question(difficulty: str):
    if difficulty == "Easy":
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(["+", "-", "×"])
        if op == "+":
            return f"{a} + {b} = ?", a + b
        elif op == "-":
            a, b = max(a, b), min(a, b) # make sure no negatives
            return f"{a} - {b} = ?", a - b
        else:
            return f"{a} × {b} = ?", a * b

    elif difficulty == "Medium":
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        op = random.choice(["×", "÷", "²"])
        if op == "×":
            return f"{a} × {b} = ?", a * b
        elif op == "÷":
            product = a * b
            return f"{product} ÷ {a} = ?", b
        else:
            return f"{a}² = ?", a * a

    else: # hard mode gl
        mode = random.choice(["algebra", "power", "sqrt", "fraction", "pythagoras"])

        if mode == "algebra":
            x = random.randint(1, 15)
            b = random.randint(1, 30)
            coeff = random.randint(2, 5)
            result = coeff * x + b
            return f"Solve: {coeff}x + {b} = {result}", x

        elif mode == "power":
            base = random.randint(2, 6)
            exp  = random.randint(2, 4)
            return f"{base}^{exp} = ?", base ** exp

        elif mode == "sqrt":
            perfect = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
            return f"√{perfect} = ?", int(perfect ** 0.5)

        elif mode == "fraction":
            # fraction simplification - answer is numerator after simplifying
            # e.g. simplify 6/9 → 2/3, enter the numerator: 2
            pairs = [(2,4),(3,6),(4,8),(6,9),(4,6),(6,10),(8,12),(9,12),(10,15),(6,8)]
            num, den = random.choice(pairs)
            f = Fraction(num, den) # auto simplifies
            # ask them to find the numerator of the simplified fraction
            return (f"Simplify {num}/{den}\nEnter the numerator: ?", f.numerator)

        elif mode == "pythagoras":
            # pythagorean triples only so answer is always whole number
            triples = [
                (3, 4, 5),
                (5, 12, 13),
                (8, 15, 17),
                (7, 24, 25),
                (6, 8, 10),
                (9, 12, 15),
                (10, 24, 26),
            ]
            a, b, c = random.choice(triples)
            # randomly ask for a, b or c
            ask = random.choice(["c", "a", "b"])
            if ask == "c":
                return f"a={a}, b={b}\nFind c (a²+b²=c²): ?", c
            elif ask == "a":
                return f"b={b}, c={c}\nFind a (a²+b²=c²): ?", a
            else:
                return f"a={a}, c={c}\nFind b (a²+b²=c²): ?", b

# button factory thing
def styled_button(parent, text, command, width=18):
    btn = tk.Button(
        parent, text=text, command=command,
        font=FONT_BTN, fg="black", bg="#CCCCCC",
        relief="raised", bd=3, padx=10, pady=6,
        width=width, cursor="hand2",
    )
    return btn

def star_label(parent, filled=True):
    colour = CYAN if filled else "#444488"
    return tk.Label(parent, text="★", fg=colour, bg=BG, font=("Courier", 18))

class FlowComputing:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Flow Computing")
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.username       = tk.StringVar()
        self.difficulty     = tk.StringVar(value="Easy")
        self.score          = 0
        self.lives          = MAX_LIVES
        self.q_number       = 0
        self.correct_answer = 0 # set later

        # IMPORTANT dont delete this or images break
        self._image_refs = []

        self.img_bg   = None
        self.img_logo = None

        # find the image file (why is this so hard)
        astronaut_file = None
        for name in ["astronaut.png.png.png", "astronaut.png.png",
                     "astronaut.png", "astronaut_png.png"]:
            if os.path.exists(os.path.join(BASE_DIR, name)):
                astronaut_file = name
                print(f"✅ Found image: {name}")
                break

        if astronaut_file:
            self.img_loading = load_image(astronaut_file, (300, 180))
            self.img_start   = load_image(astronaut_file, (260, 155))
            self.img_game    = load_image(astronaut_file, (180, 108))
        else:
            print("❌ No astronaut image found") # rip
            self.img_loading = None
            self.img_start   = None
            self.img_game    = None

        # pin images or python deletes them (learnt this the hard way)
        for img in [self.img_loading, self.img_start, self.img_game]:
            if img is not None:
                self._image_refs.append(img)

        self.current_frame = None
        self.show_loading()

    def clear(self):
        if self.current_frame:
            self.current_frame.destroy()

    def base_frame(self):
        f = tk.Frame(self.root, bg=BG, width=WINDOW_W, height=WINDOW_H)
        f.pack_propagate(False)
        f.pack(fill="both", expand=True)
        self.current_frame = f
        return f

    def draw_stars(self, canvas):
        for _ in range(60):
            x = random.randint(0, WINDOW_W)
            y = random.randint(0, WINDOW_H)
            r = random.choice([1, 1, 1, 2])
            canvas.create_oval(x-r, y-r, x+r, y+r, fill=STAR_COL, outline="")

    # loading screen
    def show_loading(self):
        self.clear()
        f = self.base_frame()

        canvas = tk.Canvas(f, width=WINDOW_W, height=WINDOW_H,
                           bg=BG, highlightthickness=0)
        canvas.place(x=0, y=0)
        self.draw_stars(canvas)

        container = tk.Frame(f, bg=BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="FLOW", font=("Courier", 38, "bold"),
                 fg=WHITE, bg=BG).pack()
        tk.Label(container, text="COMPUTING", font=("Courier", 24, "bold"),
                 fg=CYAN, bg=BG).pack()

        tk.Frame(container, bg=CYAN, height=2, width=300).pack(pady=8)

        if self.img_loading:
            lbl = tk.Label(container, image=self.img_loading, bg=BG)
            lbl.image = self.img_loading # dont remove this
            lbl.pack(pady=8)
        else:
            tk.Label(container, text="🚀", font=("Courier", 60), bg=BG).pack(pady=8)

        tk.Label(container, text="Master algebra. Explore the universe.",
                 font=("Courier", 10), fg=CYAN, bg=BG).pack()

        tk.Frame(container, bg=CYAN, height=2, width=300).pack(pady=8)

        bar_outer = tk.Frame(container, bg=DARK_CARD, width=300, height=14,
                             highlightthickness=1, highlightbackground=CYAN)
        bar_outer.pack()
        bar_outer.pack_propagate(False)

        self.loading_bar = tk.Frame(bar_outer, bg=CYAN, width=0, height=14)
        self.loading_bar.place(x=0, y=0, height=14)

        self.loading_label = tk.Label(container, text="Loading...",
                                      font=("Courier", 9), fg=CYAN, bg=BG)
        self.loading_label.pack(pady=4)

        self._loading_progress = 0
        self._animate_loading()

    def _animate_loading(self):
        self._loading_progress += 4
        bar_w = int((self._loading_progress / 100) * 300)
        self.loading_bar.place(x=0, y=0, width=bar_w, height=14)

        messages = ["Loading...", "Preparing questions...",
                    "Launching rocket...", "Almost there..."]
        idx = min(self._loading_progress // 25, len(messages) - 1)
        self.loading_label.config(text=messages[idx])

        if self._loading_progress < 100:
            self.root.after(40, self._animate_loading)
        else:
            self.root.after(400, self.show_start)

    # start screen
    def show_start(self):
        self.clear()
        f = self.base_frame()

        canvas = tk.Canvas(f, width=WINDOW_W, height=WINDOW_H,
                           bg=BG, highlightthickness=0)
        canvas.place(x=0, y=0)
        self.draw_stars(canvas)

        top = tk.Frame(f, bg=BG)
        top.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(top, text="Flow", font=("Courier", 34, "bold"),
                 fg=WHITE, bg=BG).pack()
        tk.Label(top, text="Computing", font=("Courier", 22, "bold"),
                 fg=CYAN, bg=BG).pack()

        tk.Frame(top, bg=CYAN, height=2, width=300).pack(pady=4)

        tk.Label(top, text="Username", font=FONT_SMALL, fg=CYAN, bg=BG).pack(anchor="w", padx=20)
        entry = tk.Entry(top, textvariable=self.username, font=FONT_BODY,
                         bg=DARK_CARD, fg=WHITE, insertbackground=WHITE,
                         relief="flat", bd=0, width=28)
        entry.pack(padx=20, pady=(0, 4), ipady=6)

        tk.Label(top, text="Select Difficulty", font=FONT_SMALL, fg=CYAN, bg=BG).pack()
        diff_row = tk.Frame(top, bg=BG)
        diff_row.pack(pady=2)
        for diff in ["Easy", "Medium", "Hard"]:
            btn = tk.Button(
                diff_row, text=f"★  {diff}",
                font=FONT_BTN, fg=WHITE, bg=DARK_CARD,
                activeforeground=BG, activebackground=CYAN,
                relief="flat", bd=0, padx=14, pady=6,
                width=9, cursor="hand2",
                highlightthickness=1, highlightbackground=CYAN,
                command=lambda d=diff: self._set_diff(d)
            )
            btn.pack(side="left", padx=4)

        # astronaut goes here
        if self.img_start:
            lbl = tk.Label(top, image=self.img_start, bg=BG)
            lbl.image = self.img_start
            lbl.pack(pady=6)

        btn_row = tk.Frame(top, bg=BG)
        btn_row.pack(pady=6)
        styled_button(btn_row, "START GAME",  self._start_game,      width=14).pack(side="left", padx=6)
        styled_button(btn_row, "LEADERBOARD", self.show_leaderboard, width=14).pack(side="left", padx=6)

        self.diff_label = tk.Label(top, text=f"Difficulty: {self.difficulty.get()}",
                                   font=FONT_SMALL, fg=CYAN, bg=BG)
        self.diff_label.pack(pady=4)

    def _set_diff(self, d):
        self.difficulty.set(d)
        self.diff_label.config(text=f"Difficulty: {d}")

    def _start_game(self):
        name = self.username.get().strip()
        if not name:
            messagebox.showwarning("Username required", "Please enter a username to start.")
            return
        self.score    = 0
        self.lives    = MAX_LIVES
        self.q_number = 0
        self.show_game()

    # game screen
    def show_game(self):
        self.clear()
        f = self.base_frame()

        header = tk.Frame(f, bg=DARK_CARD, pady=6)
        header.pack(fill="x")

        tk.Label(header, text=self.username.get(), font=FONT_SMALL,
                 fg=CYAN, bg=DARK_CARD).pack(side="left", padx=10)

        self.health_label = tk.Label(header, text=self._hearts(),
                                     font=("Courier", 14), fg="#FF4466", bg=DARK_CARD)
        self.health_label.pack(side="right", padx=10)

        tk.Label(header, text=f"Health {self.lives}/{MAX_LIVES}", font=FONT_SMALL,
                 fg=WHITE, bg=DARK_CARD).pack(side="right")

        level_bar = tk.Frame(f, bg=BG, pady=4)
        level_bar.pack(fill="x")
        tk.Label(level_bar, text=f"Level: {self.difficulty.get()}  ★",
                 font=FONT_BODY, fg=CYAN, bg=BG).pack(side="left", padx=14)
        self.score_lbl = tk.Label(level_bar, text=f"Score: {self.score}",
                                  font=FONT_BODY, fg=WHITE, bg=BG)
        self.score_lbl.pack(side="right", padx=14)

        card = tk.Frame(f, bg=DARK_CARD, bd=2, relief="flat",
                        highlightthickness=2, highlightbackground=CYAN)
        card.pack(padx=30, pady=20, fill="both", expand=True)

        sprite_frame = tk.Frame(card, bg=DARK_CARD, height=120)
        sprite_frame.pack(fill="x")
        if self.img_game:
            lbl = tk.Label(sprite_frame, image=self.img_game, bg=DARK_CARD)
            lbl.image = self.img_game
            lbl.pack(pady=8)

        self.q_label = tk.Label(card, text="", font=FONT_HEAD,
                                fg=WHITE, bg=DARK_CARD, wraplength=360, pady=10)
        self.q_label.pack()

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(card, textvariable=self.answer_var,
                                     font=FONT_HEAD, bg="#111133", fg=CYAN,
                                     insertbackground=CYAN, relief="flat",
                                     justify="center", width=10)
        self.answer_entry.pack(pady=10, ipady=8)
        self.answer_entry.bind("<Return>", lambda e: self._submit())
        self.answer_entry.focus_set()

        styled_button(card, "SUBMIT", self._submit, width=12).pack(pady=(0, 20))

        self._next_question()

    def _hearts(self):
        return HEART * self.lives + "  " * (MAX_LIVES - self.lives)

    def _next_question(self):
        self.q_number += 1
        q_text, self.correct_answer = generate_question(self.difficulty.get())
        self.q_label.config(text=f"Q{self.q_number}: {q_text}")
        self.answer_var.set("")
        self.answer_entry.focus_set()

    def _submit(self):
        raw = self.answer_var.get().strip()
        if not raw:
            messagebox.showwarning("Empty answer", "Please enter an answer.")
            return
        if not raw.lstrip("-").isdigit():
            messagebox.showerror("Invalid input", "Numbers only — no letters or special characters.")
            return

        guess = int(raw)
        if guess == self.correct_answer:
            self.score += 10
            self.score_lbl.config(text=f"Score: {self.score}")
            if self.q_number >= 10:
                self._end_game(won=True)
                return
            self._next_question()
        else:
            self.lives -= 1
            self.health_label.config(text=self._hearts())
            if self.lives <= 0:
                self._end_game(won=False)
            else:
                messagebox.showinfo("Wrong!",
                    f"Incorrect — {self.lives} {'life' if self.lives == 1 else 'lives'} left.\n"
                    f"Answer was: {self.correct_answer}")
                self._next_question()

    def _end_game(self, won: bool):
        save_score(self.username.get(), self.score)
        self.show_end_screen(won)

    # end screen
    def show_end_screen(self, won: bool):
        self.clear()
        f = self.base_frame()

        canvas = tk.Canvas(f, width=WINDOW_W, height=WINDOW_H,
                           bg=BG, highlightthickness=0)
        canvas.place(x=0, y=0)
        self.draw_stars(canvas)

        container = tk.Frame(f, bg=BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        star_row = tk.Frame(container, bg=BG)
        star_row.pack()
        star_label(star_row, filled=True).pack(side="left", padx=4)
        star_label(star_row, filled=won).pack(side="left", padx=4)
        star_label(star_row, filled=won).pack(side="left", padx=4)

        title  = "Mission Complete!" if won else "Mission Failed"
        colour = CYAN if won else "#FF4466"
        tk.Label(container, text=title, font=FONT_TITLE, fg=colour, bg=BG).pack(pady=(8, 4))
        tk.Label(container, text=f"Your score: {self.score}", font=FONT_HEAD,
                 fg=WHITE, bg=BG).pack()

        tk.Frame(container, bg=CYAN, height=2, width=360).pack(pady=10)

        self._build_leaderboard_table(container)

        btn_row = tk.Frame(container, bg=BG)
        btn_row.pack(pady=16)
        styled_button(btn_row, "PLAY AGAIN", self._start_game, width=13).pack(side="left", padx=6)
        styled_button(btn_row, "MAIN MENU",  self.show_start,  width=13).pack(side="left", padx=6)

        bot_row = tk.Frame(container, bg=BG)
        bot_row.pack()
        star_label(bot_row, filled=True).pack(side="left", padx=4)
        star_label(bot_row, filled=False).pack(side="left", padx=4)
        star_label(bot_row, filled=False).pack(side="left", padx=4)

    # leaderboard screen
    def show_leaderboard(self):
        self.clear()
        f = self.base_frame()

        canvas = tk.Canvas(f, width=WINDOW_W, height=WINDOW_H,
                           bg=BG, highlightthickness=0)
        canvas.place(x=0, y=0)
        self.draw_stars(canvas)

        container = tk.Frame(f, bg=BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        star_row = tk.Frame(container, bg=BG)
        star_row.pack()
        star_label(star_row, filled=True).pack(side="left", padx=4)
        star_label(star_row, filled=True).pack(side="left", padx=4)
        star_label(star_row, filled=False).pack(side="left", padx=4)

        tk.Label(container, text="Highscore", font=FONT_TITLE,
                 fg=CYAN, bg=BG).pack(pady=(8, 2))
        tk.Frame(container, bg=CYAN, height=2, width=360).pack(pady=8)

        self._build_leaderboard_table(container)

        styled_button(container, "← BACK", self.show_start, width=12).pack(pady=14)

    def _build_leaderboard_table(self, parent):
        entries = load_scores()

        table = tk.Frame(parent, bg=CYAN, padx=2, pady=2)
        table.pack(padx=20)
        inner = tk.Frame(table, bg=DARK_CARD)
        inner.pack()

        tk.Label(inner, text="  USERNAME", font=("Courier", 11, "bold"),
                 fg=CYAN, bg=DARK_CARD, width=20, anchor="w").grid(
            row=0, column=0, sticky="w", padx=8, pady=4)
        tk.Label(inner, text="SCORE  ", font=("Courier", 11, "bold"),
                 fg=CYAN, bg=DARK_CARD, width=10, anchor="e").grid(
            row=0, column=1, sticky="e", padx=8, pady=4)
        tk.Frame(inner, bg=CYAN, height=1).grid(row=1, column=0,
                                                  columnspan=2, sticky="ew")

        if not entries:
            tk.Label(inner, text="No scores yet!", font=FONT_SMALL,
                     fg=WHITE, bg=DARK_CARD).grid(row=2, column=0,
                                                    columnspan=2, pady=10)
        else:
            for i, (name, sc) in enumerate(entries):
                row_bg = "#0D1B4B" if i % 2 == 0 else "#111133"
                tk.Label(inner, text=f"  {i+1:>2}. {name}", font=FONT_SMALL,
                         fg=WHITE, bg=row_bg, anchor="w", width=22).grid(
                    row=i+2, column=0, sticky="w", padx=6, pady=2)
                tk.Label(inner, text=f"{sc}  ", font=FONT_SMALL,
                         fg=CYAN, bg=row_bg, anchor="e", width=10).grid(
                    row=i+2, column=1, sticky="e", padx=6, pady=2)

# run it
if __name__ == "__main__":
    root = tk.Tk()
    app = FlowComputing(root)
    root.mainloop()
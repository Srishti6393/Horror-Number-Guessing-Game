import tkinter as tk
import random
import time


class HorrorGuessGame:

    def __init__(self, root):
        self.root = root

        # ---------------- WINDOW ----------------
        self.root.title("CURSED NUMBER - Horror Guessing Game")
        self.root.geometry("850x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#050505")

        # ---------------- GAME VARIABLES ----------------
        self.level = 1
        self.score = 0
        self.chances = 5
        self.max_chances = 5

        self.secret = 0
        self.number_limit = 20

        self.time_left = 30
        self.timer_running = False

        self.game_over = False
        self.game_won = False

        self.flicker_state = False
        self.shake_count = 0

        # ---------------- CANVAS ----------------
        self.canvas = tk.Canvas(
            root,
            width=850,
            height=650,
            bg="#050505",
            highlightthickness=0
        )

        self.canvas.pack()

        # Start screen
        self.show_start_screen()

    # ==================================================
    # START SCREEN
    # ==================================================

    def show_start_screen(self):

        self.canvas.delete("all")

        # Background
        self.draw_horror_room()

        self.canvas.create_text(
            425,
            130,
            text="CURSED NUMBER",
            font=("Arial", 40, "bold"),
            fill="#8b0000"
        )

        self.canvas.create_text(
            425,
            185,
            text="HORROR GUESSING GAME",
            font=("Arial", 18, "bold"),
            fill="#dddddd"
        )

        self.canvas.create_text(
            425,
            270,
            text="You are trapped inside a haunted room.",
            font=("Arial", 16),
            fill="#bbbbbb"
        )

        self.canvas.create_text(
            425,
            305,
            text="Guess the cursed number before the ghost finds you.",
            font=("Arial", 14),
            fill="#888888"
        )

        # Start button
        self.start_button = tk.Button(
            self.root,
            text="ENTER THE ROOM",
            font=("Arial", 14, "bold"),
            bg="#8b0000",
            fg="white",
            activebackground="#ff0000",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.start_game
        )

        self.start_button.place(
            x=325,
            y=380,
            width=200,
            height=50
        )

        self.canvas.create_text(
            425,
            500,
            text="WARNING: Do not lose all your chances...",
            font=("Arial", 12, "italic"),
            fill="#550000"
        )

        self.flicker_title()

    # ==================================================
    # HORROR ROOM
    # ==================================================

    def draw_horror_room(self):

        # Floor
        self.canvas.create_rectangle(
            0, 520, 850, 650,
            fill="#090909",
            outline=""
        )

        # Wall lines
        for y in range(0, 520, 65):
            self.canvas.create_line(
                0, y, 850, y,
                fill="#101010"
            )

        # Door
        self.canvas.create_rectangle(
            330, 160, 520, 520,
            fill="#111111",
            outline="#3a0000",
            width=5
        )

        self.canvas.create_rectangle(
            350, 180, 500, 520,
            fill="#080808",
            outline="#220000"
        )

        # Door handle
        self.canvas.create_oval(
            470, 345, 485, 360,
            fill="#777777",
            outline=""
        )

        # Window
        self.canvas.create_rectangle(
            80, 150, 230, 290,
            fill="#020206",
            outline="#330000",
            width=4
        )

        # Moon
        self.canvas.create_oval(
            135, 175, 180, 220,
            fill="#ddddbb",
            outline=""
        )

        # Blood-like marks
        self.canvas.create_line(
            250, 100, 265, 145,
            fill="#550000",
            width=4
        )

        self.canvas.create_line(
            600, 100, 590, 155,
            fill="#550000",
            width=4
        )

        # Ghost
        self.draw_ghost(680, 300)

    # ==================================================
    # GHOST
    # ==================================================

    def draw_ghost(self, x, y):

        # Body
        self.canvas.create_oval(
            x - 55,
            y - 70,
            x + 55,
            y + 70,
            fill="#d8d8d8",
            outline=""
        )

        # Bottom ghost waves
        self.canvas.create_oval(
            x - 55,
            y + 30,
            x - 20,
            y + 90,
            fill="#d8d8d8",
            outline=""
        )

        self.canvas.create_oval(
            x - 20,
            y + 30,
            x + 20,
            y + 90,
            fill="#d8d8d8",
            outline=""
        )

        self.canvas.create_oval(
            x + 20,
            y + 30,
            x + 55,
            y + 90,
            fill="#d8d8d8",
            outline=""
        )

        # Eyes
        self.canvas.create_oval(
            x - 30,
            y - 25,
            x - 10,
            y + 5,
            fill="#000000"
        )

        self.canvas.create_oval(
            x + 10,
            y - 25,
            x + 30,
            y + 5,
            fill="#000000"
        )

        # Mouth
        self.canvas.create_oval(
            x - 18,
            y + 15,
            x + 18,
            y + 50,
            fill="#000000"
        )

    # ==================================================
    # START GAME
    # ==================================================

    def start_game(self):

        if hasattr(self, "start_button"):
            self.start_button.destroy()

        self.level = 1
        self.score = 100
        self.start_new_level()

    # ==================================================
    # NEW LEVEL
    # ==================================================

    def start_new_level(self):

        self.canvas.delete("all")
        self.draw_horror_room()

        self.game_over = False
        self.game_won = False

        self.number_limit = 20 + ((self.level - 1) * 20)

        self.chances = max(3, 6 - self.level // 2)

        self.max_chances = self.chances

        self.secret = random.randint(
            1,
            self.number_limit
        )

        self.time_left = max(
            12,
            30 - ((self.level - 1) * 3)
        )

        self.timer_running = True

        # Heading
        self.canvas.create_text(
            425,
            35,
            text="CURSED NUMBER",
            font=("Arial", 27, "bold"),
            fill="#aa0000",
            tags="title"
        )

        # Level
        self.canvas.create_text(
            120,
            75,
            text=f"LEVEL {self.level}",
            font=("Arial", 14, "bold"),
            fill="#ff3333"
        )

        # Score
        self.canvas.create_text(
            720,
            75,
            text=f"SCORE: {self.score}",
            font=("Arial", 14, "bold"),
            fill="#dddddd"
        )

        # Instructions
        self.canvas.create_text(
            425,
            110,
            text=f"Guess the cursed number from 1 to {self.number_limit}",
            font=("Arial", 14),
            fill="#bbbbbb"
        )

        # Chances
        self.canvas.create_text(
            425,
            475,
            text=f"CHANCES: {self.chances}",
            font=("Arial", 16, "bold"),
            fill="#ff3333",
            tags="chances"
        )

        # Timer
        self.canvas.create_text(
            425,
            510,
            text=f"TIME: {self.time_left}",
            font=("Arial", 15, "bold"),
            fill="#dddddd",
            tags="timer"
        )

        # Input
        self.entry = tk.Entry(
            self.root,
            font=("Arial", 20, "bold"),
            justify="center",
            bg="#111111",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entry.place(
            x=340,
            y=380,
            width=170,
            height=45
        )

        self.entry.focus()

        # Guess button
        self.guess_button = tk.Button(
            self.root,
            text="UNLOCK DOOR",
            font=("Arial", 12, "bold"),
            bg="#8b0000",
            fg="white",
            activebackground="#ff0000",
            activeforeground="white",
            relief="flat",
            command=self.check_guess,
            cursor="hand2"
        )

        self.guess_button.place(
            x=350,
            y=435,
            width=150,
            height=38
        )

        # Feedback
        self.canvas.create_text(
            425,
            560,
            text="The room is watching you...",
            font=("Arial", 13, "italic"),
            fill="#777777",
            tags="feedback"
        )

        # Bind Enter key
        self.root.bind(
            "<Return>",
            lambda event: self.check_guess()
        )

        self.update_timer()

    # ==================================================
    # CHECK GUESS
    # ==================================================

    def check_guess(self):

        if self.game_over or self.game_won:
            return

        value = self.entry.get().strip()

        if not value.isdigit():

            self.set_feedback(
                "The ghost whispers: ENTER A NUMBER...",
                "#ff3333"
            )

            self.shake_screen()
            self.root.bell()

            return

        guess = int(value)

        if guess < 1 or guess > self.number_limit:

            self.set_feedback(
                f"Choose a number between 1 and {self.number_limit}.",
                "#ff8800"
            )

            return

        self.entry.delete(0, tk.END)

        self.chances -= 1

        # Score penalty
        self.score = max(
            0,
            self.score - 10
        )

        self.canvas.itemconfig(
            "chances",
            text=f"CHANCES: {self.chances}"
        )

        # Correct
        if guess == self.secret:

            self.game_won = True
            self.timer_running = False

            self.score += self.time_left * 5

            self.root.bell()

            self.win_screen()

            return

        # Distance
        difference = abs(
            self.secret - guess
        )

        if difference <= 2:

            message = (
                "🔥 VERY CLOSE...\n"
                "You can hear breathing behind you."
            )

            color = "#ff0000"

            self.shake_screen()

        elif difference <= 5:

            message = (
                "🌡️ WARM...\n"
                "The ghost is getting closer."
            )

            color = "#ff6600"

        else:

            message = (
                "❄️ COLD...\n"
                "The room becomes colder."
            )

            color = "#66ccff"

        # Higher / Lower clue
        if guess < self.secret:

            message += "\nThe whisper says: HIGHER..."

        else:

            message += "\nThe whisper says: LOWER..."

        self.set_feedback(
            message,
            color
        )

        self.root.bell()

        # Last chance
        if self.chances == 1:

            self.canvas.itemconfig(
                "feedback",
                text="LAST CHANCE...\nTHE GHOST IS BEHIND YOU.",
                fill="#ff0000"
            )

            self.flash_screen()

        # No chances
        if self.chances <= 0:

            self.game_over = True
            self.timer_running = False

            self.root.after(
                700,
                self.lose_screen
            )

    # ==================================================
    # FEEDBACK
    # ==================================================

    def set_feedback(self, message, color):

        self.canvas.itemconfig(
            "feedback",
            text=message,
            fill=color
        )

    # ==================================================
    # TIMER
    # ==================================================

    def update_timer(self):

        if not self.timer_running:
            return

        self.canvas.itemconfig(
            "timer",
            text=f"TIME: {self.time_left}"
        )

        if self.time_left <= 5:

            self.canvas.itemconfig(
                "timer",
                fill="#ff0000"
            )

        if self.time_left <= 0:

            self.timer_running = False
            self.game_over = True

            self.lose_screen()

            return

        self.time_left -= 1

        self.root.after(
            1000,
            self.update_timer
        )

    # ==================================================
    # SCREEN SHAKE
    # ==================================================

    def shake_screen(self):

        original_x = self.root.winfo_x()
        original_y = self.root.winfo_y()

        self.shake_count = 0

        def shake():

            if self.shake_count >= 8:

                self.root.geometry(
                    f"850x650+{original_x}+{original_y}"
                )

                return

            offset = random.randint(
                -8,
                8
            )

            self.root.geometry(
                f"850x650+"
                f"{original_x + offset}+"
                f"{original_y + offset}"
            )

            self.shake_count += 1

            self.root.after(
                40,
                shake
            )

        shake()

    # ==================================================
    # FLASH EFFECT
    # ==================================================

    def flash_screen(self):

        colors = [
            "#ff0000",
            "#050505",
            "#550000",
            "#050505",
            "#ff0000",
            "#050505"
        ]

        def flash(index=0):

            if index >= len(colors):
                return

            self.root.configure(
                bg=colors[index]
            )

            self.root.after(
                120,
                lambda: flash(index + 1)
            )

        flash()

    # ==================================================
    # WIN SCREEN
    # ==================================================

    def win_screen(self):

        self.canvas.delete("all")

        if hasattr(self, "entry"):
            self.entry.destroy()

        if hasattr(self, "guess_button"):
            self.guess_button.destroy()

        self.canvas.configure(
            bg="#061b0b"
        )

        self.canvas.create_text(
            425,
            150,
            text="YOU ESCAPED!",
            font=("Arial", 42, "bold"),
            fill="#00ff66"
        )

        self.canvas.create_text(
            425,
            220,
            text="THE CURSED DOOR IS OPEN",
            font=("Arial", 20, "bold"),
            fill="#ffffff"
        )

        self.canvas.create_text(
            425,
            290,
            text=f"The number was: {self.secret}",
            font=("Arial", 18),
            fill="#bbbbbb"
        )

        self.canvas.create_text(
            425,
            330,
            text=f"Your Score: {self.score}",
            font=("Arial", 18, "bold"),
            fill="#ffd700"
        )

        self.canvas.create_text(
            425,
            410,
            text="DARE YOU PLAY AGAIN?",
            font=("Arial", 24, "bold"),
            fill="#ff3333"
        )

        self.create_end_buttons()

    # ==================================================
    # LOSE SCREEN
    # ==================================================

    def lose_screen(self):

        self.canvas.delete("all")

        if hasattr(self, "entry"):
            self.entry.destroy()

        if hasattr(self, "guess_button"):
            self.guess_button.destroy()

        self.canvas.configure(
            bg="#150000"
        )

        self.flash_screen()

        self.canvas.create_text(
            425,
            130,
            text="GAME OVER",
            font=("Arial", 45, "bold"),
            fill="#ff0000"
        )

        self.canvas.create_text(
            425,
            210,
            text="THE GHOST FOUND YOU...",
            font=("Arial", 22, "bold"),
            fill="#ffffff"
        )

        self.canvas.create_text(
            425,
            270,
            text=f"The cursed number was: {self.secret}",
            font=("Arial", 17),
            fill="#bbbbbb"
        )

        self.canvas.create_text(
            425,
            330,
            text=f"Final Score: {self.score}",
            font=("Arial", 18, "bold"),
            fill="#ffd700"
        )

        self.canvas.create_text(
            425,
            410,
            text="DARE YOU PLAY AGAIN?",
            font=("Arial", 24, "bold"),
            fill="#ff0000"
        )

        self.create_end_buttons()

    # ==================================================
    # END BUTTONS
    # ==================================================

    def create_end_buttons(self):

        self.yes_button = tk.Button(
            self.root,
            text="YES - I'M BRAVE",
            font=("Arial", 12, "bold"),
            bg="#8b0000",
            fg="white",
            activebackground="#ff0000",
            activeforeground="white",
            relief="flat",
            command=self.restart_game,
            cursor="hand2"
        )

        self.yes_button.place(
            x=275,
            y=475,
            width=145,
            height=45
        )

        self.no_button = tk.Button(
            self.root,
            text="NO - RUN AWAY",
            font=("Arial", 12, "bold"),
            bg="#222222",
            fg="white",
            activebackground="#555555",
            relief="flat",
            command=self.exit_game,
            cursor="hand2"
        )

        self.no_button.place(
            x=430,
            y=475,
            width=145,
            height=45
        )

    # ==================================================
    # RESTART
    # ==================================================

    def restart_game(self):

        if hasattr(self, "yes_button"):
            self.yes_button.destroy()

        if hasattr(self, "no_button"):
            self.no_button.destroy()

        self.canvas.configure(
            bg="#050505"
        )

        self.level = 1
        self.score = 100

        self.start_new_level()

    # ==================================================
    # NEXT LEVEL
    # ==================================================

    def next_level(self):

        self.level += 1
        self.start_new_level()

    # ==================================================
    # EXIT
    # ==================================================

    def exit_game(self):

        self.canvas.delete("all")

        if hasattr(self, "yes_button"):
            self.yes_button.destroy()

        if hasattr(self, "no_button"):
            self.no_button.destroy()

        self.canvas.configure(
            bg="#000000"
        )

        self.canvas.create_text(
            425,
            250,
            text="YOU RAN AWAY...",
            font=("Arial", 35, "bold"),
            fill="#777777"
        )

        self.canvas.create_text(
            425,
            310,
            text="The ghost is still waiting.",
            font=("Arial", 16, "italic"),
            fill="#555555"
        )

        self.canvas.create_text(
            425,
            370,
            text="Close the window to exit.",
            font=("Arial", 12),
            fill="#444444"
        )

    # ==================================================
    # FLICKERING TITLE
    # ==================================================

    def flicker_title(self):

        if not self.canvas.winfo_exists():
            return

        try:

            if self.flicker_state:

                self.canvas.itemconfig(
                    "title",
                    fill="#330000"
                )

            else:

                self.canvas.itemconfig(
                    "title",
                    fill="#ff0000"
                )

            self.flicker_state = not self.flicker_state

            self.root.after(
                random.randint(250, 700),
                self.flicker_title
            )

        except:
            pass


# ======================================================
# RUN GAME
# ======================================================

if __name__ == "__main__":

    root = tk.Tk()

    game = HorrorGuessGame(root)

    root.mainloop()
from turtle import Turtle
FONT = ("Courier", 12, "normal")
FONT2 = ("Courier", 50, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.high_score = 0
        #V3:
        with open("highscore.txt") as data:
            self.high_score = int(data.read())

    #+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X=+X
    def start_counting(self):
        self.goto(0, 280)
        self.write(f"Score:{self.score}", align="center", font=FONT)

    def refresh_score(self, plus_amount):
        self.clear()
        self.score += plus_amount
        #
        self.goto(0, 280)
        self.write(f"Score:{self.score}", align="center", font=FONT)

    #V3-Changes:
    # def game_over_screen(self):
    #     self.clear()
    #     #
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=FONT2)
    # |
    # |
    # |
    def update_score_board(self):
        self.clear()
        self.goto(0, 230)
        #
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            with open("highscore.txt", mode="r") as high_scores_list:
                self.high_score = high_scores_list.read()
            #--------------------------
            with open("highscore.txt", mode="w") as self.high_score_file_update:
                self.high_score = self.score
                self.high_score_file_update.write(str(self.high_score))

        #---------
        self.score = 0 #reset
        self.update_score_board()
        #
        #DEBUG
        with open ("highscore.txt") as file_check:
            content = file_check.read()
            print(content)

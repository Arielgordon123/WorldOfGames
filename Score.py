from utils import SCORES_FILE_NAME
from os import path


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5

    if path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r+") as file:
            data = file.read()
            score = int(data)
            file.seek(0)
            file.write(str(score + POINTS_OF_WINNING))
    else:
        with open(SCORES_FILE_NAME, "w") as file:
            file.seek(0)
            file.write(str(POINTS_OF_WINNING))

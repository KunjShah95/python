class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    print(f"Age set to {age}")

set_age(25)   # Works fine

try:
    set_age(-5)
except NegativeAgeError as e:
    print("Caught custom exception:", e)

class InvalidScoreError(Exception):
    def __init__(self, score, message="Score must be between 0 and 100"):
        self.score = score
        self.message = message
        super().__init__(f"{score} is invalid. {message}")

def enter_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(score)
    print(f"Score recorded: {score}")

try:
    enter_score(105)
except InvalidScoreError as e:
    print(e)

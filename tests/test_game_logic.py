# from logic_utils import check_guess
from app import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # result = check_guess(50, 50)
    # assert result == "Win"
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "CORRECT" in message.upper()


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    # result = check_guess(60, 50)
    # assert result == "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    # result = check_guess(40, 50)
    # assert result == "Too Low"

    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
   

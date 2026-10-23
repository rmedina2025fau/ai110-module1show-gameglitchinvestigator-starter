from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_says_go_lower():
    # Bug fix: a guess above the secret must tell the player to go LOWER
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_too_low_hint_says_go_higher():
    # Bug fix: a guess below the secret must tell the player to go HIGHER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_guess_compares_as_numbers_not_strings():
    # Bug fix: "50" > "19" is False as strings, so 50 must still be too high for 19
    outcome, _ = check_guess(50, 19)
    assert outcome == "Too High"


def test_get_range_for_each_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_valid_number():
    assert parse_guess("42") == (True, 42, None)


def test_parse_guess_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False and value is None and err == "Enter a guess."


def test_parse_guess_not_a_number():
    ok, value, err = parse_guess("abc")
    assert ok is False and value is None and err == "That is not a number."


def test_win_points_drop_with_more_attempts():
    assert update_score(0, "Win", 1) == 90
    assert update_score(0, "Win", 3) == 70


def test_win_points_have_a_minimum_of_ten():
    assert update_score(0, "Win", 20) == 10


def test_wrong_guess_costs_five_points():
    assert update_score(50, "Too High", 2) == 45
    assert update_score(50, "Too Low", 3) == 45


def test_wrong_guess_never_makes_score_negative():
    # Bug fix: score used to go negative after several wrong guesses
    assert update_score(0, "Too Low", 1) == 0
    assert update_score(3, "Too High", 2) == 0

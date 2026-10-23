# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A number guessing game in Streamlit. The player guesses a secret number within a range, gets "go higher" or "go lower" hints, and has a limited number of attempts. Points are awarded for wins and taken away for wrong guesses.

**Bugs found:**
1. Hints were inverted. A guess above the secret said "go higher".
2. New Game did not reset the game state. After a loss or win, input stayed blocked until a page refresh. New Game also ignored the difficulty range.
3. The score went negative after several wrong guesses. The Too High penalty also depended on whether the attempt number was even or odd.
4. The attempt counter started at 1, so the sidebar showed one fewer attempt left than the limit.
5. On even attempts, the secret was compared as a string, so hints could be wrong (for example, "50" > "19" is false as strings).

**Fixes applied:**
- Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py`. `app.py` imports them.
- `check_guess` returns `(outcome, message)`. "Too High" now says "Go LOWER", and "Too Low" says "Go HIGHER".
- Removed the string-secret branch. The secret is always compared as an integer.
- New Game resets the secret (within the difficulty range), attempts, score, status, and history.
- Wrong guesses cost 5 points and the score never goes below 0. A win gives 100 minus 10 per attempt, with a minimum of 10.
- The attempt counter starts at 0.
- Added pytest tests for each fix.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and pick a difficulty in the sidebar. The sidebar shows the range and the attempts allowed.
2. Enter a guess. The hint now matches the direction: a guess above the secret says "Go LOWER".
3. Keep guessing until you win or run out of attempts. The score never goes below 0.
4. After the game ends, click "New Game". The input works again, the attempts and score reset, and the new secret is in the difficulty's range.
5. Guess the secret to win. The final score is shown in the success message.

**Screenshot** *(optional)*: <!-- Not included -->

_Note: the UI steps above were written from the code and were not clicked through in a browser for this submission._

## 🧪 Test Results

```
$ python -m pytest -q
..............                                                           [100%]
14 passed in 0.01s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

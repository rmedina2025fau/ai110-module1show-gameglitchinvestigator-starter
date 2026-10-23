# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game opened as a Streamlit guessing game with a difficulty setting, a range of 1 to 100 on Normal, and 8 attempts. It ran without crashing. The problems showed up once I started playing: the hints pointed the wrong way, the game froze after it ended, and the score was wrong after a win.

**Bug 1: Hints are backwards.** With a secret of 19, I guessed 50 several times and the game kept saying to go higher until I ran out of attempts. A guess above the secret should say to go lower. Guessing below the secret also gave the wrong message: it said "go lower" when it should say "go higher". Both cases look like one inverted comparison.

**Bug 2: New Game does not reset the game state.** After I lost and clicked New Game, Developer Debug Info showed a new secret number. The screen still showed the old finished game and I could not enter any guesses until I refreshed the page. The secret resets but the game-over state does not.

**Bug 3: Wrong score after a win.** I copied the secret from Developer Debug Info, entered it, and the game said I won. The score shown was negative, and a second, different score appeared below it.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 50 repeatedly, secret was 19 | "Go lower" | "Go higher" every time, attempts ran out | none |
| Guess below the secret | "Go higher" | "Go lower" | none |
| Lose a game, then click New Game | New secret, game resets, input works again | Debug Info shows a new secret but the screen keeps the old ended state and blocks input until page refresh | none |
| Guess the secret taken from Debug Info | Win message and a positive score | Win message, but score is negative and a second score appears below it | none |

---

## 2. How did you use AI as a teammate?

I used Claude (Claude Code) to read the code, draft the fixes, write the tests, and draft this reflection. I looked at the code and the running app before and after each change.

A correct suggestion: moving `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py` and importing them in `app.py`. I checked it with `pytest` (14 passed) and by running the Streamlit app.

A suggestion I did not accept: Claude suggested that `parse_guess` reject decimal input like "19.9" instead of truncating it to 19. I kept the current behavior. The secret is a whole number, so a guess of "19.9" that counts as 19 is a reasonable result for this game. I checked it by calling `parse_guess("19.9")`, which returns `(True, 19, None)`, and I left the code and tests unchanged.

---

## 3. Debugging and testing your fixes

I counted a bug as fixed only when a test or a real run showed the correct behavior. For the hint bug, `test_too_high_hint_says_go_lower` checks that a guess above the secret says "LOWER". The test `test_guess_compares_as_numbers_not_strings` checks guess 50 against secret 19. The original code compared the secret as a string on even attempts, and "50" > "19" is false as strings, so this test guards against that. I did not run the old code against this test, so I cannot say it failed before the fix. Claude drafted the tests, and I ran them to confirm they pass on the fixed code.

---

## 4. What did you learn about Streamlit and state?

Every click reruns the whole script from top to bottom, so local variables start over each time. `st.session_state` is the only memory that survives those reruns. The New Game bug came from this: the code reset `attempts` and `secret`, but it did not reset `status`, so the saved "lost" state kept blocking input after the rerun.

---

## 5. Looking ahead: your developer habits

Reproduce the bug in the running app before changing code, and write the expected result next to it. The bug table in section 1 is what made the fixes easy to check.

Next time I want to check every state variable that a reset touches, not only the obvious ones.

Passing tests does not prove the app works. The New Game bug was only visible when I played through the UI.

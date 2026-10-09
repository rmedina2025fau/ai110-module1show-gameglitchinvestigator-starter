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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

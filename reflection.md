# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
   (for example: "the secret number kept changing" or "the hints were backwards").
  Answer:
  The first time I ran the game, the interface loaded and looked mostly playable, but the behavior was clearly inconsistent. One bug I noticed right away was that the hints were backwards: when my guess was lower than the secret number, the game sometimes told me to go lower instead of higher. I also noticed that invalid inputs like negative numbers, very large numbers, and decimals were still being accepted and processed as guesses. Another issue was that the hint did not always appear immediately after the first submit, which made the game feel delayed and confusing.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Answer:
  I used Copilot in VS Code and ChatGPT to help me understand the buggy logic before making changes. One correct AI suggestion was to check the comparison logic for the hint messages and verify whether the conditions for "Go Higher" and "Go Lower" were reversed. I verified that suggestion by manually testing guesses that were clearly above and below the secret number and comparing the result to the expected behavior. One misleading AI suggestion was that the problem might only be a UI display issue, but my manual testing showed the underlying game logic was also wrong because out-of-range guesses were still being treated as valid guesses.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
  Answer:
  I decided a bug was really fixed only after both automated tests and manual gameplay behaved correctly. I created pytest tests in `tests/test_game_logic.py` to verify the behavior of the `check_guess` function. The tests checked three cases: when the guess equals the secret number (should return "Win"), when the guess is higher than the secret (should return "Too High"), and when the guess is lower than the secret (should return "Too Low"). After running `python -m pytest`, all tests passed successfully.

  I also manually ran the Streamlit game and tried guesses above, below, and equal to the secret number to confirm that the hint messages ("Go Higher" and "Go Lower") appeared correctly during gameplay. AI helped me understand how to structure these tests and think about edge cases that might break the logic.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
  Answer:
  The secret number kept changing in the original app because Streamlit reruns the script whenever the user interacts with the page, and the secret was being regenerated during those reruns. I would explain Streamlit reruns to a friend by saying that the app feels interactive, but under the hood it often runs the script again from top to bottom after each button click or input change. Session state is what lets the app remember important values between reruns, like the secret number, score, attempts, and guess history. The change that finally made the game stable was storing the secret number in `st.session_state` and only resetting it when a real new game started.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  Answer:
  One habit I want to reuse is the practice of writing down specific test cases and expected outcomes before making code changes, which helps me stay focused on the actual behavior I want to achieve. Next time I work with AI on a coding task, I would be more cautious about accepting suggestions at face value and would make sure to verify them with manual testing or by reading the relevant documentation. This project made me realize that while AI can be a powerful tool for generating code, it can also produce incorrect or incomplete suggestions, so it's crucial to maintain a critical eye and not rely solely on AI for debugging or problem-solving.

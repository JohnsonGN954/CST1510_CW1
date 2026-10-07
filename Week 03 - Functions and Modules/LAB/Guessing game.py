"""# Number Guessing Game, upgraded

**Uses:** `random.randint()`

1. Open your Week 2 guessing game.
2. Add `import random` at the top of the file.
3. Find the line where you set the secret number.
4. Replace the fixed number with `random.randint(1, 100)`.
5. Run the game a few times and check that the secret number changes each time.

---

Stuck on why a function returning nothing gives you `None`? That's
`01 - Defining and Calling Functions`, section 4, in this folder."""



import random
secret_number = random.randint(1, 100)
print("secret number is", secret_number)


# 🧮 EXPONENTRON 1.0

A beginner-friendly CLI tool that takes a list of numbers and raises each to a specified power — with a little attitude.  
You enter the numbers — it obeys. Maybe.

---

## 🚀 Features

- Accepts integers and floats
- Gracefully handles:
  - Zero raised to a negative power (division by zero)
  - Negative numbers
  - Very large numbers (over 500)
- Strips trailing `.0` for integers (e.g., `2.0 → 2`)
- Fun and expressive output
- Loop support — run again without restarting

---

## Requirements
- Python 3

---

## 💻 Example

```bash
Enter numbers separated by spaces: 2 -4 0 501 3.5
Enter the power you want to raise each number to: 3
```

Output:
```
You entered the number 2 | Raised to the power of 3, it equals 8
-4 --- Negative? What do you think I am, a complex number calculator?
0 --- Easy there, zero raised to any power is still zero...
501 --- Whoa! Too big. Do the math yourself!
You entered the number 3.5 | Raised to the power of 3, it equals 42.875
```

---

## 📦 Usage

```bash
python exponentron.py
```

The program will ask for:
- A list of numbers (space-separated)
- The power to raise them to

---

## 🤖 Terminal Personality

```
----------------------------------------
🧮 Welcome to EXPONENTRON 1.0
----------------------------------------
You enter the numbers for computation — I obey. Maybe.
```

---

## 🧠 Why this project?

This project was built for:

- Practicing input handling and conditionals
- Getting familiar with loops and f-strings
- Having fun writing expressive CLI tools
- Adding a little soul to otherwise boring code

---

## 💡 What’s next?

Feel free to fork this project and add:

- File export of results
- Graph plotting
- Complex number support
- Unit tests (seriously, even robots need discipline)

---

## ✨ Author's note

This is part of a personal journey to master Python through playful, hands-on tools.  
**Exponentron** may be small, but it has attitude.

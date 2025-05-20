# Rolls Counter - Fate/Grand Order

Rolls Counter is a simple desktop application built with Python using tkinter. It is specifically designed for Fate/Grand Order (FGO) players who want to calculate how many summon rolls they can perform based on their available resources: Saint Quartz (SQ), SQ Fragments, and Summon Tickets.

🧠 What Does This App Do?

This tool allows the user to input:

    Number of Saint Quartz (SQ)

    Number of SQ Fragments

    Number of Tickets

It then automatically calculates the total number of rolls you can perform using the following conversion rules:

    3 SQ = 1 roll

    21 SQ Fragments = 1 SQ → 1 roll every 63 fragments

    1 Ticket = 1 roll

📦 Requirements

    Python 3.6 or higher

    No external libraries needed — uses Python’s built-in tkinter module

🚀 How to Use

 Clone or download this repository:

    git clone https://github.com/your_user/rolls-counter-fgo.git
    cd rolls-counter-fgo

 Or download directly from:
 
    https://github.com/SLMA-128/FGORollsCounter/releases/tag/Release

Run the application:

    python rolls_counter.py

Use the graphical interface:

    Enter the number of Saint Quartz, Fragments, and Tickets you have.

    The total number of summon rolls will be calculated automatically.

    Press "Close" to exit the program.

🧮 Example

If you input:

    90 SQ

    42 Fragments

    5 Tickets

The calculation will be:

    90 SQ → 30 rolls

    42 Fragments → 2 rolls (7 Fragments = 1 SQ, 21 Fragments = 3 SQ = 1 roll)

    5 Tickets → 5 rolls

Total: 30 + 2 + 5 = 37 rolls

📌 Notes

    Only numeric input is accepted. Empty fields are treated as 0.

    A lightweight, desktop utility intended to help FGO fans easily plan their summon sessions.

🛠️ Credits

Created by Sarmiento Leonardo
Inspired by the summoning mechanics of Fate/Grand Order. To count how many rolls you might have for a certain servant in the future. (I'll get Morgan this time!)

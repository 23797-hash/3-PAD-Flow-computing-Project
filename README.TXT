Flow Computing - Space Algebra Game
=====================================
Author: Janidu Hettiarachchi
Date: 2026
School: Lynfield College
Subject: 3PAD - Digital Technologies AS91907

PURPOSE
-------
A space-themed algebra learning game where players answer
maths questions across three difficulty levels to earn points.
Features a leaderboard, lives system, and loading screen.

HOW TO RUN
----------
1. Make sure Python 3 is installed on your computer
2. Install the required library by opening terminal/command prompt and running:

   pip install Pillow

   OR if that doesn't work:

   py -m pip install Pillow

3. Make sure the following files are in the SAME folder:
   - flow_computing.py
   - astronaut.png.png  (the astronaut image file)
   - scores.txt         (created automatically when you play)

4. Run the program:
   - Double click flow_computing.py
   OR open terminal in the folder and type:

   py flow_computing.py

LIBRARIES REQUIRED
------------------
- tkinter     (built into Python - no install needed)
- random      (built into Python - no install needed)
- os          (built into Python - no install needed)
- fractions   (built into Python - no install needed)
- Pillow      (NOT built in - must install with pip)

  To install Pillow:
  py -m pip install Pillow

HOW TO PLAY
-----------
1. Enter your username
2. Select a difficulty: Easy, Medium or Hard
3. Click START GAME
4. Answer 10 algebra questions
5. You have 3 lives - a wrong answer costs 1 life
6. Score 10 points for every correct answer
7. Complete all 10 questions to win and get on the leaderboard

DIFFICULTY LEVELS
-----------------
Easy   - Addition, subtraction, multiplication (numbers 1-20)
Medium - Multiplication, division, squares (numbers 2-12)
Hard   - Algebra, powers, square roots, fractions, Pythagoras

FILES IN THIS PROJECT
---------------------
flow_computing.py   - Main program file (run this)
astronaut.png.png   - Astronaut image used in the game
scores.txt          - Stores player scores (auto-created)
README.txt          - This file

TROUBLESHOOTING
---------------
- If the image doesn't load, make sure astronaut.png.png is in
  the same folder as flow_computing.py
- If Pillow is not installed you will see "image load failed"
  in the terminal - run: py -m pip install Pillow
- If scores.txt is missing it will be created automatically
  when you finish your first game

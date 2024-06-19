# 100 Prisoner Experiment 

## Overview
The 100-Prisoner Experiment is a probability and combinatorics problem that demonstrates how a group of prisoners can use a specific strategy to significantly increase their chances of all finding their own numbers in a set of drawers. The problem and the corresponding solution showcase interesting aspects of random processes and cooperative strategies.

#### Concept of the 100-Prisoner Experiment:
In the 100-Prisoner Experiment, there are 100 prisoners, each assigned a unique number from 1 to 100. There are also 100 drawers, each containing a unique number from 1 to 100, arranged randomly. Each prisoner is allowed to open up to 50 drawers in an attempt to find their own number. If every prisoner finds their number, all prisoners are freed. If even one prisoner fails to find their number, all prisoners are executed.

Key Rules:
- They are not allowed to talk after their attempt is over
- They are allowed to talk and formulate a stratagy before they start
- Each prisoner enters the room with the drawers alone
- Each prisoner can open up to 50 drawers.
- This process continues until the prisoner finds their own number or exhausts the 50 attempts.
- All prisions have to find their number

Strategy:
The strategy involves prisoners using a cyclic approach:
- Each prisoner starts with the drawer labeled with their number.
- They continue to open the drawer indicated by the number found in the previous drawer.
- This continues until they find their own number or use up all 50 attempts.

This method exploits the presence of cycles in permutations. Surprisingly, this strategy results in a success rate of over 30%, which is significantly higher than what random guessing would yield.

#### Installation
Install dependencies in a virtual environment:
    make install



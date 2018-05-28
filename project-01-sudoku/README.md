# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propogation is used to convey the reduction in domain of one variable to all the constraints imposed on the variable. In the naked twins problem, if we have two boxes in a unit containing two identical options, by virtue of the constraint on the unit to contain single instances of all digits between 1-9, we can infer that if one of the boxes contains one of the option, then by elimination, the other box has to contain the other option or the domain of the other box would be empty, hence leading to failure. From this inference, we also conclude that none of the other peers in that unit can contain either of the two values and hence their domains can be reduced further by eliminating two of the options. 

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonal sudoku problem is similar to the normal sudoku problem but with an added constraint.  The constraint is imposed on the boxes on the diagonals of the sudoku and is that, each of the elements in the diagonals has only one instance of the numbers from 1-9. Hence, when the value of one the boxes in the diagonal unit is determined, the peers of that box in the diagonal unit, cannot hold that value as an option and undergo a domain reduction. This domain reduction might lead to further assignments or an empty domain hence causing failure and invalidating the solution.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.


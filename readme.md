The experiment is comprised of three phases.
Each one of the phases uses the CET in order to get a ‘curiosity level’ score. At the end of the experiment,
 all ‘curiosity level’ scores are calculated into the final curiosity estimation.


Stage 0 - Setting up the program:
The user activates the program and gives his/her identification number. This id will be used for all files created by the program.
All other parameters should be set within the config files attached to the program. 

./main_kivy

**User Workflow - How to use the Program**\
***Stage 1***\
The user sees a screen split into two parts. 
On the left side is a column consisting of four buttons. The rest of the screen contains part of a graph.
No further information is displayed to the user.

The user has a set number of steps or a set amount of time to interact with the program. Afterwards, the screen goes black and a message indicating the end of the first stage is displayed as well as a button with the word “next”.

***Stage 2***\
A black screen is displayed with a column of four buttons on the left. These buttons are identical to the ones featured in part 1. On the rest of the screen a new graph is displayed. The user has a set number of steps to interact with the program, this amount is known to the user.
After the user finished interacting with the graph, the screen goes black a message is displayed for a predetermined amount of time.
	A fixed number of questions are shown on-screen and the user has to answer them. At the bottom of the screen there is a button with the word “submit” on it, the user presses this button after answering all of the questions. After answering the questions, a results page is shown. 
The left side of the results page shows each question, the answer the user gave, the correct answer taking into account the parts of the graph the user saw, and the optimal answer taking into account the entire graph. In addition two numerical values are displayed, indicating what percentage of questions the user answered correctly, one in relation to the part of the graph the user saw and the other in relation to the entire graph. On the right side the entire graph is displayed as well as an indication of which part of the graph the user saw. In addition a numerical value is displayed, indicating what percentage of the graph the user saw. 
	The steps described in part 2 are repeated a predetermined number of times.

***Stage 3***\
	A black screen with the a message indicating the end of the test is displayed.


What can the user see and do
Explanation about the program itself.
Buttons:
Each button is composed only of a random background image, consistent throughout the entire experiment. 
Each button has its own unique functionality, this functionality is consistent throughout the experiment and is not divulged to the user. 
Graph view:
Each graph consists of different colored nodes and white edges connecting them. 
Questionnaire:
The questionnaires contain a fixed number of questions that can be either multiple choice questions or open-ended questions.
 If a multiple choice question is displayed the user has to choose the correct answer out of the possible options.
If an open-ended question is displayed the user has a textbox to enter his/her answer. 




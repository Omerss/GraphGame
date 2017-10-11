## Directory Structure

#### Fonts
Folder used to store fonts for lab use - mainly to allow for hebrew text

#### GraphGeneration
Contains tools to allow us to create a tests graphs manually.
* [GraphGenerator](GraphGeneration/GraphGenerator.py) - Allow enumerating over all steps to make sure the graph has only a single solution.
* [HandmadeGraph](GraphGeneration/HandmadeGraph.py) - Allows creating graphs manually
* [KivyRunner](GraphGeneration/KivyRunner.py) - Allows to view a graph or play it without any other functionality

#### GraphsData
Contains all the graphs used in the main game. All graphs are in xml format.
* [graph_config](GraphsData/graph_config.txt) -
 A config files used by all the graphs when they are loaded.
 Parameters about the structure of the graphs
* [graph_config](GraphsData/questions_format.txt) - A guide on how to insert questions into the graph xml

#### Images
Contains images used in the project and game

#### KivyCommunication
Communication modules used by the lab. External code to program
* [kivy_logger](KivyCommunication/kivy_logger.py) - Main logger file. Sends data to server in lab
* [logged_widgets](KivyCommunication/logged_widgets.py) - Used for logging specific actions of widgets
* [twisted_client](KivyCommunication/twisted_client.py)  - Used by my logger for client-server interactions

#### KivyFiles
Contains almost all of the kivy files used in the project
***Questions Folder***\
Contains Kivy files used in the questionnaire and the result screen.
* [AnswerObject](KivyFiles/Questions/AnswerObject.py) - An objects that holds all data about a question, including the answer the user gave, the answer
as seen in both the graph discovered by the user and in the true graph. Used by the result screen.
* [QuestionObject](KivyFiles/Questions/QuestionObject.py) - A question object is used in the questionnaire. Holds information
about a question and the answers given to it.
* [QuestionsAnswers](KivyFiles/Questions/QuestionsAnswers.py) - Answers a question based on the type of question, the graph given and other arguments.
* [QuestionsDisplay](KivyFiles/Questions/QuestionsDisplay.py) - Holds Question display and QuestionnaireWidget. Used to display the actual questionnaire.
* [QuestionWidgets](KivyFiles/Questions/QuestionWidgets.py) - A widget used to hold the kivy information about a question for display proposes.
* [ResultDisplay](KivyFiles/Questions/ResultDisplay.py) - Holds ResultDisplay and ResultWidget. Used to display the result screen.

***Main Folder***\
* [GameLayout](KivyFiles/GameLayout.py) -
* [GraphButton](KivyFiles/GraphButton.py) -
* [GraphDisplay](KivyFiles/GraphDisplay.py) -
* [GraphLayout](KivyFiles/GraphLayout.py) -
* [GraphTabletGame](KivyFiles/GraphTabletGame.py) -
* [KivyEdge](KivyFiles/KivyEdge.py) -
* [KivyGraph](KivyFiles/KivyGraph.py) -
* [KivyNode](KivyFiles/KivyNode.py) -

#### QLearning
Contains the Q learner and resulting files
* [QLearner](QLearning/QLearner.py) -Holds Qplayer and QMatrix.
QMatrix is contains the matrix used to calculate each step.
The player runs a series of games (episodes) that allow the QMatrix to be built up over time.

#### ScrapPad

#### SupplementaryFiles
#### Testing
#### TestingGraphs
#### Main

./main_kivy

## User Workflow - How to use the Program
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




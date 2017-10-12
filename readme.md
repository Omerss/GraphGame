## Directory Structure

#### Fonts
Folder used to store fonts for lab use - mainly to allow for hebrew text

#### GraphGeneration
Contains tools to allow us to create a tests graphs manually.
* [GraphGenerator](GraphGeneration/GraphGenerator.py) - Allow enumerating over all steps to make sure the graph has only a single solution.
* [HandmadeGraph](GraphGeneration/HandmadeGraph.py) - Allows creating graphs manually.
* [KivyRunner](GraphGeneration/KivyRunner.py) - Allows to view a graph or play it without any other functionality.
* [CreateRandGraph](GraphGeneration/CreateRandGraph.py) - Creates random graphs.

#### GraphsData
Contains all the graphs used in the main game. All graphs are in xml format.
* [graph_config](GraphsData/graph_config.txt) -
 A config files used by all the graphs when they are loaded.
 Parameters about the structure of the graphs
* [questions_format](GraphsData/questions_format.txt) - A guide on how to insert questions into the graph xml

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
* [GameLayout](KivyFiles/GameLayout.py) - Controls the displaying of the entire game. Contains the GraphLayout and the buttons.
* [GraphButton](KivyFiles/GraphButton.py) - Graph buttons a sophisticated WidgetButton that allows greater functionality in the application.
* [GraphDisplay](KivyFiles/GraphDisplay.py) - A layout that allows the entire graph to be displayed onscreen.
* [GraphLayout](KivyFiles/GraphLayout.py) - A kivy layout that contains the graph in a format that can be displayed.
* [GraphTabletDisplay](KivyFiles/GraphTabletDisplay.py) - Controls the game playing, also responsible for sending out the information seen onscreen.
* [KivyEdge](KivyFiles/KivyEdge.py) - A connection between two kivy nodes is a KivyEdge.
* [KivyGraph](KivyFiles/KivyGraph.py) - Graph object use by the graph layout to hold information about the graph.
* [KivyNode](KivyFiles/KivyNode.py) - Node objects use by the kivy graph to hold information about each node.

#### QLearning
Contains the Q learner and resulting files
* [QLearner](QLearning/QLearner.py) - Contains Qplayer and QMatrix.
QMatrix holds the matrix used to calculate each step.
QPlayer runs a series of games (episodes) that allow the QMatrix to be built up over time.

#### ScrapPad
Used for personal files

#### SupplementaryFiles
* [Enums](SupplementaryFiles/Enums.py) - Holds all enums used in the repository
* [GameDataHandler](SupplementaryFiles/GameDataHandler.py) - The main class that handle all graph data. Tracks information about the graph,
connections, false nodes, partial knowledge etc.
* [GraphObj](SupplementaryFiles/GraphObj.py) - Graph Objects hold all the data about a graph.
 All actions on the graph itself are done through this object
* [LoadGraph](SupplementaryFiles/LoadGraph.py) - Loads a graph from an xml file. Returns a GraphObj
* [SaveGraph](SupplementaryFiles/SaveGraph.py) - Saves a GraphObj into a readable xml file
* [NodeObject](SupplementaryFiles/NodeObject.py) - Node Objects as the basis of all graphs.
 Any action taken by or on a node is done through this object
* [Point](SupplementaryFiles/Point.py) - Inherited by the NodeObject. A point with functionality.
* [LineEquation](SupplementaryFiles/LineEquation.py) - Used to create a line equation for calculations.
Used to understand how nodes connect to each other in space.
* [RepeatedTimer](SupplementaryFiles/RepeatedTimer.py) - Used by GameLayout to run threads
* [Utils](SupplementaryFiles/Utils.py) - Contains general functions used all around the repository

#### Testing
Contains testers for the projects
* [RunAllTests](Testing/RunAllTests.py) - The starting point of the application.

#### TestingGraphs
Graphs that are still under construction

#### Main Folder
* [Main](Main.py) - The starting point of the application.
* [GraphGameScreen](GraphGameScreen.py) - The screen object that holds the graph game part of the app. All graph interactions start here.
* [QuestionnaireScreen](QuestionnaireScreen.py) - The screen object that holds the questionnaire part of the app. All questionnaire interactions start here.
* [ResultsScreen](ResultsScreen.py) - The screen object that holds the result part of the app.
Building the widget that displayed the results to the user are constructed under this.


## Kivy flow
When setting up the game we need to load all the game screen. Each screen consists of three objects:
1) A kivy screen object. Each screen is independent from the other. The game moves between the screens as the game progresses.
2) A display object. These classes are none kivy objects that connect the screen objects to the kivy layouts
3) A kivy layout. The layout holds all the widgets that are displayed on the screen.
We load the objects in sequence: Screen -> Display -> Layout
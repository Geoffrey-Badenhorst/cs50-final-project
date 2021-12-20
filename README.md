# Guess those Trends!
#### Video Demo:  <URL HERE>
#### Basic Description:  A web app game about trending results and which is less or more popular

#### Libraries
The following libraries were used for this project
- [PyTrends](https://pypi.org/project/pytrends/)

### Website Names
index (homepage introduction)\
rules (how game works)\
game (User has to pick an option between the two on what they think is the greater of the two)\

Display button leading back to index
- loss (Display if user guessed wrong)
- win (Display if user is right)

### Process
User gets taken to an index homepage site to introduce the game, then takes them to a rules page explaining the game a little bit more.\
The site sources out the list of trends using the pytrends API, saving them in a list before picking two random trends, then finding the more popular of the two.\
The site takes the user to the game page with with the results are put into different buttons and if they guess correctly, the cycle would continue for five rounds.\
If the user gets it all right, it'll display the winning page with the list of trends or else display the lose page.\
A pair of buttons on several pages takes the user back to either the home page or the game page where they can start the whole process again.

### Design Reasoning
The app was kept minimal with a lot of white and white space being used with small pops of colour to keep it from being too bland, such as with the game name, the logo icon and the footer line.\
The tiger cub was then brought in to add some life to the app with reactions to suit the situations under which they were being used.\
A good flow during the game is kept up using a series of buttons for navigations, keeping things simple.

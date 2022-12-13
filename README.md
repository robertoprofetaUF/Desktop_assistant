# Desktop_assistant
Desktop assistant called Hasbulla is similar to Siri and Alexa. It is capable of interacting with the users to answer questions by searching in the web, play videos, open and close apps, among other things.

The imported packages are the following with the use given to them:

Pyttsx3 -- It is the module used to interpretate text and make the program talk. As it will be explained below, is the package that allowed us to make the program speak.

SpeechRecognition -- The use of this package is pretty self explanatory with its name. It allows our program to intepreatate voice inputs and transcript them to the strings that move the program.

Datetime -- Package used to retrieve date and time information

Wikipedia -- Package used to retreieve information from wikipedia to answer questions with web information.

Webbrowser -- Package used to work with web browsers as the name implies.

Subprocess -- Open applications

OS -- Package to access to system capabilities.

Pywhatkit -- Web page interactions

OpenAI -- Package from the company with same name, that allow us to introduce the capability to the program of generating images with the API Artifial Intelligence. A key was retrieved and placed in the code giving us access to 50 images per month.



The greetMe() function introduces Hasbulla every time the code runs. 
The takeOrder() function uses the micrphone of the computer to retrieve the voice inputs from the user. We use a recognizer from Google to use English as the set language. With this function ready, we can start to explain the logic and how to interact with the assistant for it to make what we want. 

The main portion of the code is composed of a while loop that stays active as long as the user does not say the word 'goodbye' or 'stop'. This loop has several nested if statements that react to the voice inputs. Once Hasbulla is ready to receive the command, it will say 'Ready to listen..."

The following list has all the strings that must be said to trigger each action

'How are you':
Hasbulla responds cordially

'Play' and 'on youtube':
Hasbulla plays the first video that matches what was said by the user using pywhatkit.

'Create image':
Hasbulla generates an image based on the command said by an user. The image is created using the function open.Image.create() and is displayer in chrome using webbrower()

'Time is':
The user can ask 'what time is it?' and Hasbulla will respond with the current time.

'Date' and 'Today':
The user can ask 'What is today's date?' or something containing the mentioned words and Hasbulla will respond with the current date.

'Search' , 'What is' or 'Who is:'
With these combinations of words, Hasbulla will look first fro matches in Wikipedia using the Wikipedia API to provide a summary of two sentences (this can be easily modified in the arguments). If the program does not find any direct match between what was said by the user and Wikipedia, it will just open Google and show the search results for the user input.

'Run':
These word followed by other inputs such as 'microsoft excel' or 'spotify' opens programs that are in the computer. Cirrently, the programs that can be run using this feature are Microsoft Word, Microsoft Excel, Microsoft Powerpoint, Spotify, and Minecraft. 

'Open':
These word has to be followed by the name of a webpage such as youtube and it will open a tab in google for any .com page requested. This is done utilizing the webbrowser package.

'Exit':
This word closes the open programs in the computer with the use iof os.system() function.

'Goodbye' or 'Stop':
These two words are the ones that change the active state of the loop to false. This will make Hasbulla wish us a good day and let us know that he is there for us whenever we needed him.

Every time Hasbulla does not understand a command, it will say it and automatically be ready to receive a new one. 

It is important to mention that the proper performance of this desktop_assistant relies significantly in the correct function of the computer microphone from where it is being reproduced. In other words, Hasbulla will work its best with a quality microphone.


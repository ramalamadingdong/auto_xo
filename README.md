# auto_xo
I made this project to create a signal based way to submit Trip Tickets to the XO without needing to go to the talk and submit a paper copy.
It take inputs from any text messages and looks for this format:
```
Please edit the following trip ticket:

DEST: XXXXXX 
MIS: XXXX
NCOIC: XXXX
VIX 1: BUMPER#, DRIVER, TC, PAX1, PAX2
VIX 2: BUMPER#, DRIVER, TC, PAX1, PAX2
VIX 3: BUMPER#, DRIVER, TC, PAX1, PAX2
VIX 4: BUMPER#, DRIVER, TC, PAX1, PAX2
VIX 5: BUMPER#, DRIVER, TC, PAX1, PAX2
```
Then the script will update a Google Sheets with all the information pushed from the ticket above. 
I hosted the server on a local machine that I keep running 24/7 and used a Google Voice Number so that it wouldn't affect my personal Signal. 
(for more instructions on how to set this up please let me know)



## Some additional Instructions:

To create a free Google Server to host this you can follow the steps on this https://pathowe.co.uk/get-a-free-linux-server-with-google-cloud-services/

To create a free Google voice number: 
https://support.google.com/voice/answer/115061?co=GENIE.Platform%3DDesktop&hl=en

To get Signal to work on the Linux machine:
follow the instructions in https://github.com/AsamK/signal-cli#install-system-wide-on-linux 
I noticed the last command doesn't work just use cd to navigate to /bin/signal-cli and run all ./signal-cli from there

Follow Usage Instructions: 
https://github.com/AsamK/signal-cli#usage once that is setup you can send and recieve messages from Linux command line!
Then launch a shell with tmux and run ./signal-cli daemon

Then download auto_xo.py and follow gspread instructions 
https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project to create the creds.json
once all is setup and changed all the phone numbers run another shell tmux session and run ./auto_xo.py



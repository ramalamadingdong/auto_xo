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

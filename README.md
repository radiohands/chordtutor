# chordtutor

Typing program for learning chording for the artsey.io layout. https://artsey.io
(think Mavis Beacon Teaches Typing)

------------
######  How it looks:
<p align="center">
	<img src="https://radiohands.com/chayzer/cht_01.png" alt="Screen 1">	
	<img src="https://radiohands.com/chayzer/cht_02.png" alt="Screen 2">
</p>

------------
## How to install:
The program uses python along with they "pygame" library. You should be able to run this on any OS that supports python.
1. Install  Python 3 - https://www.python.org/downloads/ (click "add python to path, and then restart)
2. Make sure it is able to run from the command line and add the "pygame" library (if you didn't hit "add python to path" you have to add it and pip manually)
	- pip install pygame
3. Clone the program, extract it to a directory and run it
	- python main.py

------------
## Options you can change
- **refDelay = #** -- This sets how long until the layout "helper" pops up, too slow and you have to wait for it to give you help on an unfamiliar chord, too fast and you'll get the "I KNEW THAT! GIVE ME A MINUTE!" feeling...

- **myFont = 'font'** -- Change this if you really want a different font, if it's not monospaced it breaks the layout. lol.

- **darkMode = False/True** -- Allow for dark mode. Kinda nice if you plan on staring at the screen for a while. Off by default.

- **scale = False/True** -- Setting this to True will double the screen size. Nice for small monitors or big resolutions.

- **fpsLimit = #** -- Sets the FPS. If you have this too high it will attempt to run it at that speed at all costs. Keeping it low keeps the CPU happy.
## What??
When learning a new keyboard layout I get frustrated trying to do it from scratch. I always liked how we all learned it in school, using a program that hand feeds you the letters piece by piece.

I decided to throw this together in order to learn the new layout by programming with it (well, some of it) and running through the exercises. I just kind of threw it together and wasn't going to complete it but I figured I could put a basic finish on it just in case it came in handy for someone else.

For more information about the layout checkout the project page https://artsey.io
(not my project)
## Are you giving up on this project?
Not really.
I'll poke in from time to time and add things. Always intended there to be a couple typing games instead of the two pointless stories at the end.
Saying that, this code is free with a very basic license, feel free to copy, clone, modify, sell (lol) to your hearts content.

Feel free to throw in any bug reports that don't involve "I can't get python/pygame to run on my system", or "why do you suck at programming?"...

✌️
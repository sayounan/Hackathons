# Hackathons
This is a collection of work or puzzles I solved in hackathons.
## Deloitte Hackathon (Total Time: 9 hrs.)
## Solve Times
- [CANBus log](/CAN.log) + [Dashboard Recoding](/Dashboard.mkv):<br />~90 mins.
- [chall.py](/chall.py) + [chall_edited.py](/chall_edited.py) + [example.py](/example.py):<br />~6 hrs.
- [Comp.py](/Comp.py) + [Dashboard.mkv](/Dashboard.mkv):<br />~90 mins.
- [Mayday.wav](/Mayday.wav):<br />~5 mins
- [out.txt](/out.txt):<br />~5 mins
### CAN.log
CANBus log from a "Tesla" used alongside a [Dashboard Recoding](/Dashboard.mkv). Prompt was to watch the dashboard 
recording and use that to find the CANBus log code for door opened and door closed events based on the video.
### chall.py
A challenge source code that rquired a guess before generating the flag and only confirmed if the guess was correct or 
not.
### chall_edited.py
Personal edit of [chall.py](/chall.py) where after learning what the imported library does and how it works, rewrote the 
code to become a writer instead of a guesser.
### Comp.py
Imported the [CANBus log](/CAN.log) and listed the codes in ascending order of occurrence frequency.
### Dashboard.mkv
A video recording of a "Tesla" dashboard to be used alongside [CANBus log](/CAN.log) to gain information about the codes
corresponding to the events of interest.
### example.py
An example of how the library in [chall.py](/chall.py) worked.
### Mayday.wav
An audio file containing "morse code from a sinking Italian ship." The morse code decoded into a shift cypher (Key: 6)
### out.txt
A text file with a hidden flag. It was simply the first letter of each word.
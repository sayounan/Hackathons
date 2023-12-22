# Sari I. Younan
# Hackathons
This is a collection of work or puzzles I solved in hackathons.
<details><summary>Deloitte Hackathon (Total Time: 9 hrs.)</summary><blockquote>

####
<details><summary><code style='color : red'>⏳ Solve Times</code></summary><blockquote>

- [CANBus log](/CAN.log) + [Dashboard Recoding](/Dashboard.mkv):<br /><code style='color : red'>~90 mins.</code>
- [chall.py](/chall.py) + [chall_edited.py](/chall_edited.py) + [example.py](/example.py):
<br /><code style='color : red'>~6 hrs.</code>
- [Comp.py](/Comp.py) + [Dashboard.mkv](/Dashboard.mkv):<br /><code style='color : red'>~90 mins.</code>
- [Mayday.wav](/Mayday.wav):<br /><code style='color : red'>~5 mins</code>
- [out.txt](/out.txt):<br /><code style='color : red'>~5 mins</code>
</blockquote></details>

### [CAN.log](/CAN.log)
CANBus log from a "Tesla" used alongside a [Dashboard Recoding](/Dashboard.mkv). Prompt was to watch the dashboard 
recording and use that to find the CANBus log code for door opened and door closed events based on the video.
### [chall.py](/chall.py)
A challenge source code that rquired a guess before generating the flag and only confirmed if the guess was correct or 
not.
### [chall_edited.py](/chall_edited.py)
Personal edit of [chall.py](/chall.py) where after learning what the imported library does and how it works, rewrote the 
code to become a writer instead of a guesser.
### [Comp.py](/Comp.py)
Imported the [CANBus log](/CAN.log) and listed the codes in ascending order of occurrence frequency.
### [Dashboard.mkv](/Dashboard.mkv)
A video recording of a "Tesla" dashboard to be used alongside [CANBus log](/CAN.log) to gain information about the codes
corresponding to the events of interest.
### [example.py](/example.py)
An example of how the library in [chall.py](/chall.py) worked.
### [Mayday.wav](/Mayday.wav)
An audio file containing "morse code from a sinking Italian ship." The morse code decoded into a shift cypher (Key: 6)
### [out.txt](/out.txt)
A text file with a hidden flag. It was simply the first letter of each word.
</blockquote></details>
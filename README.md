# Sari I. Younan
# Hackathons
This is a collection of work or puzzles I solved in hackathons.
![alt text](images/Deloitte-Logo.png)
<details><summary>Dec. 2023 Mountain West Cyber Challenge by Hackazon & Deloitte (Total Time: 9 hrs.)</summary><blockquote>

####
<details><summary>⏳ Solve Times</summary><blockquote>

- [Connected Car](#Connected-Car):<br />~2 hrs.
- [Logic Analysis](#Logic-Analysis):<br />~6.5 hrs.
- [Mayday](#Mayday):<br />~5 mins.
- [Find The Hidden Message](#Find-The-Hidden-Message):<br />~5 mins.
</blockquote></details>

<details><summary>Challenges</summary><blockquote>

# Connected Car
- **Dependencies/Auxiliaries:** [Dashboard Recoding](/Dashboard.mkv), [CANBus log](/CAN.log), and [Solution](/Comp.py)
- **Prompt:** Watch the [Dashboard Recoding](/Dashboard.mkv) and use that to help find the [CANBus log](/CAN.log) code for door opened and door closed events based on the video.

#### [CANBus log](/CAN.log)
- **Description:** CANBus log from a "Tesla."

#### [Dashboard Recording](/Dashboard.mkv)
- **Description:** A video containing a few second recording of a "Tesla" dashboard.

#### [Solution](/Comp.py)
- **Description:** Python code to sort the frequency of code occurrences in the [CANBus log](/CAN.log) in ascending order, as there was only one door opened event and only one door closed event based on the [Dashboard Recording](/Dashboard.mkv).  

# Logic Analysis
- **Dependencies/Auxiliaries:** [Example Code](/example.py), [Challenge](/chall.py), & [Solution](/chall_edited.py)
- **Prompt:** [Challenge](/chall.py) takes user input for a potential flag, generates the flag based on 32 XOR conditions, compares the guess with the generated flag, confirms or denies a match between the two. Find the flag.

#### [Example Code](/example.py)
- **Description:** Example python code containing the library that performs the logic.

#### [Challenge](/chall.py)
- **Description:** Provided source code that takes and stores a user input guess for the flag, generates the flag then confirms or denies if the guess was correct.

#### [Solution](/chall_edited.py)
- **Description:** Personal edit of [Challenge](/chall.py) where after learning what the imported library does and how it works, rewrote the code to become a writer instead of a guesser.

# Mayday
- **Dependencies/Auxiliaries:** [Morse Code Audio File](/Mayday.wav)
- **Prompt:** This is a recorded signal broadcast by a sinking ship. Find the flag in the broadcast.

### [Morse Code Audio File](/Mayday.wav)
- **Description:** Audio file containing the broadcast morse code.

### Solution
- Decoded using online morse code decoder, returned a string of text that was not recognizable language but had a noticeable pattern. Immediately chose to use an online shift cypher decoder to find the flag.

# Find The Hidden Message
- **Dependencies/Auxiliaries:** [Text File](/out.txt)
- **Prompt:** Find the hidden message within the [Text File](/out.txt).

### [Text File](/out.txt) 
- **Description:** Text file containing a paragraph.

### Solution
- First guess was to try extracting the first letter of every word as the paragraph made no grammatical, syntactical, or logical sense. The resulting string revealed the flag by spelling out the numbers and directly providing the letters.

</blockquote></details>
</blockquote></details>
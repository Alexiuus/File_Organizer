# File organizer for Linux
## Resume

Program that sort folders and files in the directories given as argument.

## Functioning

Run the program giving as argument the directories to be sorted (the directory address must start from the desktop/Escritorio). for more help, run:

```
File_Organizer$ python3 run.py
Running mode:

[STANDARD] Sort folders and files in the directories given as argument. For running:
   python3 run.py "<directory1>" "<directory2>" ... "<directoryN>"

[MONO] Sort folders and files on the <nameFolder> that meets a <condition>
       (that condition is a word found in the names of the folders and files
       to sort) on the directories given as argument. For running:
   python3 run.py -l <nameFolder> <condition> <directory>

[HELP] For run:
   python3 run.py --help
   python3 run.py
```

in the CMD.
# Integrate Pyannote
Whisper Mate 5.5.2 start to support pyannote (https://github.com/pyannote/pyannote-audio)
Cause the macos sandbox app permission issue, You need manual do some steps to use it as diarization in Whisper Mate

# First time use setup
---
1.Set an sync folder to auto export pyannote needed audio.wav file
2.Place the pyannote.py to step-1 folder

# Every project manual exec
---
1.When project added to Whisper Mate after start process, copy the shell command to exec it in terminal
```sh
python pyannote.py project-id.wav
```
2.Done (MacOS Sandbox App can't auto execute outside shell script)

> Whisper Mate will auto monitor the sync folder to wait for the pyannote.py result file generate, when pyannote.py execute finish will create project result file
> Whisper Mate then auto load the result file to task, when transcribe complete auto use the pyannote result to put the speaker data to row

You also can manual paste the pyannote result to Whisper Mate then press parse to set speaker data


> use replace feature to batch replace  @Speaker_01 to Sam 
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") # please follow the pyannote github to get your huggingface api auth token https://github.com/pyannote/pyannote-audio

import sys
import torch
pipeline.to(torch.device("cpu"))

wav = str(sys.argv[1])
pid = wav[:-4]
if len(sys.argv) >= 3:  
    speakers = int(sys.argv[2])  
else:  
    speakers = 0 

if speakers == 0:
    print(f"Processing file {wav}")
    diarization = pipeline(wav)    
else:
    print(f"Processing file {wav} with speaker count -> {speakers}")
    diarization = pipeline(wav, num_speakers=speakers)
    
output_file = open(f"{pid}.txt", "w") 
# print the result and generate the result to txt, then Whisper Mate will auto load the result txt back to project and fill to speaker column
for turn, _, speaker in diarization.itertracks(yield_label=True):
    output_file.write(f"start={turn.start:.2f}s stop={turn.end:.2f}s {speaker}\n")
    print(f"start={turn.start:.2f}s stop={turn.end:.2f}s {speaker}")

output_file.close()
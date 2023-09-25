import demucs.separate

options = ["sample/no_vocal.wav",
           "-n", "htdemucs",
           #"--two-stems", "vocals",
           "--mp3"]

demucs.separate.main(options)
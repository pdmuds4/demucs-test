import demucs.separate

options = ["sample/no_vocal.wav",
           "-n", "htdemucs",
           "--two-stems", "vocal",
           "--mp3"]

demucs.separate.main(options)
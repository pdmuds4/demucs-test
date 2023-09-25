import demucs.separate as ds
import ffmpeg, os, enum #ffmpeg-python

class Model(enum.Enum):
    htdemucs = "htdemucs"
    htdemucs_ft = "htdemucs_ft"
    htdemucs_6s = "htdemucs_6s"
    hdemucs_mmi = "hdemucs_mmi"
    mdx = "mdx"
    mdx_extra = "mdx_extra"
    mdx_q = "mdx_q"

class Stem(enum.Enum):
    vocals = "vocals"
    drums = "drums"
    bass = "bass"
    other = "other"

class Format(enum.Enum):
    int24 = "int24"
    float32 = "float32"
    mp3 = "mp3"
    flac = "flac"

def demucs_separate(track, model_name:Model=None, stem:Stem=None, format:Format=None):
    convert_path = os.path.dirname(__file__)+"/sample/"+os.path.basename(track)
    if convert_path.endswith(".wav"):
        pass
    else:
        convert_path = convert_path.split(".")[0]+".wav"

    try:
        ffmpeg_input =  ffmpeg.input(track)
        ffmpeg_output = ffmpeg.output(ffmpeg_input, convert_path)
        ffmpeg.run(ffmpeg_output, overwrite_output=True)
    except:
        print("[Error] ffmpeg convert error")

    else: # create options
        options = [convert_path]
        if model_name and isinstance(model_name, Model):
            options.extend(["-n", model_name])
        elif stem and isinstance(stem, Stem):
            options.extend(["--two-stems", stem])
        elif format and isinstance(format, Format):
            options.extend(["--"+format])
        print(f"[Options]:{options}")
        ds.main(options)

if __name__ == "__main__":
    demucs_separate("/Users/pam/Downloads/BGM/Soleily&Sanaas Collection/Road To Glory.mp3")
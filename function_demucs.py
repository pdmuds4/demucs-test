import demucs.separate as ds
import ffmpeg, os #ffmpeg-python


def demucs_separate(track, model_name:str=None, stem:str=None, format:str=None):
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
        if model_name:
            options.extend(["-n", model_name])
        elif stem:
            options.extend(["--two-stems", stem])
        elif format:
            options.extend(["--"+format])
        ds.main(options)

if __name__ == "__main__":
    demucs_separate("/Users/pam/Downloads/BGM/Soleily&Sanaas Collection/Road To Glory.mp3")
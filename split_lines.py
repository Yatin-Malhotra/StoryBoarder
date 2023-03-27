import audio as ad
import movie as mv

def read_script(script):
    lines = script.splitlines()
    length = len(lines)

    for i in range(length):
        ad.generate_movie_clip(lines[i], i)
    
    mv.generate_movie(length)

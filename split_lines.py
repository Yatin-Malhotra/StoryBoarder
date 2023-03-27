import audio as ad
import movie as mv
import images as im

def read_script(script, model):
    lines = script.splitlines()
    updated_lines = []
    for i in range(len(lines)):
        if (lines[i].strip() != '' and lines[i].strip() != '\n'):
            updated_lines.append(lines[i])
    length = len(updated_lines)

    for i in range(length):
        im.image_generator(updated_lines[i], model, i)

    for i in range(length):
        ad.generate_movie_clip(updated_lines[i], i)
    
    mv.generate_movie(length)

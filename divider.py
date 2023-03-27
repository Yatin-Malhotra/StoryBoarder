import re
import storyboard as sb
import collage as cg
import audio as ad
import movie as mv

def divide_script(script, num_parts, model):

    print("Inside divide script function")
    # Split the script into sentences
    sentences = re.findall('[A-Z][^\.!?]*[\.!?]', script)
    
    # Determine the number of sentences per part
    num_sentences_per_part = len(sentences) // num_parts
    
    # Initialize a list to hold the divided script parts
    parts = []
    
    # Divide the sentences into parts
    for i in range(num_parts):
        # Determine the start and end indices of the current part
        start = i * num_sentences_per_part
        end = start + num_sentences_per_part
        
        # Adjust the end index of the last part to include any remaining sentences
        if i == num_parts - 1:
            end = len(sentences)
        
        # Extract the sentences for the current part and join them into a string
        part_sentences = sentences[start:end]
        part = ' '.join(part_sentences)
        
        # Add the current part to the list of parts
        parts.append(part)

    # print("Parts", parts)
    
    for i in range(len(parts)):
        # print("Giving storyboard the input")
        sb.storyboard_generator(parts[i], model, i)
    
    cg.collage(len(parts))


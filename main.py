from PIL import Image
import custom_story as cs
import divider as dd
from termcolor import colored
import split_lines as sl

def main():
    title = colored("Welcome to the StoryBoarder\n", "red")
    print(title)
    print("A program that will write a script according to your needs and will show a storyboard for that script")
    print("Menu:\n")
    print("1. Generate a script and the storyboard")
    print("2. Generate storyboard for my script")
    print("3. Thumbs Up!")
    print("4. Exit")
    
    user_input = int(input("Choose the number: "))
    if (user_input == 1):
        genre = input("Enter the genre of the movie: ")
        description = input("Enter the description for the movie: ")
        num_storyboards = int(input("Enter the # storyboards: "))
        model = input("Enter the model: ")
        script = cs.Custom_Script(description, genre)
        print("Get ready for your awesome script: \n")
        print(script)
        print("working on the storyboards")
        dd.divide_script(script, num_storyboards, model)
        print("generated the storyboards")
        image = Image.open("collage.png")
        image.show()
        sl.read_script(script, model)
    elif (user_input == 2):
        script = input("Enter your script: ")
        dd.divide_script(script, num_storyboards, model)
        image = Image.open("collage.png")
        image.show()
        sl.read_script(script, model)
    elif (user_input == 3):
        print("Displaying a thumbs up (our presentors are)")
    elif (user_input == 4):
        print("Goodbye!")
        quit()
    else:
        print("Invalid error :(\n")
        main()


main()

import os


def main():
    # """Program to consistently name files."""
    # print("Starting directory is: {}".format(os.getcwd()))
    #
    # # Change to desired directory
    # os.chdir('Lyrics\Old')
    #
    # for directory_name, subdirectories, filenames in os.walk('.'):
    #     # print("Directory:", directory_name)
    #     # print("\tcontains subdirectories:", subdirectories)
    #     print("\tand files:", filenames)
    #     # print("(Current working directory is: {})".format(os.getcwd()))

    filenames = ['Cornerstone.txt', 'GloryToGodForever.txt', 'GodOfThisCity.txt']

    for filename in filenames:
        # full_name = os.path.join(directory_name, filename)
        new_name = get_fixed_filename(filename)
        # new_name = os.path.join(directory_name, get_fixed_filename(filename))
        # os.rename(full_name, new_name)
        print(new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name = ''
    # words = list(enumerate(filename))
    # for word in words:
    #     name.join(word[1])
    # print(words)
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    # return new_name
    for letter in enumerate(filename):
        word = ""
        x = letter[1]
        new_word = word + x
        if x.islower():
            position = letter[0]
            if


main()

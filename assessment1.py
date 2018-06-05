"""
Student Name: Ye Yint Thet Khine
Student ID:13539860
Date: 19/04/2018
This is the program that help people to learn the song by providing the song adding feature
and the mark as complete features.
Github: https://github.com/CP1404-2017-2/a1-YeYintThetKhine/blob/master/assignment1.py
"""


from operator import itemgetter  # import the itemgetter function from the operator
Filename = "songs.csv"  # import the song.csv function to the program


def main_menu():  # The function that request the menu choice
    prompt = "Menu:\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n>>> "  # Asking for menu input
    selection = input(prompt).upper()  # Making the input into capital letters
    while selection not in list("LACQ"):
        print("Invalid menu choice")
        selection = input(prompt).upper()  # Re-Asking for menu input
    return selection  # Return the menu input


"""
loading songs
    list_of_song = list
    in_file = open songs.csv (r)
    for line in in_file
        remove new character
        song_artist_year_list = split line for ","
        list_of_song = append song_artist_year_list
    return list_of_song
"""


def loading_songs():  # loading the_songs function opens the songs file and imput them to song_list
    list_of_song = []
    in_file = open(Filename, 'r')  # "r" the meaning of read
    for line in in_file:  # to use the for loop
        line = line.strip("\n")  # to strip the line
        song_artist_year_list = line.split(",")  # to split the line to the datum list
        list_of_song.append(song_artist_year_list)  # to save all the "song_artist_year_list" in file_list. inside file_
    in_file.close()  # to close #                     list is the "song_artist_year_list (list)"
    return list_of_song  # return Song_list


def display_song_list(list_of_song): # display_song_list function prints a formatted table of songs from song_list
    count = 0  # to declare the variable and start form 0
    for i in range(len(list_of_song)):  # make the constant "i"
        if list_of_song[i][3] == "y":  # make the program to count symbol"y" in the csv file
            count += 1                 # to make the counting
            symbol = "*"               # to add the * symbol beside the complete song list
        else:
            symbol = " "               # to add the blank  beside the incomplete song list
        print(" ", str(i) + ".", symbol, "", end="")  # to show the results of the list
        for j in range(len(list_of_song[i]) - 2):    # the list of the song
            if j == 1:              # analysing the j
                dash = "-"  # adding the dash symbol
            else:
                dash = ""  # adding the blank symbol
            print(dash, "{:30}".format(list_of_song[i][j]), end=" ")
        print("({:4})".format(list_of_song[i][-2]))
    print(len(list_of_song) - count, "songs learned,", count, "songs still to learn")  # to show the user the number
                                                                                       # of song that need to learn


"""
learned_song(list_of_song)
    song_number = get_integer("song number: ")
    song_list[song_number][3] = "n"
    print song_list[song_number][0]+"by"+song_list[song_number][1]+"learned"
    return song_list
"""


def learned_song(list_of_song):     # the function that mark the songs as complete
    count = 0  # to declare the variable and start form 0
    for i in range(len(list_of_song)):  # make the constant "i"
        if list_of_song[i][3] == "y":  # make the program to count symbol"y" in the csv file
            count += 1     # to make the counting
            symbol = "*"   # to add the * symbol beside the complete song list
        else:              # to add the blank  beside the incomplete song list
            symbol = " "   # to add the blank  beside the incomplete song list
        print(" ", str(i) + ".", symbol, "", end="")  # to show the results of the list
        for j in range(len(list_of_song[i]) - 2):  # the list of the song
            if j == 1:   # analysing the j
                dash = "-"  # adding the dash symbol
            else:
                dash = ""   # adding the blank symbol
            print(dash, "{:30}".format(list_of_song[i][j]), end=" ")
        print("({:4})".format(list_of_song[i][-2]))
    if count ==0:
        print("No song need to learn. Please kindly enter 2 and Q to Quit")

    print(len(list_of_song) - count, "songs learned,", count, "songs still to learn")  # to show the user the number of song that need to learn
    s_number = count_number("Enter the number of song that you want to learn\n>>> ")  # For the user to choose the number to learn with the song number
    if list_of_song[s_number][3] == "n":  # If there is "n" in forth position in csv file, it show the duplicate message
        print("You have already learned", list_of_song[s_number][0])
    else:
        list_of_song[s_number][3] = "n"  # If there is "n" but for the song that is not in th above if statement, there will be marked as learned
        print(list_of_song[s_number][0], "by", list_of_song[s_number][1], "learned")
        return list_of_song


def add_new_song():  # the function that add the new song to the songs.csv
    input_song = []
    title = word_input("Title: ")  # input the title
    artist = word_input("Artist: ")  # input the Artist
    year = str(count_number_year("Year: "))  # input the year
    input_song.append(title)  # add to the list add_new_song from the title_name
    input_song.append(artist)  # add to the list add_new_song from the artist_name
    input_song.append(year)  # add to the list add_new_song from the Year
    input_song.append("y")  # add to the list add_new_song from symbol "y"
    print(title, "by", artist, "({:4})".format(year), "added to song list")  # prompt that show user that the song has
    return input_song  # returned to input_song                                been added


def word_input(prompt):   # to collecte the user input easily and th solve the error, i created the get_string functions
    string_input = input(prompt)  # to connect between the all user input prompt and string_input
    while len(string_input) == 0:  # when the user did not write anything, it will pop up the following message
        print("Input can not be blank")  # if the imput blank, it will shown "Input can not be blank"
        string_input = input(prompt)  # to re - request the prompt
    return string_input.title()  # to return to the string-input.title


def count_number(prompt):  # the function that control the number counting in the whole program
    valid = False       # to make variable as False
    while not valid:    # to make while loop
        try:
            input_number = int(input(prompt))  # make connection between the integer input and the
            if input_number < 0:            # if the user input is less than 0, it will show the error message.
                print("Number must be >= 0")  # the error message
            elif input_number >= 7:      # if the user input more than 7, it will show the following error message
                print("Song number not in the list")  # the error message
            else:
                return input_number  # to make user to rewrite
        except ValueError:
            print("Invalid input; enter a valid number")


def count_number_year(prompt):
    valid = False       # to make variable as False
    while not valid:    # to make while loop
        try:
            input_number = int(input(prompt))  # make connection between the integer input and the
            if input_number < 0:            # if the user input is less than 0, it will show the error message.
                print("Number must be >= 0")  # the error message
            else:
                return input_number  # to make user to rewrite number
        except ValueError:  # for the value error
            print("Invalid input; enter a valid number")


def final_saving_songs(list_of_song):   # writing the list function
    final_file = open(Filename, 'w')    # if the code is "w', it will overwrite the whole program in list
    for i in range(len(list_of_song)):  # the constant and the variable
        if i != 0:
            print("\n", end="", file=final_file)  # the  message that show th final file
        for j in range(len(list_of_song[i])):   # constant j is represent that range of the list
            final_file.write(list_of_song[i][j])  # write the arranged data into the songs.csv
            if j != 3:
                print(",", end="", file=final_file)  # the message that show the confidential note
    final_file.close()  # close the songs.csv file


def main():  # the main of the function combines all other functions
    print("Songs To Learn 1.0 - by Ye Yint Thet Khine ")
    list_of_Song = loading_songs()  # to connected between list_of_song function and loading song function
    print(len(list_of_Song), "songs loaded")  # this function is to shows the number of songs contain in songs.csv
    menu_selection = main_menu()  # to connected between menu_Selection and main_Menu()
    while menu_selection != "Q":  # If user enter Q, this will go to  list_of_Song.sort function
        list_of_Song.sort(key=itemgetter(1, 0))
        if menu_selection == "C":  # If user enter C, this will go to display_song_complete_a_song(list_of_Song)function
            learned_song(list_of_Song)
        elif menu_selection == "A":  # If user enter A, this will go to display_song_list(list_of_Song) function
            list_of_Song.append(add_new_song())
        else:  # If user enter L, this will go to display_song_list(list_of_Song) function
            display_song_list(list_of_Song)
        menu_selection = main_menu()  # to connected between menu_Selection and main_Menu()
    final_saving_songs(list_of_Song)  # If user enter Q, the program will overwrite the csv file
    print(len(list_of_Song), "songs saved to", Filename, "\nHave a nice day :)")  # Save tocsv and show farewell message


if __name__ == '__main__':
    main()


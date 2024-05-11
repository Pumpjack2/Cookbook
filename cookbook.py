#importing our modules
import time
import os

# Creating a loop statement so that whenever the user finishes creating, searching,- 
# -or editing a function or puts and incorrect answer they return back to the main menu
while True:
    print("Welcome to Laurens CookBook.")
    print("[1] to create a new recipe.")
    print("[2] to search a recipe.")
    print("[3] to exit.")

    response = int(input())
    
    # Goes through code to create a recipe if the user presses 1
    if response == 1: 
        # Gets the recipe name from the user
        print("Add recipe name.")
        recipename = input()
        # Gets the ingrdents needed for the recipe from the user
        print("Please enter ingredents.")
        print("(seperated by commas)")
        ingredents = input()
        # Gets the instruction to make the recipe from the user
        print("Now write instructions.")
        print("For example: 1. Flower, 2. 3 Eggs, 3. ect...")
        instructions = input()
        # Gets the serving size of the recipe from the user
        print("Enter the amount of people this dish will feed.")
        servingsize = input()
        # Checks to see if the serving size is numerical
        if servingsize.isdigit():
            # If the severing size is numerical then the program continues
            
            # Prints out a preview of the contents of the file to the user
            recipe = list()
            list = ["RECIPE NAME:" ,recipename ,"INGREDENTS:" ,ingredents ,"INSTRUCTIONS:" ,instructions ,"SERVING SIZE:" ,servingsize,]
            print("----Content of File----")
            print(list)
            # Asks the user if the information is correct or not
            print("If this information is correct then press 1.")
            print("If this information is wrong then press 2.")
            choice = int(input())
            
            #Gets the user to name the file of the recipe
            if choice == 1:
                print("Enter the name of the new recipe: ", end="")
                filename = input()
            
            # Then makes a file named by the user
            try:
                fp = open(filename, "x")
                # Tells the user that the file was create successfully
                print("\nThe file, \"" + filename + "\" created successfully.")
                # Writes the information of the recipe into the file
                fp = open(filename, "w+")
                fp.write(recipename)
                fp.write("\n")
                fp.write(ingredents)
                fp.write("\n")
                fp.write(instructions)
                fp.write("\n")
                fp.write(servingsize)
                fp.write("\n")
                # Prints out the final version of the file
                print("\n----Content of File----")
                fp.seek(0)
                print(fp.read())
                fp.close()
                quit

            # If the file already exist then an error message will occur  
            except FileExistsError:
                print("\nThe file, \"" + filename + "\" already exists.")
                time.sleep(3)
                quit
            
            #If user beleive the information he or she entered is wrong then the program restarts
            if choice == 2:
                print("Ok.")
                time.sleep(3)
                quit

        # If the serving size is not numerical then an error message occurs    
        else:
            print("INVALID OPTION!")
            print("Please try again.")

    # If the user presses 2 then the search program runs    
    elif response == 2:
        # Asks the user the name of the file they want to see
        print("Please type the recipe you would like to see.")
        # Gets the file name
        filename = input()
        # Opens the file
        fp = open(filename, "r")
        #Say that the file is available
        print("The file is available.")
        # Asks the user if they want to see the information in the file or not
        print("If you would like to see the recipe press 1.")
        print("If you don't want to see the recipe press 2.")
        decision = int(input())

        # If they do then the program prints out the information in the file
        if decision == 1:
            print("\n----Content of File----")
            fp.seek(0)
            print(fp.read())
            fp.close()

        # If they don't want to see the file then the program brings user to the menu
        elif decision == 2:
            print("Ok.")
            time.sleep(3)

        # If user enters and invalid option then a error message is printed out
        else:
            print("INVAILD OPTION!")
            print("Please try again.")


    # If the user presses 3 then the program ends
    elif response == 3:
        print("Goodbye.")
        time.sleep(3)
        break


    # If the user enters and invalid option then an error message is displayed
    else:
        print("INVALID OPTION!")
        print("Please try again.")
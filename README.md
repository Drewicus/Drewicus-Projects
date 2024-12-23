# Food Suggester ( for indecisive people)
  #### Video Demo:  <[Final Project](https://youtu.be/DX8wC_hb8q8)>

  ### Description:
  This program will use Machine learning via scikit-learn to suggest a food the user may want to try via their own answers to the questions provided. It has a Class, with all questions encapsulated in. The program uses an API from spooncular to access some online suggestions, an option for the user to add data to the data-sets, and a random choice option. It has four extra files/libraries created to function with it, time_machine.py, machine_learning.py, dataset_files.py, and dataset.json. I created all of these and they are essential to the file running. It also has a list of pip installable which are also needed, these can be found in requirements.txt.

  How does it work?

  The main use case: option 1: ( get a suggestion)
   - If 'get a suggestion' is selected in the menu, it will prompt the user 5 questions, all of which will be collected by the class UserInfo and be fed into the sci-kit and using the datasets it has, it will predict a food that best fits the user input, however if it is unable to match something correctly, it will return a random one as to still give a suggestion to the user.

  Option 2: Add new data to improve recommendations
   - This will go through the orginal 5 questions, plus an extra for the food which the user wishes to input. It will then if passing validation, add it to the data sets

  Option 3: Get some food suggestions from the internet
   - This will use spooncular's API to get 5 food suggestions in relation to the user's cuisine input. If validated, and also not in the dataset already it will print the 5 suggestions, and add them to the datasets. If in the dataset already, it will simply print the suggestions to the user.


  Option 4: Get something totally random
   - Returns a food suggestion using random.choice with the food name dataset.

  Option 5: Exit
  - Exits the application

  ## Self-intro/story: (can skip)
  <details>
    <summary>Click to expand</summary>
This project was inspired by my constant battle with my wife to decide what to eat for dinner. We're both indecisive.
The hope was that this would hopefully address and help fix any issues we ran into on the daily breakfast/lunch or dinner time ( even snacks).
Orginally I simply started with a bunch simple user input questions, I was going to make a list and use A LOT of conditionals to try find something to suggest from a very large data set I was going to create.
I started with the input as mentioned, thinking about the main compenents required to make a good suggestions for what to eat.
First; What time, Second; cuisine, Third; healthy or guilty, fourth; eat in or eat out (Which i still feel doesnt have much weight to it).

After that, I spent a long time trying to validate each, and decided to make a class based off a real-life information sheet of sorts where all the collected information would be.
That proved difficult as I seemingly didnt have a good grasp on classes. But after much review of the lectures and reading up on classes I got it to a functional state.
The main difficulty was trying to understand how all the functions/input questions could line up and function correctly.

I decided to start trying for conditonals which proved far to difficult and lengthy for my current skill level, so I googled some basic prediction libraries and found scikit-learn, which is a very basic machine learning library. I almost gave up on implementing it multiple times, even considered starting a whole new project that was more in-line with what I could do or even understand. I read up on it and tried implementing it in different files and on old projects from my previous courses, eventually i got it to be at least functional and added it to my final project. The information returned however wasnt exactly correct. For example, after user input wanting some breakfast italian food that was guilty, it returned a japanese soup. I tried to add more to the data sets to try give more for the library to use but then realised they had to be the same length for both my example user input dataset, and example answer data set. I also realised that I didnt understand what the "machine" learning part was doing, so I studied on what each function did, such as encoders, as the transformers as well as the inverse transform, I ,at least, understand it conceptually now. This was the most difficult and time consuming part of my project.

Post implementation of the machine learning I still felt that the project wasnt enough and realised that i only had 1 function outside of main(), as per the guidelines I needed 3, so i dedcided to add options to the "start menu", first was the user adding a food example, which was a pain to implement and get their data added to the data-sets. I couldnt quite think of anything adiquite to add to the menu, so I googled about some API's i could add into it and found spooncular has a free version of their API that allows 150 uses per day( Enough for final project). After reviewing the lecture on API and their implementation it wasn't that hard to implement, specially after the ML. I also made sure it would add the suggestions to the example answers data-set, however this raised another problem, it unbalanced the two data-sets lengh, so i added a random.choice function for the usual user_input questions and filled the cuisine part with what the user had chosen. This fixed the balance.

For the last function to add outside of the class, i chose an "easy" one, which was simply a random suggestion without any of the questions, simply, just choosing 1 suggestion from the example answers data set.

After these i tested via the test file, and once figuring that out, which was much harder testing a project with multiple libraries, data-sets and seperate files, than the simple ones we did in lecture, I used figlet to edit the Options print, and after some time found colorama to color and differeniate each option and sentence in the project.
  </details>

# **Files and their functions**:
  ## **Project.py**
  - Contains the Class(UserInfo), Start menu, and 3 extra functions, get food suggestion, Add new example(via user input), new suggetions(via the Spooncular API), and random_food( give random suggestion without input)

    ### **Class: UserInfo**

    - Class functions

        - init(self)
        - collect_time_of_day
        - collect_cuisine_preference
        - _more_suggestions
        - collect_health_type
        - collect_food_group
        - collect_eating_preference
        - (property) info, set_info
        - collect_all_info, get_food_suggestion
    - List and Dictionary
      -  list of the top 50 (from google), cuisine names.
      - dictionary of the different food groups as keys, and values of specifics like chicken, beef etc.

    - **_init__(self)**

          - sets self.info as a list

    - **collect_time_of_day(self)**

          - Prints a greeting message to user.
          - While loop for input "what time is it?"
            - calls on time_of_day function from time_machine.py
            - uses time_of_day, and what_meal to recieve either Breakfast, lunch, dinner, or snack time, and appends it to the self.info list

    - **collect_cuisine_preference(self)**

          - While True loop
              - gets input from what user feels like, with a for loop using enumerate on cuisine list to show examples.
              - gives option to enter 'r' for random, or 'm' for more options
              - conditonals for if user entere cuisine name, r, or m.
                  - if 'm' it will call a private helper function _more_suggestions()
                  - then condtional to check if returned value is truthy, then append to info.list
    - **_more_suggestions(self, start = 10, step = 10)**

          - assign variable a **.lower()** verison of cuisne names in food list via list comprehension.
          - while loop for when start is less than the length of the entire cuisine list
              - enumerate for loop to list 10 examples
              - user input question to ask for want, or m for more.
              - conditional if they entered a cuisine
                - if true add cusine to self.info list
              - else: return 10 more options via  start+= step

    - **collect_health_type(self)**

          - While True loop
              - ask for healthy or guilty
              - small validation if true, append
              - else: ask again.

    - **collect_food_group(self, start=5, step=5)**

          - While true loop:
              - input question to see what the user is feeling like, rice, bread, meat, fish etc.
              - set a variable to FALSE to help end loop when answered correctly.
              - For loop for group and items in food_group dict.
                  - check if user input is in main options, meats, fish, vegetables, if so,  will enumerate for loop to list options in those catergories out.
                    - gets user input again from the options
                      - if entered correctly will set found to TRUE
              - contional if found is equal to TRUE then will append to the user.info list
                - else ask again

    - **collect_eating_preference(self)**

          - While true loop
              - user input question to choose if they eat in or eat out.
              - validator to check if entered correctly, then append to self.info list
              - else ask again

    - **getter and setter**

          - last ditch effort to check if the self.info isnt an empty string

    - **collect_all_info(self)**

          - calls all the class methods and gathers together

    - **get_food_suggestion(self, model, f_encoder, t_encoder)**

          - assign variable a list of columns in self._info using slicing/index ( all user input )
          - use the encoder method imported from sci-kit with .trasnform string into numerical values and enmeruate for loop
          - assign variable the .prediction fucntion with encoded input
          - assign new variable the inverse.transform ( from numbers to str (english))
          - print that new variable containing the predicted food.
          - give option to quit out or start the program again. with 0 or enter
            - if reset will return to start menu
              - else: sys.exit()
          - Incase the ML program couldn't predict a food based on input ( not big enough data set?), it will print a random selection from the choices that were transformed back into english
          - then give option to reset or quit.




    # **Non-class Functions**

      ## functions:
        - add_new_example
        - new_food_suggestion
        - get_random_food
        - main

      #### main()
          - create and globalize ex, ex_answer functions ( for the datasets)
          - Trains the Machine learning file with ex_ex_answer, spliting it into model, f_encoder, t_encoder.\
          - While loop, containing the options for which the user can choose;
              1. Get food suggestion ( main function)
              2. Add user data into ML model
              3. Use API to get suggestions and then also add into ML model.
              4. A totally random food suggestion from ex_answer
              5. exit

          - conditionals for each choice,
            1 will call the class and start the orginal process of the project, then use the ML model to predict an answe rbased on the choices.
            2 will call add_new_example function to start that functions process.
            3 will get user input for cuisine and use the api to recieve 5 suggestions then add to ML model.
            4 calls get_random_food function to get a random choice.
            5 to exit

      #### add_new_example()
          - ask the same 5 questions as per the UserInfo input, plus  a 6th asking what the food theyre adding is named.
          - create a list containing 5 of the answers
          - conditional if statement to check if list isnt already in dataset 1(user answers) and 6th isnt in dataset 2 ( food names)
          - append new entry to dataset 1 and food name to data set 2
          - save dataset


      #### new_food_suggestion(cuisine)
          - Takes the users input cuisine choice as arguement
          - Loads the dataset ( I couldnt test it properly if it didnt load it seperately)
          - Loads the API key from spooncular
          - uses a formated string to assign the URL to a variable, the url contains the input cuisine and api_key variables as per states from their website documentation
          - sets a variable using .get(url) from requests library
          - then change it to a .json()
          - list comprehension assigned to variable which finds the title of the food in the json under "results" in the dict
          - set a checker variable assigned 0 used to know if the suggestions were already in the data set or not.
          - For loop to enumerate the titles gained from the json. ( to show the user what was suggested)
          - For look to check if suggestion is already in the dataset 2 ( ex_answer), if in it, continue without appending.
              - if not, use 4 random choice answers for the usual user input to balance both datasets
                  eg; Breakfast time!, Healthy, rice, eat out
              - append these, plus the API's suggested food, and add 1 to the counter variable.
          - if the counter is above 0 it will use save_dataset
          - else return an empty list with a print informing users of what happened.

      #### get_random_food
            - opens the dataset.json file and loads it into a variable.
            - assigns ex_answer the dataset 2 food names
            - conditional to check if its not an empty string.
            - if truthy, will assign a variable a random choice using random.choice from the dataset 2 and returns the formated string.





# **time_machine.py**
  - This file is a combined verison of two problem set assignements(working, meal), using regex, and two help functions, it will return either, breakfast, lunch, dinner, or snack time.
      - This helper-file can take 24hr time, 12 hour time, and it also is very user friendly not requiring minutes, or spaces between HH:MM am/pm.
  - This was actually the first thing i did as it was the first question i needed in my final project file. and took a lot of trying to get the regex to catch what i wanted it to, then later going back and adding in 24hr time and user friendly parts like minutes and spaces etc.
            ~ I was forced to learn about re.sub which was confusing at first.

      ## Functions:
      - time_checker
      - am_or_pm
      - meal_time

      #### time_checker(time)
          - 2 regex using re.sub to find if there is a space between the HH:MM and am/pm both for 9 am 9pm/ 9:00am / 9:00 pm, with or without minutes.
          - uses the warlus operator :=  and re.fullmatch on my regex for 12 hour and 24 hour time.
            - if truth, split the hours,mins, and am/pm of 12 hour using match.group(1-3), and 24hr time into group(5-6 if existing)
                - conditonal to check if 12 hour exists,
                - if no 12 hour return formated string which calls on helper function am_or_pm to return float of 24 hour input
                  - else: return formated string calling am_or_pm to change 12hr to 24hour

      #### am_or_pm(hour, am_pm)
          - conditonal to check if ":" is in the hour
            - if true, split into hours minutes variabbles
            - else; the same, but set minutes to "00" for conversion
          - try to set hours and minutes to int()
              - or raise value error
          - condtional to check if there is or is not am or pm in arguement.
              - if no am_pm then validator to check if hours are between 0 and 23,
                - and another to check if minutes between 00 and 59
                - returns the vaildated hours and minute sin formated string
          - if am_pm entered in arguement, will do same validation
            - then validate if am_pm is "pm", and hours doesnt equal 12, +12 to hours
              - or if am_pm is "am" and hours == 12, assigned 0 to hours
              - return  hours and minutes

      #### meal_time(time)
          - set a variable with the converted float value of the time string returned, eg; 9:30 am would be 9.5
          - then use a condtional statement to check it on some defined times like 7-10 is breakfast time, 12-13 is lunch, 18-20 is dinner, else is snacktime
          - return the one which is true.

      #### main()
          - user input question for time
          - call the functions then print what time it is, Breakfast, lunch,dinner or snacktime.


# **machine_learning.py**
  - This file contains the model for the basic prediction model using scikit-learn
      - contains: Two encoders, f_enconder, and t_encoder, and a model
      - This file returns Model, f_encoder, t_encoder

      ## Functions:
      - Main
      - train_ml_model

      ### main()
          - calls the singular function

      ### train_ml_model(ex, ex_answer)
            - f_encoder
              -- assigns a variable with a list comprehension using LaberEncoder from scikit-learn, with a range(5) of 5.
              - f_encoder creates a laberencoder for each column(5) and handles its values independantly. Then using .fit_transform(col) in a for loop with enumerate,
                    on a zip()'d verison of the input dataset, it will transform it into numerical values.
              -- assigns a variable with a list comprehension encoded verison of the data set 1, using a for loop including;
                  1. list() - sets it to a list
                  2. .fit - fit learns all the unique values in the columns
                  3._transform(col) - will convert values to numerical values
                  4. enumerate -  iterates with index and each value
                  5. zip() -  makes a list of rows into a lsit of columns
                  6. *ex - unpacks the list of dataset 1
            - t_encoder
              -- assigns t_encoder with a LaberEncoder()
              - t_encoder Does the same as above but to the answer set which is much simplier lsit of food examples.
              -- assigns an encoded variable with .fit_transform(ex_answer)  dataset2

            - model variable is assigned DecisionTreeClassifier() function from scikit library
              -- This is the prediction unit that takes numerical values from data sets and predicts the answer using the user_input. based from all the examples in the data set1
              -- .fit then learns the unique values of both encoded datasets 1-2

            returns f_encoder, t_encoder, model



# **dataset_files.py**
  - A simple file containing two functions;
  - Functions:
    - save_dataset , load_dataset
        - These functions open a seperate .json file containing the two data sets and either loads the files or save them.
        - contains an older default value that can be used if it is unable to load the correct file.


# **dataset.json**
   - Contains a dictionary containing, ex, and ex_example, the two datasets.


# TODO:
  - Ideally i'd like to add in another part of the API to get recipes ,if wanted, when eat-in was selected. using the grocery-list problem set

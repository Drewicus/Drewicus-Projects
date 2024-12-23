import random
import requests
import json
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from machine_learning import train_ml_model
from dataset_files import save_dataset, load_dataset
from time_machine import time_checker, meal_time # My self made time checker for time period
import pyfiglet
from colorama import Fore, Style

class UserInfo:
    #Class for user_information to feed into the scikit-learn
    # list of top cuisines
    popular_cuisines = [
    "Italian", "Chinese", "Indian", "Mexican", "Korean",
    "French", "Japanese", "American", "Greek", "Middle Eastern",
    "Spanish", "Thai", "Vietnamese", "Turkish", "Caribbean",
    "Mediterranean", "African", "Brazilian", "German", "Russian",
    "Filipino", "Malaysian", "Indonesian", "Ethiopian", "Persian",
    "British", "Portuguese", "Cuban", "Argentinian", "Cajun",
    "Moroccan", "Swedish", "Polish", "Lebanese", "Australian",
    "Hawaiian", "Pakistani", "Burmese", "Nepalese", "Tibetan",
    "Peruvian", "Chilean", "Bangladeshi", "Israeli", "Afghan",
    "Uzbek", "Mongolian", "South African", "Belgian", "Swiss",
    ]
    # list of food groups
    food_groups = {
        "grains": ["pasta", "rice", "bread", "oats", "quinoa", "barley", "noodles", "wheat", "corn", "rye", "millet", "sorghum", "buckwheat", "farro", "pancakes"],

        "vegetables": ["broccoli", "carrot", "spinach", "peas", "chickpeas", "lentils", "beans", "tomatoes", "potatoes", "onions", "peppers", "garlic", "lettuce", "cucumber", "zucchini", "kale", "cauliflower", "mushrooms", "celery", "vegetables"],

        "fruits": ["apple", "banana", "orange", "berries", "melon", "grape", "pineapple", "strawberries", "blueberries", "mangoes", "cherries", "peaches", "watermelon", "papaya", "kiwi", "lemon", "avocado"],

        "fish": ["fish", "salmon", "tuna", "mackerel", "sardines", "cod", "haddock", "trout", "herring", "anchovies", "snapper", "shellfish", "fish"],

        "meats": ["chicken", "beef", "pork", "lamb", "turkey", "duck", "goat", "veal", "venison", "rabbit", "bison", "ham", "bacon", "sausage", "organ meats (liver, heart)", "meats"],

        "dairy": ["milk", "yogurt", "cheese", "soy milk", "almond milk", "butter", "cream", "cottage cheese", "cream cheese", "sour cream", "buttermilk", "ricotta", "mozzarella", "parmesan", "feta"],

        "alternatives": ["tofu", "eggs", "nuts", "seeds", "tempeh", "edamame", "seitan"]
        }

    #create the infomation list
    def __init__(self):
        self._info =[]
    #Gather the eating period
    def collect_time_of_day(self):
        print(f"\n{Fore.BLUE}You {Fore.RED}must{Fore.BLUE} be {Fore.RED}hungry {Fore.BLUE}don't worry I've got you covered!\nPlease {Fore.GREEN}Answer{Style.RESET_ALL} {Fore.BLUE}the {Fore.GREEN}questions{Fore.BLUE} so we can get you fed, quick!\n{Style.RESET_ALL}")
        while True:
            u_time = input(f"What {Fore.YELLOW}time{Style.RESET_ALL} is it?: ")
            try:
                time_of_day = time_checker(u_time)
                what_meal = meal_time(time_of_day)
                print(f"{Fore.BLUE}It's {Fore.YELLOW}{what_meal}{Style.RESET_ALL}\n")
                self.set_info(what_meal)
                break
            except ValueError:
                print(f"{Fore.RED}Please Try again in HH:MM format!{Style.RESET_ALL}")

    # Gather what cuisine the user feels like.
    def collect_cuisine_preference(self):
        while True:
            print(f"Please {Fore.YELLOW}enter the name{Style.RESET_ALL} of the cuisine you feel like most:")
            for i, food in enumerate(self.popular_cuisines[:10], start=1):
                print(f"{Fore.CYAN}{i}. {Fore.BLUE}{food}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Type {Fore.RED}'m'{Style.RESET_ALL} {Fore.BLUE}for more suggestions\n{Fore.CYAN}Type {Fore.RED}'r'{Style.RESET_ALL} {Fore.BLUE}for a random choice{Style.RESET_ALL}")

            food_type = input("\nSelection: ").strip()
            # for more options
            if food_type.lower() == 'm':
                more_food = self._more_suggestions()
                if more_food:
                    self.set_info(more_food)
                    break
            # random choice
            elif food_type.lower() == "r":
                random_choice = random.choice(self.popular_cuisines[:20])
                print(f"\n{Fore.BLUE}You chose a random choice, Here it is!: {Fore.YELLOW}{random_choice}{Style.RESET_ALL}")
                self.set_info(random_choice)
                break


            elif food_type.lower() in map(str.lower, self.popular_cuisines):
                self.set_info(food_type.capitalize())
                break
            else:
                print(f"{Fore.RED}Please answer the questsions again, something was invalid!{Style.RESET_ALL}")

    # if the first 10 werent enough, up to 50 will be shown
    def _more_suggestions(self, start=10, step=10):
        pop_cuisines_lower = [cuisine.lower() for cuisine in self.popular_cuisines]
        while start < len(self.popular_cuisines):
            print(f"\n{Fore.BLUE}Here are some more options: {Style.RESET_ALL}")
            for n, food in enumerate(self.popular_cuisines[start:start+step], start=start+1):
                print(f"{Fore.CYAN}{n}. {Fore.BLUE}{food}{Style.RESET_ALL}")

            more_options = input(f"{Fore.BLUE}Please enter what you feel like, or type {Fore.RED}'m'{Fore.BLUE} for even more options:\n {Style.RESET_ALL}").strip()

            if more_options.lower() in pop_cuisines_lower:
                return more_options.capitalize()

            elif more_options.lower() == "m":
                start += step
                if start >= len(self.popular_cuisines):
                    print("No more cusisines to show!")
                    return None
            else:
                print(f"{Fore.RED}Invalid entry, Please try again or type 'm' for more options.{Style.RESET_ALL}")
    # Gather healthy or unheathy info
    def collect_health_type(self):
        while True:
            print(f"\n{Fore.BLUE}Do you feel like a {Fore.RED}guilty{Fore.BLUE} pleasure or a {Fore.GREEN}healthy{Fore.BLUE} meal?:\n {Style.RESET_ALL}")
            health_type = input("Selection: ").lower()
            if health_type in ("healthy", "guilty"):
                self.set_info(health_type)
                break
            print(f"{Fore.RED}Please choose either 'healthy', or 'guilty'{Style.RESET_ALL}")
    # Gather food group info
    def collect_food_group(self, start=5, step=5):
        while True:
            print(f"\n{Fore.BLUE}What are you feeling today, {Fore.YELLOW}rice?, pasta?, bread?, noodles?, meat?, fish? {Fore.BLUE}etc..\n {Style.RESET_ALL}")
            desire = input("Selection: ").strip().lower()
            found = False
            for group, items in self.food_groups.items():
                if desire in ["meat", "meats"]:
                    print(f"{Fore.BLUE}Which would you prefer: {Style.RESET_ALL}")
                    for n, food in enumerate(self.food_groups["meats"], start=1):
                        print(f"{Fore.CYAN}{n}. {Fore.BLUE}{food}{Style.RESET_ALL}")

                    specific = input(f"\n{Fore.BLUE}What meat are you feeling like?{Style.RESET_ALL}\nSelection: ").lower().strip()
                    if specific in self.food_groups["meats"]:
                        self.set_info(specific)
                        found = True
                        break

                elif desire in ["fish", "seafood"]:
                    print(f"{Fore.BLUE}Which would you prefer: {Style.RESET_ALL}")
                    for n, food in enumerate(self.food_groups["fish"], start=1):
                        print(f"{Fore.CYAN}{n}. {Fore.BLUE}{food}{Style.RESET_ALL}")

                    seafood = input(f"\n{Fore.BLUE}What seafood are you feeling like?{Style.RESET_ALL}\nSelection: ").lower().strip()
                    if seafood in self.food_groups["fish"]:
                        self.set_info(seafood)
                        found = True
                        break

                elif desire in ["veges", "vegetables"]:
                    print(f"{Fore.BLUE}Which would you prefer: {Style.RESET_ALL}")
                    for n, food in enumerate(self.food_groups["vegetables"], start=1):
                        print(f"{Fore.CYAN}{n}. {Fore.BLUE}{food}{Style.RESET_ALL}")

                    vegetables = input(f"\n{Fore.BLUE}What vegetable are you feeling like?{Style.RESET_ALL}\nSelection: ").lower().strip()
                    if vegetables in self.food_groups["vegetables"]:
                        self.set_info(vegetables)
                        found = True
                        break


                elif desire in items:
                    print(f"{Fore.YELLOW}{desire.capitalize()}!{Fore.BLUE} Delish!")
                    self.set_info(desire)
                    found = True
                    break
            if found:
                break
            print(f"{Fore.RED}Unfortunately I couldn't find that one! Please try another!{Style.RESET_ALL}")

    #Eat in or out info
    def collect_eating_preference(self):
        while True:
            print(f"\n{Fore.BLUE}Will you {Fore.YELLOW}eat-in {Fore.BLUE}or{Fore.YELLOW} eat-out: {Style.RESET_ALL}")
            preference = input("Selection: ").strip().lower()
            if preference in ["eat-in", "eat-out", "eat in", "eat out"]:
                self.set_info(preference)
                break
            print(f"{Fore.RED}Please Choose either 'eat-in' or 'eat-out'{Style.RESET_ALL}")
    #validation JUST before appending, post functions self validation as last ditch effort
    @property
    def info(self):
        return self._info

    def set_info(self, value):
        if not value == "":
            self._info.append(value)
        else:
            print(f"{Fore.RED}{value} is invalid{Style.RESET_ALL}")
    #gather info all together
    def collect_all_info(self):
        self.collect_time_of_day()
        self.collect_cuisine_preference()
        self.collect_health_type()
        self.collect_food_group()
        self.collect_eating_preference()
    #feed it into the scikit model
    def get_food_suggestion(self, model, f_encoder, t_encoder):
        try:
            #each number is 1 column 0-4 in the list
            new_input = [self._info[0], self._info[1], self._info[2], self._info[3], self._info[4]]
            #list comprehendsion for encoding and transforming columns into numbers
            new_input_encoded = [f_encoder[i].transform([val])[0] for i, val in enumerate(new_input)]
            #using the numbers will predict what the food suggestion should be
            prediction = model.predict([new_input_encoded])
            #changes the numbers back into human readable language ( english)
            predicted_food = t_encoder.inverse_transform(prediction)

            print(f"\n{Fore.BLUE}Based on your choices, I recommend: {Fore.YELLOW}{predicted_food[0]}{Style.RESET_ALL} 🍽️")
            reset = input(f"{Fore.BLUE}If you'd like to run the program again type {Fore.RED}'0'{Fore.BLUE}, or push {Fore.RED}enter{Fore.BLUE} to exit the application:{Style.RESET_ALL}\n ")
            if reset:
                return
            else:
                sys.exit()
        except ValueError:
            random_food = random.choice(t_encoder.classes_)
            # just icnase it could not find a match it will print something random from the food list
            print(f"\n{Fore.BLUE}I couldn't match your choices perfectly, but how about trying something random:{Fore.YELLOW} {random_food}{Style.RESET_ALL} 🍽️?")
            reset = input(f"{Fore.BLUE}If you'd like to run the program again type {Fore.RED}'0'{Fore.BLUE}, or push {Fore.RED}enter{Fore.BLUE} to exit the application:{Style.RESET_ALL}\n ")
            if reset:
                return
            else:
                sys.exit()

# Option to add a new example to the data set for the scikit model
def add_new_example():
    print(f"\n{Fore.BLUE}Add a new food suggestion to improve the model!")
    time_of_day = input(f"Enter time of day (ex: {Fore.YELLOW}Breakfast time!, Lunch time!, Dinner time!{Style.RESET_ALL}):\nSelection:  ").strip()
    cuisine = input(f"{Fore.BLUE}Enter cuisine (ex:{Fore.YELLOW} Italian, Chinese, American..):{Style.RESET_ALL}\nSelection: ").strip()
    health = input(f"{Fore.BLUE}Is it {Fore.GREEN}healthy {Fore.BLUE}or {Fore.RED}guilty?:{Style.RESET_ALL}\nSelection: ").strip()
    food_group = input(f"{Fore.BLUE}Enter food group (ex: {Fore.YELLOW}rice, bread, meats):{Style.RESET_ALL}\nSelection: ").strip()
    eat_preference = input(f"{Fore.BLUE}will you {Fore.YELLOW}eat-in {Fore.BLUE}or {Fore.YELLOW}eat-out?:{Style.RESET_ALL}\nSelection: ").strip()
    suggested_food = input(f"{Fore.BLUE}What is the name of this dish?:{Style.RESET_ALL}\nSelection: ").strip()
    # checking if the entry already exists in the dataset
    new_entry = [time_of_day, cuisine, health, food_group, eat_preference]
    if new_entry in ex and suggested_food in ex_answer:
        print(f"\n{Fore.RED}This already exists in the dataset!{Style.RESET_ALL}")
        return
    # append the new entry if not duplicate to the datasets
    ex.append(new_entry)
    ex_answer.append(suggested_food)
    #save to dataset
    save_dataset(ex, ex_answer)
    print(f"{Fore.MAGENTA}New example has been added!{Style.RESET_ALL}")

#Use API to get 5 suggestions for the entered cuisine, and add to the dataset.
def new_food_suggestion(cuisine):
    ex, ex_answer = load_dataset()
    try:
        api_key = "31fdb4a32e3644cb95fc500359903904"
        url = f"https://api.spoonacular.com/recipes/complexSearch?cuisine={cuisine}&number=5&apiKey={api_key}"
        response = requests.get(url)
        #print(json.dumps(response.json(), indent=2))
        data = response.json()
        suggestions = [recipe["title"] for recipe in data["results"]]
        added_count = 0
        print("Suggestions:\n")

        for n, food in enumerate(suggestions, start=1 ):
            print(f"{Fore.CYAN}{n}. {Fore.BLUE}{food}{Style.RESET_ALL}")

        for n, suggestion in enumerate(suggestions, start=1):
            if suggestion in ex_answer:
                continue
            #set random answers for the input to keep datasets even in number
            random_time = random.choice(["Breakfast time!", "Lunch time!", "Dinner time!", "Snack time!"])
            random_health = random.choice(["healthy", "guilty"])
            random_fgroup = random.choice(list(UserInfo.food_groups.keys()))
            random_pref = random.choice(["eat-in", "eat-out", "eat in", "eat out"])

            ex.append([random_time , cuisine, random_health, random_fgroup, random_pref])
            ex_answer.append(suggestion)
            added_count += 1

        if added_count > 0:
            save_dataset(ex, ex_answer)
            print(f"{Fore.BLUE}Added {Fore.YELLOW}{added_count}{Fore.BLUE} new suggestions!{Style.RESET_ALL}")
            reset = input(f"{Fore.BLUE}If you'd like to run the program again type {Fore.RED}'0'{Fore.BLUE}, or push {Fore.RED}enter{Fore.BLUE} to exit the application:{Style.RESET_ALL}\n ")
            if reset:
                return
            else:
                sys.exit()
        else:
            print(f"\n{Fore.BLUE}The suggestions gathered from online already exist inside the data-set! yippie!{Style.RESET_ALL}")
            reset = input(f"{Fore.BLUE}If you'd like to run the program again type {Fore.RED}'0'{Fore.BLUE}, or push {Fore.RED}enter{Fore.BLUE} to exit the application:{Style.RESET_ALL}\n ")
            if reset:
                return []
            else:
                sys.exit()

    except ValueError:
        return(f"{Fore.RED}Please enter a Cusinie name like, American, or Japanese{Style.RESET_ALL}")
        return []

# if someone wants a quick random food suggestion
def get_random_food():
    try:
        with open("dataset.json") as file:
            data = json.load(file)
        ex_answers = data.get("ex_answer", [])
        if ex_answers:
            random_food = random.choice(ex_answers)
            return f"{Fore.YELLOW}{random_food}{Fore.BLUE} is the food that was randomly selected!{Style.RESET_ALL}"
    except FileNotFoundError:
        return(f"{Fore.RED}Food file not found{Style.RESET_ALL}")

def main():
    #load dataset to global
    global ex, ex_answer
    ex, ex_answer = load_dataset()
    #train model
    model, f_encoder, t_encoder = train_ml_model(ex, ex_answer)
    #Give options to user
    while True:
        options = pyfiglet.figlet_format("\nOptions:")
        print(f"{Fore.CYAN}{options}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}1. Get a food suggestion🍔🍟\n")
        print(f"{Fore.GREEN}2. Add new data to improve recommendations🗃️\n")
        print(f"{Fore.YELLOW}3. Get some food suggestions from the internet!🛜\n")
        print(f"{Fore.MAGENTA}4. Get something totally random🤷{Style.RESET_ALL}\n")
        print(f"{Fore.RED}5. Exit👋{Style.RESET_ALL}")
        choice = input(f"Enter your choice: ").strip()


        if choice == "1":
            # collect user info and predict
            user_info = UserInfo()
            user_info.collect_all_info()
            user_info.get_food_suggestion(model, f_encoder, t_encoder)
        elif choice == "2":
            # Add new data and retrain model
            add_new_example()
            # retrain
            model, f_encoder, t_encoder = train_ml_model(ex, ex_answer)
        elif choice == "3":
            #Use API to get suggestions and add to the dataset
            cuisine = input("Enter a cuisine to get some suggestions(ex: Mexican, Korean etc): ").strip()
            new_food_suggestion(cuisine)
            ex, ex_answer = load_dataset()
            model, f_encoder, t_encoder = train_ml_model(ex, ex_answer)
        elif choice == "4":
            #random suggestion from food list dataset
            random_food = get_random_food()
            print(random_food)
            break
        elif choice == "5":
            #end
            print("See you next time!\n🍽️🍽️🍽️🍽️🍽️")
            break
        else:
            print("Invalid Choice, please try again!")


if __name__ == "__main__":
    main()

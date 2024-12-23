import re

def time_checker(time):

    time = re.sub(r"(\d)(AM|PM|am|pm)$", r"\1 \2", time.strip(), flags=re.IGNORECASE)
    time = re.sub(r"(\d{1,2}:\d{2})(AM|PM|am|pm)", r"\1 \2", time.strip(), flags=re.IGNORECASE)

    if match := re.fullmatch(r'^(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)|(([01]?[0-9]|2[0-3]):([0-5][0-9])?)$',time, re.IGNORECASE):
        hours = match.group(1)
        minutes = match.group(2) or "00"
        am_pm = match.group(3)
        tfh_hours = match.group(5)
        tfh_minutes = match.group(6) or "00"
        if hours is None:
            return am_or_pm(f"{tfh_hours}:{tfh_minutes}", None)
        else:
            return am_or_pm(f"{hours}:{minutes}", am_pm)
    else:
        raise ValueError("Please enter in 'HH:MM am/pm' or HH:MM (24hour) format")



def am_or_pm(hour, am_pm):
    if ":" in hour:
        hours, minutes = hour.split(":")
    else:
        hours, minutes = hour, "00"
    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        raise ValueError("Invalid hour or minute format")

    if am_pm is None:
        if not (0 <= hours <= 23):
            raise ValueError(f"Incorrect hours{hours} for 24hr format")
        if not (0 <= minutes <= 59):
            raise ValueError(f"invalid minutes: {minutes}")
        return f"{hours:02}:{minutes:02}"

    if not (1 <= hours <= 12):
        raise ValueError(f"Invalid hour: {hours}")
    if not (0 <= minutes <= 59):
        raise ValueError(f"Invalid hour: {minutes}")


    if am_pm in ["PM", "pm"] and hours != 12:
        hours += 12
    elif am_pm in ["AM", "am"] and hours == 12:
        hours = 0

    return f"{hours:02}:{minutes:02}"

def meal_time(time):
    c_time =float(time.split(":")[0]) + float(time.split(":")[1]) / 60
    if c_time >= 7.0 and c_time <= 10.0:
        return("Breakfast time!")
    elif c_time >= 12.0 and c_time <= 13.0:
        return("Lunch time!")
    elif c_time >= 18.0 and c_time <= 20.0:
        return("Dinner time!")
    else:
        return("Snack Time!")

def main():
    user_time = input("What time is it? ")
    try:
        the_time = time_checker(user_time)
        what_meal = meal_time(the_time)
        print(what_meal)
    except ValueError:
        print("Please enter a valid format")

if __name__ == "__main__":
    main()


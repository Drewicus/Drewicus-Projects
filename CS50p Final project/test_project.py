from project import get_random_food, new_food_suggestion, add_new_example
import pytest


def test_get_random_food():
    test_ex = [["Breakfast time!", "Japanese", "healthy", "rice", "eat-in"]]
    test_ex_answer = ["Salmon Onigiri", "Risotto", "Kimchi Fried Rice"]
    result = get_random_food()
    assert get_random_food() != ""
    assert "is the food that was randomly selected!" in result


def test_new_food_suggestion():
    test_ex = [["Breakfast time!", "Japanese", "healthy", "rice", "eat-in"]]
    test_ex_answer = ["Salmon Onigiri"]

    cuisine = "Korean"
    new_suggestions = new_food_suggestion(cuisine)

    assert isinstance(new_suggestions, list)
    assert all(suggestion not in test_ex_answer for suggestion in new_suggestions)

def test_add_new_example():
    test_ex = [["Breakfast time!", "Japanese", "healthy", "rice", "eat-in"]]
    test_ex_answer = ["Salmon Onigiri"]

    time_of_day = "Breakfast time!"
    cuisine = "Italian"
    health = "healthy"
    food_group = "rice"
    eat_preference = "eat-in"
    suggested_food = "Risotto"

    new_entry = [time_of_day, cuisine, health, food_group, eat_preference]
    if new_entry not in test_ex and suggested_food not in test_ex_answer:
        test_ex.append(new_entry)
        test_ex_answer.append(suggested_food)

        assert new_entry in test_ex
        assert suggested_food in test_ex_answer
    else:
        assert new_entry in test_ex
        assert suggest_food in test_ex_answer


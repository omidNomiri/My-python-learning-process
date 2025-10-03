def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate BMI based on weight and height.

    Parameters:
    weight (float): Weight in kilograms.
    height (float): Height in centimeters.

    Returns:
    float: BMI value.
    """
    return weight / ((height / 100) ** 2)


def get_bmi_category(bmi: float) -> str:
    """
    Determine BMI category based on its value.

    Parameters:
    bmi (float): BMI value.

    Returns:
    str: Corresponding BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "Obesity"
    elif 35 <= bmi <= 39.9:
        return "Extreme obesity"
    else:
        return "Morbid obesity"


if __name__ == "__main__":
    weight = float(input("Please enter your weight (kg): "))
    height = float(input("Please enter your height (cm): "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"Your BMI is {bmi} and you are {category}.")

def calculate_bmi(weight, height):
    bmi = (weight * 720) / (height ** 2)
    if bmi < 19:
        return f"BMI: {bmi:.2f} - Below healthy range"
    elif 19 <= bmi <= 25:
        return f"BMI: {bmi:.2f} - Within healthy range"
    else:
        return f"BMI: {bmi:.2f} - Above healthy range"

print(calculate_bmi(150, 68))  

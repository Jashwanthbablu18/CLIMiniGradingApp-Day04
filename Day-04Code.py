# Day 4 - Mini Grading App
# Topic: Operators

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🔹 Welcome to Day 4 of Python 30-Day Challenge!")
    print("🔹 Topic: Operators in Python")
    print("📊 Today we’re building a Mini Grading App using all types of operators in python!\n")

# This function takes mark parameter as an input and gets grade b/w A+ to F based upon the marks that obtained using comparision and logical operators.
def get_grade(mark):
    # This statement returns "A+" if the marks are between 91 - 100,  as well it works for decimals also.
    if (mark >= 91 or mark >= 91.0) and  (mark <= 100 or mark <= 100.0):
        return "A+"
    # This statement returns "A" if the marks are between 81 - 90, as well it works for decimals also.
    elif (mark >= 81 or mark >= 81.0) and (mark <= 90 or mark <= 90.0):
        return "A"
    # This statement returns "B" if the marks are between 71 - 80, as well it works for decimals also.
    elif (mark >= 71 or mark >= 71.0 ) and (mark <= 80 or mark <= 80.0):
        return "B"
    # This statement returns "C" if the marks are between 61 - 70, as well it works for decimals also.
    elif (mark >= 61 or mark >= 61.0) and (mark <= 70 or mark <= 70.0):
        return "C"
    # This statement returns "D" if the marks are between 51 - 60, as well it works for decimals also.
    elif (mark >= 51 or mark >= 51.0) and (mark <= 60 or mark <= 60.0):
        return "D"
    # This statement returns "F" if the marks are between 0 - 50, as well it works for decimals also.
    elif (mark <= 50 or mark <= 50.0):
        return "F"  

# This function takes val as a parameter and checks weather the given value is in between range or not. If valid return true else false. 
def validate_score(val):
    return val >= 0 and val <= 100 


# Main logic
def main():

    # This function calls show_intro() to display a simple welcome msg.
    show_intro()
    
    # This handles the input of the user, This takes input from 0 -100, removes extra spaces by using .strip(). It converts the input into decimal value
    # because user may enter decimal value.
    try:
        # Takes input as str removes extra spaces.
        raw_score = input("Enter student score (0–100): ").strip()

        # Converts into float.
        DecimalScore = float(raw_score)  

    # If user enters an invalid input, it's handle by this one.
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")
        return  
    
    # This one validates the user input by passing DecimalScore into validate_score().
    if not validate_score(DecimalScore):
        print("⚠️ Score must be between 0 and 100.")
        return

    # Asigns DecimalScore to score and initializes bonus with 0.
    score = DecimalScore
    bonus = 0

    # Updating the score and bonus for encouragement.
    if score <= 50 or score <= 50.0:
        print("💡 Adding bonus 5 points for effort!")  # adding some kindness 😅
        score += 5
        bonus = 5

    # Grades them with adjusted score.
    final_grade = get_grade(score)

    # Feedback based on grade.
    # If student fails
    if final_grade == "F":
        feedback = "Needs Improvement 😟"
    # If student not fails
    else:
        feedback = "Well done! 🎉"

    # Displays the final output.
    # Displays final, original scores and if any added bonuses.
    print(f"\n🧾 Final Score: {score} (Original: {DecimalScore}, Bonus: {bonus})")
    # Displys final grade
    print(f"🎓 Grade: {final_grade}")
    # Displays feedback
    print(f"📢 Feedback: {feedback}")

# calling main() to starting execution of program
if __name__ == "__main__":
    main()

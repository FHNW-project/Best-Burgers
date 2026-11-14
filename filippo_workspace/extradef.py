def ask_yes_no(question):
    answer= input(question).strip().lower()
    while answer not in ("yes", "ye", "y", "no", "n"):
        print("Invalid choice, please answer yes or no.")
        answer= input(question).strip().lower()
    return answer in ("yes", "ye", "y")


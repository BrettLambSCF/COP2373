#Brett Lamb
#9/19/2026
#Github: https://github.com/BrettLambSCF/COP2373
#Program to check emails for spam

def check_spam(email_message): #defines first function to check email for spam,
    #with a parameter that represents the email message inputted.
    spam_words_list = [
        "once in a lifetime",
        "winner",
        "weight loss",
        "act now",
        "limited time",
        "meet singles",
        "risk free",
        "financial freedom",
        "cash bonus",
        "no obligation",
        "you have been selected",
        "last chance",
        "cryptocurrency",
        "lottery",
        "sweepstakes",
        "free gift",
        "free money",
        "buy now",
        "bank account",
        "wire transfer",
        "prize",
        "processing fee",
        "claim your prize",
        "no cost",
        "special offer",
        "earn money",
        "work from home",
        "debt relief",
        "extra cash",
        "credit card"
    ]

    spam_score = 0 #starts our spam score at 0
    detected_spam_words = [] #creates our empty list to
    message = email_message.lower() #converts our whole message to lower case characters

    for word in spam_words_list: #creates for loop to go through each word in the list once
        count = message.count(word)

        if count > 0:
            spam_score = spam_score + count
            detected_spam_words.append(word) #each time it goes through the loop, stores spam word in word variable

    return spam_score, detected_spam_words

def get_spam_rating(score): #our second function with parameter score which is our calculated spam score
    #succession of if and elif statements to check where the score lies and probability of spam
    if score == 0:
        return "Very unlikely that this is spam."
    elif score <= 3:
        return "Unlikely to be spam."
    elif score <= 6:
        return "Being spam is possible."
    elif score <= 9:
        return "Likely that this is spam."
    else:
        return "Very likely that this is spam."

def main_function(): #creates a main function where the program runs from
    print("Check Emails For Spam")
    print("---------------------") #makes the program look more clean

    #where we ask the user to input their email
    message = input("Please input your email message: ")

    score, detected_spam_words = check_spam(message) #sends their email off to check it for spam
    rating = get_spam_rating(score) #sends their score into the function to get spam rating

    print()
    print("Spam Score:", score)
    print("Likelihood For Spam:", rating)
    print("Spam words that were found:")

    #tells us how many spam words from the list were in the email
    if len(detected_spam_words) == 0:
        print("No spam words detected.")
    else:
        for word in detected_spam_words:
            print(word)

main_function()
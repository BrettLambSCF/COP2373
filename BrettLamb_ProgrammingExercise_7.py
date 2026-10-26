#Brett Lamb
#10/22/2026
#Github: https://github.com/BrettLambSCF/COP2373
#This program allows the user to enter a paragraph, including sentences that begin
#with numbers. Then it displays each individual sentence and the count of sentences
#in that paragraph.

#Import the regular expression module
import re

#The first function takes the entered paragraph and uses regular expression to find individual sentences
def get_sentences(paragraph):

    #r = raw string, [A-Z0-9] = sentence has to start with A - Z or 1 - 9,. = match almost any character,
    #* = match zero or more characters,? = make * non greedy and stop right when it finds a valid sentence
    #ending, [.!?] = says sentence has to end with . ! ?, (?=) = the look ahead, [A-Z0-9] = look ahead for
    #after the punctuation, look for a space followed by a capital letter or a number, | = or, $ = end of
    #the whole paragraph
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    #re.findall searches the paragraph & anything found that matches the pattern is given pattern variable
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL) #. should also be allowed to match new line
    return sentences

#The second function gets ours sentences and then displays them
def show_sentences(sentences):

    #Needs a \n for new line to make it cleaner
    print("\nEach individual sentence: ")

    #Goes through the sentences list and then puts them into the sentence variable
    for sentence in sentences:
        print(sentence)

    #Needs a \n for new line to make it cleaner
    #Shows the number of sentences by using len to find the length of the list
    print("\nThe number of sentences is:  ", len(sentences))

    #The main function takes the user's input and stores the paragraph in paragraph
def main():
    paragraph = input("Enter your paragraph: ")

    #Call our above functions
    sentences = get_sentences(paragraph)

    show_sentences(sentences)

main()
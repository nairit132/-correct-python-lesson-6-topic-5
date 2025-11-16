class Flashcard:
    def __init__(self,word,definition):
        self.word = word
        self.definition = definition
    def __str__(self):
        return self.word + ' (' + self.definition + ')'
Flash = []
print("Welcome to Flashcard application")
while (True):
    word = input("Enter a word (or type 'exit' to quit): ")
    definition = input("Enter its definition: ")
    Flash.append(Flashcard(word,definition))
    option = input("Do you want to add another flashcard? (yes/no): ")
    if (option):
        break
print("\nYour Flashcards:")
for i in Flash:
    print('>',i)
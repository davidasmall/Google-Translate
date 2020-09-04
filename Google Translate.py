print('----------------------------------------------------')
from googletrans import Translator, LANGUAGES

Answer = 'y'

print()
print("Welcome to Davrhos Translate")
print("Enter a word/phrase/sentence, select a language, and I will translate it for you")


while Answer == 'y':
    print()
    sample_text = input('enter word or sentence: ')
    print()
    user_dest = input('choose a language [use lower case]: ')
    print()
    t = Translator().translate(sample_text , dest = user_dest)
    print(t.text)
    print(t.extra_data['confidence'])
    print(t.extra_data['possible-mistakes'])
    print()
    choice = input("Would you like to translate that through other/more languages? Type 'm' for [MULTIPLE LANGUAGES] or 'all' for [ALL LANGUAGES]: ")
    Answer = input("or alternatively would you like to start again? Type 'y' for YES and 'n' for NO: ")
    if choice == 'all':
        for language in LANGUAGES:
            t = Translator().translate(sample_text , dest = language)
            print(LANGUAGES[language] + ':' + t.text) 
    elif choice == 'm':
        language_list = []
        print()
        n = int(input("Enter no. of languages: "))
        for i in range (0,n):
            element = input("Enter languages: ")
            language_list.append(element)
            print(language_list)
        for language in language_list:
            t = Translator().translate(sample_text , dest = language) 
            print()
            print(t.text) 
            print()
    Answer = input("would you like to translate something else? Type 'y'for YES and 'n' for NO: ")        

# figure out how to print what language each translation is in as well.
      








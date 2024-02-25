def auto_correct(sentence):
    # Dictionary of common misspellings
    corrections = {
        "teh": "the",
        "taht": "that",
        "withe": "with",
        "travil": "travel",
        'greatful': 'grateful',
        'sucess': 'success',
        'sucessful': 'successful',
        'seperate': 'seperate',
        'belevie': 'be',
        'belive': 'believe',
        'recieve': 'receive',
        'travil': 'travel',
        'inglish': "english",
        #add more words to the dictionary
    }

    # Check if the length of the sentence exceeds 35 characters
    if len(sentence) < 35:
        # Auto-correct words in the sentence
        corrected_sentence = ' '.join(corrections.get(word, word) for word in sentence.split())
        return corrected_sentence

    # Check if the sentence contains non-alphabetic characters
    if not sentence.isalpha():
        return "Sentence contains non-alphabetic characters."

    if len(sentence) > 35:
        return "Sentence is too long. Maximum length is 35 characters."


# Test the function
sentence = input("Enter a sentence (up to 35 characters): ")
corrected_sentence = auto_correct(sentence)
print("Corrected sentence:", corrected_sentence)

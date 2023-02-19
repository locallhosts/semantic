import spacy

# Load the medium English language model
nlp = spacy.load('en_core_web_md')

"""
To run the example file with the simpler language model 'en_core_web_sm'
, you can simply change the line that loads the model to:
nlp = spacy.load('en_core_web_md')
To
nlp = spacy.load('en_core_web_sm')

"""



# Define the target words to compare
words = ["apple", "banana", "orange"]

# Calculate the similarity between the words
for word1 in words:
    for word2 in words:
        if word1 != word2:
            similarity = nlp(word1).similarity(nlp(word2))
            print(f"The similarity between '{word1}' and '{word2}' is: {similarity}")


    """
    NOTE:
    When you run the code with the smaller model, you may notice that the similarity scores are slightly lower
    This is because the smaller model has less data and may not be as accurate as the medium model.
    
    """
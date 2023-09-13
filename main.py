import re

with open('./text_analysis/my_text.txt') as file:
    text = file.read()
    
# Let's create a class called analyzer_text to analyze text
class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        # Remove punctuation using a regex pattern
        # Replace '\n' between words with a space
        clean_text_enter = re.sub(r'\n', ' ', text)
        clean_text = re.sub(r'[.,!?¿"]', '', clean_text_enter)
        # lowercase, easier to read :)
        clean_text_lower = clean_text.lower()
        self.format_text = clean_text_lower 
        
    def count_freq(self):
        # split text into list of words first
        words_list = self.format_text.split(" ")
        
        # create a dict to count words
        freq_dict = {}
        # using a set to remove duplicates
        for word in set(words_list):
            freq_dict[word] = words_list.count(word) # to count how many times the word appears in the word list
        return freq_dict
    
    def freq_unique_word(self, word):
        freq_dict = self.count_freq()
        
        if word in freq_dict:
            return f"The word {word.upper()} appears {freq_dict[word]} times in your text."
        else:
            return f"The word {word} is not in your text"

my_clean_text = TextAnalyzer(text)

print(my_clean_text.freq_unique_word("data"))
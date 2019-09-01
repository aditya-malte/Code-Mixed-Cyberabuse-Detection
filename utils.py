import re
import string
import emoji 
    
def preprocess(text):
    #remove urls
    processed_text = re.sub("http\S+", "", text, flags=re.MULTILINE)
   

    #handle hashtags and usernames
    processed_text = re.sub("#", "", processed_text)
    processed_text = re.sub("@", "", processed_text)
    
    
    
    #remove repeated punctuations
    for punctuation in string.punctuation:
        while True:
            replaced =  processed_text.replace(punctuation * 2, punctuation)
            if replaced == processed_text:
                break
            processed_text = replaced
            
    
    
    #tokenize punctuations
    """
    for punctuation in string.punctuation:
        processed_text =  processed_text.replace(punctuation, " " + punctuation+ " ")
    """ 
    
    
    #remove numbers
    processed_text = re.sub("\d+", "", processed_text)
    
    
    
    #convert emojis
    processed_text = emoji.demojize(processed_text)
    
    
    #spell checking
    
    
    
    #convert multiple whitespaces to single
    #detect newline and replace with random string
    processed_text = processed_text.replace("\n", "QSDWDSrfefafawecsd")
    processed_text = re.sub("\s\s+", " ", processed_text)
    #replace again with newline
    processed_text = processed_text.replace("QSDWDSrfefafawecsd", "\n")
    
    """
    #convert to devanagiri
    try:
        translator = Translator()
        processed_text = translator.translate(processed_text, dest='hi').text
    except Exception:
        print(processed_text)
        translator = Translator()
        processed_text = translator.translate(processed_text, dest='hi').text
    print(processed_text)
    """
    
    return processed_text.lower()


print(preprocess("CHECK @out this123!!! \n u`??rl https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python my car another 😅urlhttps://codereview.stackexchange.com/questions/186614/text-cleaning-script-producing-lowercase-words-with-minimal-punctuation"))
print(preprocess("Check out this #url!!???"))

import string
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


ps=PorterStemmer()
def stem(content):
    lower_case = content.lower()
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
    stemmed_content = cleaned_text.split() # into a list
    stemmed_content = [ps.stem(word) for word in stemmed_content if not word in stopwords.words("english")]
    stemmed_content = ' '.join(stemmed_content) # back into a string 
    # stemmed_content = vader.polarity_scores(stemmed_content)
    # if ( stemmed_content['neg'] < stemmed_content['pos']):
    #  return "Positive"
    # elif (stemmed_content['neg'] > stemmed_content['pos']):
    #   return "Negative"
    # else: "Neutral"
    return stemmed_content
    
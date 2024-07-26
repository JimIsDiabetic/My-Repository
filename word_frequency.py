# from nltk.corpus import stopwords
# STOP_WORDS = stopwords.words('english')

STOP_WORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 
               'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 
               'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 
               'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 
               'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 
               'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 
               "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 
               'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 
               'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# from nltk.tokenize import word_tokenize

PUNCT = ['.',',','!','?','"']


def read_file_to_string(filename):
    with open(filename) as f:
      lines = f.readlines()
    return ' '.join(lines)


def process_text(text):
    text = text.lower()

    for i in range(0, len(PUNCT)):
        text = text.replace(PUNCT[i], ' ')

    text = text.split()

    problemNumbers = []

    for i in range(0, len(text)):
        if text[i] in STOP_WORDS:
            problemNumbers.append(i)

    initialProblemNumbersMax = len(problemNumbers) - 1

    for i in range(0, len(problemNumbers)):
        text.pop(problemNumbers[initialProblemNumbersMax - i])
    
    return text

def create_count_dictionary(words):
    dictionary = {}
    
    for i in range(len(words)):
        if words[i] not in dictionary:
            dictionary[words[i]] = 1
        else:
            dictionary[words[i]] += 1

    return dictionary


def main():
    file = 'text_comedy_reviews.txt'

    print("Contents read from " + file + ":")
    contents = read_file_to_string(file)
    print(contents)

    print("\nTokenized word list with no stop words:")
    words = process_text(contents)
    print(words)

    print("\nCount dictionary:")
    word_list = create_count_dictionary(words)
    
    sorted_word_list = sorted(word_list.items())


    for i in range(len(sorted_word_list)):
        largestIndex = 0
        largestCount = 0
        for j in range(i, len(sorted_word_list)):
            if sorted_word_list[j][1] > largestCount:
                largestIndex = j
                largestCount = sorted_word_list[j][1]
        transferVar = sorted_word_list[largestIndex]
        sorted_word_list[largestIndex] = sorted_word_list[i]
        sorted_word_list[i] = transferVar

    sorted_word_list = dict(sorted_word_list)

    print(sorted_word_list)

    


if __name__ == '__main__':
    main()
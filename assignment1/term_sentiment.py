import sys
import json

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    score = 0
    for letter in word:
    	if SCRABBLE_LETTER_VALUES.has_key(letter):
    		score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(letter)
    score += n
    return score


def dict_sentiment(file_sentiment):
	dict = {}
	for line in file_sentiment:
		term, score  = line.split("\t")  
		dict[term] = int(score)
	return dict

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = dict_sentiment(sent_file)

    for tweet in tweet_file:
    	score = 0.0
    	words = []
    	dict = json.loads(tweet)
    	if dict.has_key("text"):
    		strArray = dict["text"].split()
    		for str in strArray:    			
    			if scores.has_key(str):
    				score = score + scores[str]
    			else:
    				words.append(str)
    	for word in words:
    		print "%s %.4f" %(word, getWordScore(word, score))    	
    

if __name__ == '__main__':
    main()

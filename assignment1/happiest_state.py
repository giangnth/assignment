import sys
import json


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
    array_scores = []
    for tweet in tweet_file:
    	score = 0
    	dict = json.loads(tweet)        
    	if dict.has_key("text"):
    		strArray = dict["text"].split()
    		for str in strArray:
    			if scores.has_key(str):
    				score = score + scores[str]
                array_scores.append(score)
    print max(array_scores)
    	

if __name__ == '__main__':
    main()

import sys
import json
from collections import OrderedDict

def main():
    sent_file = open(sys.argv[1])
    dict = {}
    for string in sent_file:
    	dict_child = json.loads(string)
    	if dict_child.has_key("entities"):
            entities = dict_child["entities"]
            if entities.has_key("hashtags") and len(entities["hashtags"]) > 0:
    		hashtags = entities["hashtags"]                
                for tag in hashtags:
                    if tag.has_key("text"):
                        if dict.has_key(tag["text"]):
                            dict[tag["text"]] += 1
                        else:
                            dict[tag["text"]] = 1

    sorted_hashtags = OrderedDict(sorted(dict.items(), key=lambda t: t[1], reverse=True))
    count = 1
    for x,y in sorted_hashtags.items():
        if count == 10:
            break;
    	print "%s %d" %(x, y)
        count +=1
    	

if __name__ == '__main__':
    main()
import sys
import json

def main():
    sent_file = open(sys.argv[1])
    dict = {}
    for string in sent_file:
    	dict_child = json.loads(string)
    	if dict_child.has_key("text"):
    		array = dict_child["text"].split()
    		for str in array:    			
    			if dict.has_key(str.strip()):
    				dict[str.strip()] = dict[str.strip()] + 1
    			else:
    				dict[str.strip()] = 1

    for str in dict:
    	print "%s %.4f" %(str, float(dict[str]) / sum(dict.values()) )
    	

if __name__ == '__main__':
    main()
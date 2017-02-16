### story classifier by ali hashmi

Load all the story text you wish to classify into `inputfile.txt`, with one story on each new line of the .txt file.

The following script will then generate 'outputfile.json', which creates a json file with scores for each story. 

	import multi
	FILENAME = "inputfile.txt"
	OUTPUTJSONFILE = "outputfile.json"
	multi.classifyDocs(FILENAME,OUTPUTJSONFILE)

The json output looks something like this:

	"topics": {
		"Feminism/Women Issues/Gender Issues": "20.13", 
		"Arts": "1.43", 
		"Fashion": "0.67", 
		"Sports": "1.84", 
		"Food": "10.78", 
		"Auto": "2.49", 
		"Energy": "1.91", 
		"Science and Technology": "10.53", 
		"Accident and Disasters": "0.59", 
		"Sexuality": "1.65", 
		"Environment": "1.85", 
		"Religion": "15.69", 
		"Economy and Business": "1.21", 
		"Health": "5.19", 
		"Weather": "6.42", 
		"Politics": "68.46", 
		"Education": "98.8", 
		"Agriculture": "1.05", 
		"Travel": "1.5"
	}

Take the category with the highest score as the categorization for the story. Anecdotally, categories with scores of over 80 or 90 tend to be pretty reliable. If the highest score is less than 80, take the classification with a little more salt than usual.

## Miscellany

Due to some quirk in how pickle works, this code only works on Linux and Mac operating systems; it was pretty unhappy with my Windows system. You'll also have to downgrade scikit-learn to version 0.15, otherwise there are incompatibility issues with the pickled classifiers. This is reflected in `requirements.txt`. Run 
	
	pip install -r requirements.txt

to install the dependencies you need.

# llama_toy
Toy command line fn to use Llama GPT
 
This is a simple toy application to show the use of Llama indexing for GPT.

clone this repo and try:
python3 llama_toy.py -i "queryin.txt" -o "gptout.txt"

usage: llama_toy.py [-h] [-i INFILE] [-q QUERY] [-r READ] [-o OUT]

## options:
  -h, --help 
  -i INFILE, --infile : File to load query from.
  -q QUERY, --query : What you want to ask ChatGPT.
  -r READ, --read : Directory to load from.
  -o OUT, --out : File to save output to.

For this example the default data is included in the repo and is a selection of articles on medium. Copyright remains with the authors of those articles.

## dependencies:
 	Python 3.1+
	LlamaGPT: instructions [here](https://gpt-index.readthedocs.io/en/latest/getting_started/installation.html)

Feel free to PR. 


	

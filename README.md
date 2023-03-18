# llama_toy
Toy command line fn in python to use Llama GPT
 
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

For this example some data is included in the default 'data' directory. As many files as your subscription to OpenAI allows.

## dependencies:
 	Python 3.1+
	LlamaGPT: instructions : https://gpt-index.readthedocs.io/en/latest/getting_started/installation.html
	OpenAI account and API token: https://platform.openai.com/account/api-keys
	(this fn assumes an environment variable set at the OS level)
	

Feel free to PR. 


	

import logging
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", help="File to load query from.")
parser.add_argument("-q", "--query", help="What you want to ask ChatGPT.")
parser.add_argument("-r", "--read", help="Directory to load from.")
parser.add_argument("-o", "--out", help="File to save output to.")

args = parser.parse_args()

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

qry = ""
infile = ""
outfile = ""

if args.infile is None:
    print("no query file provided\n")
    if args.query is None:
        qry = input('enter query:')
    else:
        qry = args.query
        print("command line query is: ", qry, "\n")
else:
    f = open(str(args.infile),"r")
    qry = str(f.readlines())
    print("using query file: ", args.infile, " reading: ", qry, "\n")
    
    
if args.out is None: 
    outf = input('enter file:')
else:
    outf = args.out
    print("using output file: ", outf, "\n")
    
if args.read is None: 
    readr = "data"
    print("using default directory : data\n")
else:
    readr = args.read
    print("reading from directory:", readr, "\n")
    

print('Indexing & Processing...\n')

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
source_docs = SimpleDirectoryReader(readr).load_data()
index = GPTSimpleVectorIndex(source_docs)

response = index.query(qry)
print('Answer: ', response, "\n")

with open(outf, 'w') as f:
    f.write(str(response))
    
    
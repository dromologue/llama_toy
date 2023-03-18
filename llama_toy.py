import logging
import sys
import argparse
import os

# if OS environment variable not set you may set it here.
# os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="File to load query from.")
    parser.add_argument("-q", "--query", help="What you want to ask ChatGPT.")
    parser.add_argument("-r", "--read", help="Directory to load from.")
    parser.add_argument("-o", "--out", help="File to save output to.")
    parser.add_argument("-m", "--model", help="GPT model to use.")
    parser.add_argument("-t", "--temp", help="GPT temperature to use.")
    parser.add_argument("-k", "--tokens", help="Max tokens")
    parser.add_argument("-v", "--verbose", help="To turn on logging, set to YES, or it's ignored.")
    parser.add_argument("-n", "--GPTindex", help="Either KeywordTable [enter K] or SimpleVector [enter V]")
    
    args = parser.parse_args()

    if args.verbose == "YES":
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
        
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

    qry = ""
    infile = ""
    outfile = ""
    tmp = 0
    tkns = 1
    mdl = "none"
    GPTindex = ""

    try:
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
            print("using query file: ", args.infile, "\nreading: \n", qry, "\n")


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

        if args.model is None:
            mdl = "text-davinci-003"
        else:
            mdl = args.model
    
        if args.temp is None:
            tmp = 0
        else:
            tmp = int(args.temp)

        if args.tokens is None:
            tkns = 1024
        else:
            tkns = int(args.tokens)


        print('Indexing & Processing...\n')

        from llama_index import (
            GPTKeywordTableIndex, 
            SimpleDirectoryReader, 
            LLMPredictor,
            GPTSimpleVectorIndex,
        )

        from langchain import OpenAI
        source_docs = SimpleDirectoryReader(readr).load_data()
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=tmp, model_name=mdl, max_tokens=tkns))

        if args.GPTindex == "K":
            index = GPTKeywordTableIndex(source_docs, llm_predictor=llm_predictor)
            index.save_to_disk('index.json')
            print("using keyword index \n")
        elif args.GPTindex == "V":
            index = GPTSimpleVectorIndex(source_docs, llm_predictor=llm_predictor)
            index.save_to_disk('index.json')
            print("using simple vector index \n")
        else:
            index = GPTSimpleVectorIndex(source_docs, llm_predictor=llm_predictor)
            index.save_to_disk('index.json')
            print("using simple vector index \n")
        
        response = index.query(qry)
        print('Answer: ', response, "\n")

        with open(outf, 'w') as f:
            f.write(str(response))
    
    except:
       print("UNHELPFUL ERROR #1: something went wrong... play with your parameters")
    
if __name__ == '__main__':
    main()
    
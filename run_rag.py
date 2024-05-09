import sys
import time
from argparse import ArgumentParser
from rag_pipeline.retrieval import RAGPipeline
import chromadb


def create_cli_parser():

    parser = ArgumentParser(
        prog = "Movies RAG",
        description="Asking question about query plots",
        epilog="Thanks for using"
    )

    parser.add_argument('query', help="A query/question you want answers of")
    parser.add_argument(
        '--path', default="./vector_data", help="Full path to the Chroma DB persist path; defaults to vector_data")
    parser.add_argument(
        '--collection', default="movie_collection", help="Chroma DB collection name; defaults to movie_collection")
    parser.add_argument(
        '--topk', default=20, help = "Number of documents to consider"
    )


    return parser


def run_rag(args):

    print(f" Received {args}")
    parser = create_cli_parser()

    parsed_args = parser.parse_args(args)

    print(f"{parsed_args.query}, {parsed_args.collection}, {parsed_args.path}" )

    query = parsed_args.query

    rag_pipeline = RAGPipeline(
        persist_path=parsed_args.path,
        collection_name=parsed_args.collection
    )
    
    ## Start a timer
    _start = time.time()
    response = rag_pipeline.run_rag(query)
    _end = time.time()
    print(f"Answer is available in {(_end-_start)} seconds")

    movie_matches = response[1]
    

    print("MISTRAL answers with:----- ")
    print(f"{response[0][0]}")
    
    if movie_matches:
        print("Also check these .....")
        for movie in movie_matches:
            print(f"\t Title: {movie[0]}\n\t\t {movie[1]}")
    else:
        print("Apology, we could not find any matching movie known to us")

    
if __name__ == "__main__":

    run_rag(sys.argv[1:])
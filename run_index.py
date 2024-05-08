import sys
import time
from argparse import ArgumentParser
from rag_pipeline.utility import convert_data_to_document
from rag_pipeline.index_pipeline import IndexPipeline

import chromadb


def create_cli_parser():

    parser = ArgumentParser(
        prog = "run_index",
        description="Indexing a movie plot database",
        epilog="Thanks for using"
    )

    parser.add_argument('filename', help="Full path of the source database file")
    parser.add_argument(
        '--path', default="./vector_data", help="Full path to the Chroma DB persist path; defaults to vector_data")
    parser.add_argument(
        '--collection', default="movie_collection", help="Chroma DB collection name; defaults to movie_collection")


    return parser


def run_indexing(args):

    print(f" Received {args}")
    parser = create_cli_parser()

    parsed_args = parser.parse_args(args)

    print(f"{parsed_args.filename}, {parsed_args.collection}, {parsed_args.path}" )

    source_file = parsed_args.filename

    movie_documents = convert_data_to_document(source_file)

    print(f"{len(movie_documents)} movies found in database")

    print("Creating indexes ....")
    indexer = IndexPipeline(
        parsed_args.path,
        parsed_args.collection
    )

    ## Start a timer
    _start = time.time()
    indexer.run_pipeline(movie_documents)
    _end = time.time()
    print(f"Finished indexing in {(_end-_start)/60} minutes")

    print("Checking Database")

    chroma_client = chromadb.PersistentClient(path=parsed_args.path)
    collection = chroma_client.get_collection(parsed_args.collection)
    movies_in_db = collection.count()
    print(f"Found {movies_in_db} movies indexed in DB.")


if __name__ == "__main__":

    run_indexing(sys.argv[1:])
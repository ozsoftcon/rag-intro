from typing import List, Dict, Any
from csv import reader
from haystack import Document


def process_movie_data(data: List[str], movie_types) -> Dict[str, Any]:

    title = data[0]
    plot = data[1].strip()
    type_info = data[2:]

    types = []
    for idx, type_info in enumerate(type_info):
        if type_info == "0":
            continue
        types += [movie_types[idx]]
    
    return {
        "content": plot,
        "meta": {
            "title": title,
            "movie_types": ",".join(types)
        }
    }

def process_header(header: List[str]) -> List[str]:

    types = header[2:]
    return types


def convert_data_to_document(
        filepath: str
) -> List[Document]:
    
    movie_documents = []
    with open(filepath, newline="\n") as sourcefile:
        data = reader(sourcefile, delimiter="\t", quotechar='"')
        header = data.__next__()
        movie_types = process_header(header)

        for movie_data in data:

            processed_data = process_movie_data(
                movie_data, movie_types
            )
            document = Document(
                content = processed_data["content"],
                meta = processed_data["meta"]
            )
            movie_documents.append(document)
    return movie_documents



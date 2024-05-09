# Introduction to RAG

This is a very simply development and application of RAG Pipeline using open source tools. We want to be able to ask questions on a movie database.

NOTE: The code is tested on MAC (Apple M3 Max)

The tools we are going to use are `haystack-ai`, `Ollama + mistral`, `Chroma DB`.

## Set up

### Cloning the repo

```
$ git clone ...
```

Once you clone the repo move to the directory when code is downloaded. This document will refer to the directory as `$RAG_DIR`

### Creating the environment

From inside the `$RAG_DIR`, run

```
$ python3 -m venv ./<env_name>
$ source ./<env_name>/bin/activate
<env_name> $ pip install -r requirements.txt
```

### Setting up the Ollama service

- Download the required installer from [Ollama](https://github.com/ollama/ollama) [for Mac users unzip and move it to Application]
- Pull the `mistral` model `ollama pull mistral`
- Run the Ollama serve `ollama serve`

This will start the server at `http://localhost:11434`

### Chroma DB

Currently, `haystack.ai` supports `in-memory` and `peristent` mode for Chroma DB. This means no separate service is required to run. However, if you are interested, you can consult [Chroma DB documentation](https://docs.trychroma.com/) and its [support in `haystack`](https://docs.haystack.deepset.ai/reference/integrations-chroma#chromadocumentstore)

### Install the `rag_pipeline` package

```
$ python setup.py install
$ pytest test/unit/test_**
```
NOTE: If the tests pass, the package installation is successful.

## RAG Pipeline

This simple example is a slight modification of the pipeline available in [`haystack` documentation](https://haystack.deepset.ai/overview/quick-start#installation). For us, we have a movie database with plots (along with some meta data). We want to ask questions and get answers about movie plots.

### First Step : Indexing the Data

```
<env_name> $ python run_index.py --path PATH --collection COLLECTION filename
```

where

- `filename` is the full path to the movies database file (included in the code)
- `PATH` is the full path to the Chroma DB persist location; it can be any location within disk.
- `COLLECTION` is a name for the indexed collection within Chroma DB

The database has 117352 movies.

Complete indexing of the data (no optimization) took 654 minutes. The compute spec (the compute was running the indexing pipeline and the Ollama service) was

- System : `macOS 14.4.1`
- Kernel : `Darwitn 23.4.0`
- Chip   : Apple M3 Max
- Cores  : 14
- Memory : 36 GB

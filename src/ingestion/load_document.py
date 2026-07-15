
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
import logging
logger = logging.getLogger(__name__)
def load_pdfs() -> list:
    logger.info("Loading documents")
    documents = SimpleDirectoryReader(
        input_dir="../data",
        recursive=True,
        required_exts=[".pdf"]
    ).load_data()

    logger.info(f"Loaded {len(documents)} documents")
    logger.info("first file name %s",documents[0].metadata["file_name"])
    return documents

def load_web_documents() -> list:
    raise NotImplementedError("implement the web page reader")


def documents_to_chunks(documents, config) -> list:
    logger.info("spliting documents into chunks")
    spliter = SentenceSplitter(chunk_size= config.chunk_size, chunk_overlap= config.chunk_overlap)
    chunks = spliter.get_nodes_from_documents(documents)
    return chunks
    # print(f"no of chunks : {len(chunks)}")
    # print(chunks[0].text[:500])
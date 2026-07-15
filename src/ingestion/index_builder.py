from llama_index.core import VectorStoreIndex
import logging
logger = logging.getLogger(__name__)
def build_index(chunks, model):
    logger.info("Building index from %d chunks", len(chunks))
    index = VectorStoreIndex(nodes=chunks,embed_model = model)
    logger.info("Index created successfully")
    return index
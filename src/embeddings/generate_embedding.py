from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import logging
logger = logging.getLogger(__name__)
def get_embedding_model(config):
    logger.info("initializing embedding model")
    return HuggingFaceEmbedding(
    model_name=config.model_name)
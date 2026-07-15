from dataclasses import dataclass

@dataclass
class ChunkConfig:
    chunk_size: int = 800
    chunk_overlap: int = 100

@dataclass
class EmbeddingConfig:
    model_name :str = "BAAI/bge-small-en-v1.5"

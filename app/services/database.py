import os
from llama_index.vector_stores import AstraDBVectorStore

def connect_to_db():
  db = AstraDBVectorStore(
    token=os.environ['ASTRA_DB_APPLICATION_TOKEN'],
    api_endpoint=os.environ['ASTRA_DB_APPLICATION_TOKEN'],
    collection_name=os.environ['ASTRA_DB_API_ENDPOINT'],
    embedding_dimension=512
  )
  return db
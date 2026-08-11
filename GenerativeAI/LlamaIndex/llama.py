import os
from dotenv import load_dotenv

from llama_index.core import (
    SimpleDirectoryReader,
    Settings,
    VectorStoreIndex,
)

from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


load_dotenv()

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN is not set in the environment.")

llm = HuggingFaceInferenceAPI(
    model_name="Qwen/Qwen2.5-72B-Instruct",
    token=hf_token,
)

Settings.llm = llm

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

documents = SimpleDirectoryReader(
    "../../Documents"
).load_data()

print(f"Loaded {len(documents)} document(s).")


vector_store_index = VectorStoreIndex.from_documents(
    documents
)

query_engine = vector_store_index.as_query_engine()

response = query_engine.query(
    "Summarize the key points from the documents."
)


print("\nResponse from LlamaIndex:")
print(response)
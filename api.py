import pathway as pw
import os
import time
from dotenv import load_dotenv
from common.embedder import embeddings, index_embeddings
from common.prompt import prompt
from llm_app import chunk_texts, extract_texts

load_dotenv()

dropbox_folder_path = os.environ.get("DROPBOX_LOCAL_FOLDER_PATH", "/usr/local/documents")
rate_limit = float(os.environ.get("API_RATE_LIMIT", 1))  # Default to 1 calls per second

def run(host, port):
    last_call_time = 0

    while True:
        current_time = time.time()
        if current_time - last_call_time < rate_limit:
            time.sleep(rate_limit - (current_time - last_call_time))

        # Given a user search query
        query, response_writer = pw.io.http.rest_connector(
            host=host,
            port=port,
            schema=QueryInputSchema,
            autocommit_duration_ms=50,
        )

        # Real-time data coming from external unstructured data sources like a PDF file
        input_data = pw.io.fs.read(
            dropbox_folder_path,
            mode="streaming",
            format="binary",
            autocommit_duration_ms=50,
        )
        
        # Chunk input data into smaller documents
        documents = input_data.select(texts=extract_texts(pw.this.data))
        documents = documents.select(chunks=chunk_texts(pw.this.texts))
        documents = documents.flatten(pw.this.chunks).rename_columns(chunk=pw.this.chunks)

        # Compute embeddings for each document using the OpenAI Embeddings API
        embedded_data = embeddings(context=documents, data_to_embed=pw.this.chunk)

        # Construct an index on the generated embeddings in real-time
        index = index_embeddings(embedded_data)

        # Generate embeddings for the query from the OpenAI Embeddings API
        embedded_query = embeddings(context=query, data_to_embed=pw.this.query)

        # Build prompt using indexed data
        responses = prompt(index, embedded_query, pw.this.query)

        # Feed the prompt to ChatGPT and obtain the generated answer.
        response_writer(responses)

        last_call_time = time.time()

class QueryInputSchema(pw.Schema):
    query: str

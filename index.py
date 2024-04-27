from pinecone import Pinecone
from dotenv import load_dotenv
import os, csv
import pandas as pd
from io import StringIO
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()
def create_embeddings():
    embeddings_model = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(index_name="shortpp", embedding=embeddings_model)
    # adding fix of https://github.com/langchain-ai/langchain/pull/20701 to load certain fields
    file = './test.csv'
    file = './public_up_to_150k_12_230930.csv'
    output_file = './output.csv'
    df = pd.read_csv(file)
    df.to_csv(output_file, columns=['LoanNumber','BorrowerName'])
    # source can be used to find loadnumber in metadata
    loader = CSVLoader(
        file_path=output_file,
        source_column="LoanNumber"
    )
    docs = loader.load()
    vectorstore.add_documents(docs)
# create_embeddings()
def search(query):
    embeddings_model = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(index_name="shortpp", embedding=embeddings_model)
    docs = vectorstore.similarity_search(query, k=1)
    print(docs[0].metadata['source'])
    loan_number = int(docs[0].metadata['source'])
    return loan_number
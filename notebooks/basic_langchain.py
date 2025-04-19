#!/usr/bin/env python3
"""
LangChain 基本チュートリアル
このスクリプトではLangChainの基本的な使い方を紹介します。
"""

import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

print("## 1. 基本的なLLMの使用")
from langchain_community.llms import Ollama

# LLMの初期化
llm = Ollama(model="llama3")

# 直接質問する
print("質問: LangChainとは何ですか？")
response = llm.invoke("LangChainとは何ですか？")
print(f"回答: {response}")

print("\n## 2. プロンプトテンプレート")
from langchain.prompts import PromptTemplate

# プロンプトテンプレートの作成
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="{topic}について詳しく説明してください。"
)

# テンプレートから具体的なプロンプトを生成
prompt = prompt_template.format(topic="LangChain")
print(f"生成されたプロンプト: {prompt}")

# LLMに問い合わせ
response = llm.invoke(prompt)
print(f"回答: {response}")

print("\n## 3. チェーンの基本")
from langchain.chains import LLMChain

# チェーンの作成
chain = LLMChain(llm=llm, prompt=prompt_template)

# チェーンの実行
print("質問: RAG (Retrieval Augmented Generation)について")
response = chain.invoke({"topic": "RAG (Retrieval Augmented Generation)"})
print(f"回答: {response['text']}")

print("\n## 4. シンプルなRAG (Retrieval Augmented Generation)")
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# サンプルドキュメント
documents = [
    "LangChainは大規模言語モデル（LLM）アプリケーションを構築するためのフレームワークです。",
    "LangChainはプロンプト管理、チェーニング、データ接続などの機能を提供します。",
    "RAG（Retrieval Augmented Generation）は文書検索とLLMを組み合わせる手法です。",
    "LangChainを使うと、複雑なLLMのワークフローを簡単に構築できます。"
]

# テキスト分割
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.create_documents(documents)

# ベクトルストアの作成（OllamaのEmbeddingsを使用）
embeddings = OllamaEmbeddings(model="llama3")
db = Chroma.from_documents(texts, embeddings)

# 検索クエリ
query = "RAGとは何ですか？"
print(f"検索クエリ: {query}")
docs = db.similarity_search(query)
print("検索結果:")
for doc in docs:
    print(f"- {doc.page_content}")

print("\n## 5. RAGと組み合わせたチェーン")
from langchain.chains import RetrievalQA

# RetrievalQAチェーンの作成
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# 質問に回答
query = "LangChainでできることは？"
print(f"質問: {query}")
result = qa_chain.invoke({"query": query})
print(f"回答: {result['result']}")
print("\n参照ドキュメント:")
for doc in result['source_documents']:
    print(f"- {doc.page_content}") 
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 環境変数を読み込む
load_dotenv()

app = FastAPI(title="LangChain API Demo")

# OllamaのLLMを初期化（Docker環境ではollama:11434、ローカルではlocalhost:11434）
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")
llm = Ollama(model="llama3", base_url=f"http://{OLLAMA_HOST}:11434")

# プロンプトテンプレート
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""あなたは親切で丁寧な日本語アシスタントです。
以下の質問に日本語で答えてください。

質問: {question}

回答:"""
)

# LLMチェーン
chain = LLMChain(llm=llm, prompt=prompt_template)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "Welcome to LangChain API Demo"}

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # LangChainを使って質問に回答
        response = chain.invoke({"question": request.question})
        return {"answer": response["text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
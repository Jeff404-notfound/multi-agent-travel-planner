from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:4b",
    base_url="http://172.30.48.1:11434",
)

response = llm.invoke(
    "Give me 3 tourist attractions in Goa. Keep the answer short."
)

print(response.content)

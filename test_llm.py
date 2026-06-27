from src.llm import load_llm

try:
    llm = load_llm()
    print("LLM loaded successfully")

    response = llm.invoke("What is Artificial Intelligence?")
    print(response.content)

except Exception as e:
    import traceback
    traceback.print_exc()
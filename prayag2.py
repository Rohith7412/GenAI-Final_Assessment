from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are my AI assistant. "
        "Explain concepts clearly and simply."
    ),
    (
        "human",
        "{question}"
    )
])
parser = StrOutputParser()
chain = prompt | model | parser

print("==============================")
print("        LangChain AI Chatbot")
print("==============================")
print("Type 'exit' to stop.\n")

while True:

    user_input = input("you: ")

    if user_input.lower() == "exist":
        print("Goodbye!")
        break

    response = chain.invoke({
        "question": user_input
    })

    print("AI:", response.content)

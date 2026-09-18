from transformers import pipeline

LLM = pipeline(
    "text-generation",
    model="google/flan-t5-small"
)

print("Small LLM chatbot")
print("Press 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = LLM(
        user_input,
        max_new_tokens=100
    )

    print("LLM:", response[0]["generated_text"])
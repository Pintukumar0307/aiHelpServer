import openai

# Set your OpenAI API key
openai.api_key = "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"

def response(user_input):
    
    print("Chatbot: Hello! I'm here to help. Type 'exit' to end the conversation.")

   # Start the conversation with a system message
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    # Add the user's message to the conversation
    conversation.append({"role": "user", "content": user_input})
    
    # Simulate a chat conversation
    responses = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    # Extract and print the assistant's response
    assistant_response = responses.choices[0].message['content']
    # print(f"Chatbot: {assistant_response}")
    
    
    # Add the assistant's response to the conversation
    conversation.append({"role": "assistant", "content": assistant_response})
    
    return  assistant_response

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("Chatbot: Goodbye!")
#         break
    
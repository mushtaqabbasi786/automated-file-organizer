# Simple keyword-based chatbot

# Dictionary to hold keywords and their responses
RESPONSES = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "hours": "We are open Monday to Friday from 9 AM to 6 PM.",
    "timing": "Our timings are 9:00 AM - 6:00 PM on weekdays.",
    "price": "Please visit our website catalog for product pricing.",
    "shipping": "Standard shipping takes 3 to 5 business days.",
    "refund": "We offer a 30-day return policy for all products."
}

print("=" * 50)
print("             SIMPLE INTERACTIVE CHATBOT            ")
print("=" * 50)
print("Bot: Hello! Type 'exit', 'bye', or 'quit' to end the chat.\n")

while True:
    # Get input, convert to lowercase, and remove extra spaces
    user_input = input("You: ").lower().strip()
    
    # Check for exit commands
    if user_input in ['exit', 'bye', 'quit']:
        print("Bot: Goodbye! Have a great day.")
        print("=" * 50)
        break
        
    # Skip empty inputs
    if not user_input:
        continue
        
    # Search for keywords in the user's input
    found_match = False
    for keyword, response in RESPONSES.items():
        if keyword in user_input:
            print(f"Bot: {response}\n")
            found_match = True
            break # Stop searching once a match is found
            
    # Fallback if no keywords match
    if not found_match:
        print("Bot: I'm sorry, I don't understand that. Try asking about 'hours', 'price', or 'shipping'.\n")

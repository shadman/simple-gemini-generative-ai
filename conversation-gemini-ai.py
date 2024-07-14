import google.generativeai as genai

GOOGLE_API_KEY = "YOUR KEY"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-latest')

conversation = model.start_chat()

while True:
    user_input = input('Gemini Promot: ')
    conversation.send_message(user_input)
    print(conversation.last.text)
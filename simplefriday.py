import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# 1. Automatically load keys from your hidden local .env file
load_dotenv()

# 2. Check if the key loaded successfully
if not os.getenv("GOOGLE_API_KEY"):
    print("⚠️ Error: GOOGLE_API_KEY not found! Make sure your .env file exists and contains your key.")
    exit()

print("Booting up F.R.I.D.A.Y.'s core logic. . .")

# 3. Initialize the AI Brain (Gemini 2.5 Flash)
brain = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# 4. Identity coaching
identity = SystemMessage(
    content="You are F.R.I.D.A.Y., a highly advanced AI assistant. Your user is Tejas, an AIML student. Be concise, witty, and helpful."
)

print("F.R.I.D.A.Y. is online. Type 'exit' to turn off the system.")
print("---------------------------------------------")

# 5. Continuous Loop
while True:
    user_input = input("\nTejas: ")

    if user_input.lower() in ["exit", "quit", "go offline"]:
        print("F.R.I.D.A.Y.: Systems powering down. Goodbye, Boss.")
        break

    if not user_input.strip():
        continue

    user_message = HumanMessage(content=user_input)
    
    try:
        response = brain.invoke([identity, user_message])
        print(f"F.R.I.D.A.Y.: {response.content}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")
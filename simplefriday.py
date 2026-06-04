import os
from dotenv import dotenv_values
import pyttsx3
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# 1. Safely pull your keys from the local environment vault
config = dotenv_values(".env")
api_key = config.get("GOOGLE_API_KEY")

if not api_key:
    print("⚠️ Error: GOOGLE_API_KEY not found inside your local .env file!")
    exit()

os.environ["GOOGLE_API_KEY"] = api_key

print("Booting up F.R.I.D.A.Y.'s core logic. . .")

# 2. Synchronize Audio Engine Properties
voice_engine = pyttsx3.init()
voices = voice_engine.getProperty('voices')

if len(voices) > 1:
    voice_engine.setProperty('voice', voices[1].id)

voice_engine.setProperty('rate', 185)

# The Core Speaking Mechanism
def speak(text):
    # 1. Initialize a clean, isolated voice engine instance for this sentence
    local_engine = pyttsx3.init()
    
    # 2. Grab the system voices inside this local instance
    local_voices = local_engine.getProperty('voices')
    if len(local_voices) > 1:
        local_engine.setProperty('voice', local_voices[1].id)
        
    local_engine.setProperty('rate', 185)
    
    # 3. Speak the text out loud
    local_engine.say(text)
    local_engine.runAndWait()
    
    # 4. Explicitly stop and release the hardware thread back to Windows
    local_engine.stop()
# 3. Initialize AI Model Connection Array
brain = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.7
)

identity = SystemMessage(
    content="You are F.R.I.D.A.Y., a highly advanced AI assistant. Your user is Tejas, an AIML student. Be concise, witty, and helpful."
)

print("F.R.I.D.A.Y. is online. Type 'exit' to turn off the system.")
print("---------------------------------------------")

# 4. Continuous Input-Output Evaluation Loop
while True:
    user_input = input("\nTejas: ")

    if user_input.lower() in ["exit", "quit", "go offline"]:
        print("F.R.I.D.A.Y.: Systems powering down. Goodbye, Boss.")
        speak("Systems powering down. Goodbye, Boss.")
        break

    if not user_input.strip():
        continue

    user_message = HumanMessage(content=user_input)
    
    try:
        response = brain.invoke([identity, user_message])
        print(f"F.R.I.D.A.Y.: {response.content}")
        
        # This routes the AI response straight into the speech synthesis pipeline
        speak(response.content)
        
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")
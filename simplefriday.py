import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDIbqkVhrIIPQ-QYiRBdOsFj1fcIRu2p28"

print("Booting up F.R.I.D.A.Y.'s core logic. . .")

brain = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


identity = SystemMessage(
    content="You are F.R.I.D.A.Y., a highly advanced AI assistant, Your user is Tejas, an AIML student, Be concise, witty, and helpful."

)

print("F.R.I.D.A.Y. is online. Type 'exit' to turn off the system.")
print("---------------------------------------------")

while True:
    user_input = input("\nTejas: ")

    if user_input.lower() in ["exit","quit", "go offline"]:
        print("F.R.I.D.A.Y.: Systems powering down. Goodbye, Boss.")
        break

    user_message = HumanMessage(content=user_input)

    response = brain.invoke([identity, user_message])

    print(f"F.R.I.D.A.Y.: {response.content}")

from llm import ask_ai
import time 

print("="*60)
print("🤖 KOVE | Your Professional AI Learning Tutor😊")
print("="*60)

print("1. Study Mentor")
print("2. Interview Coach")
print("3. Quiz Generator")
print("4. Coding Mentor")

choice = input("\nChoose Mode : ")

def stream_text(text):

    words = text.split() #it splits the user question.

    for word in words:  

        print(word, end=" ", flush=True) #flush forces python to immediatley display the response tokens

        time.sleep(0.08) #gives a typing effect

    print()

while True:
    
    question = input("\nYou : ")
    if question.lower() == "exit":
        break
    answer = ask_ai(choice, question)
    print("\n🤖 Kove AI:")
    stream_text(answer)
    
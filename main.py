import sys

sys.stdout.reconfigure(encoding="utf-8")

from speech_to_text import listen
from llm import ask_ai
from text_to_speech import speak

print("=" * 50)
print(" Voice AI Assistant Started")
print("Say 'Exit' or 'خروج' to stop.")
print("=" * 50)

while True:

    try:
        # الاستماع إلى المستخدم
        user_message = listen()

        if not user_message:
            continue

        print(f"\n Rayan: {user_message}")

        # إيقاف البرنامج
        if user_message.lower() in ["exit", "quit"] or "خروج" in user_message:
            goodbye = "Goodbye! Have a nice day."

            if "خروج" in user_message:
                goodbye = "إلى اللقاء، أتمنى لك يوماً سعيداً."

            print(f"\n Assistant: {goodbye}")
            speak(goodbye)
            break

        # إرسال الرسالة إلى Cohere
        response = ask_ai(user_message)

        # عرض الرد
        print(f"\n Assistant: {response}")

        # تشغيل الرد صوتياً
        speak(response)

    except KeyboardInterrupt:
        print("\n\nProgram stopped.")
        break

    except Exception as e:
        print("\nError:", e)
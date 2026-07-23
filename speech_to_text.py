import speech_recognition as sr
import whisper
import tempfile
import os

# تحميل موديل Whisper (يمكن تغييره إلى small أو medium لتحسين العربية)
model = whisper.load_model("base")

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("\n Listening...")

        # تقليل الضوضاء
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # تسجيل الصوت
        audio = recognizer.listen(source)

    # حفظ الصوت مؤقتًا
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio.get_wav_data())
        temp_path = temp_audio.name

    # تحويل الصوت إلى نص
    result = model.transcribe(
        temp_path,
        language=None,     # يكتشف اللغة تلقائيًا (عربي أو إنجليزي)
        fp16=False
    )

    # حذف الملف المؤقت
    os.remove(temp_path)

    # استخراج النص
    text = result["text"].strip()

    # طباعة معلومات التعرف (للتجربة)
    print("\nDetected Language:", result["language"])
    print("Recognized Text:", text)

    return text
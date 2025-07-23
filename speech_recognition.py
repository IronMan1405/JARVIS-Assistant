from vosk import Model, KaldiRecognizer
import pyaudio
import json

def get_voice_command():
    model = Model("models/vosk-model-small-en-us-0.15")
    recogniser = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    stream.start_stream()

    print("Listening...")

    while True:
        data = stream.read(4000, exception_on_overflow=False)

        if recogniser.AcceptWaveForm(data):
            result = json.loads(recogniser.Result())
            cmd = result.get("text", "").strip()

            if cmd:
                stream.stop_stream()
                stream.close()
                p.terminate()
                return cmd
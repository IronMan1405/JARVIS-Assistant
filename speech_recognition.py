import os, sys, ctypes
# sys.stderr = open(os.devnull, "w")

def suppress_stderr():
    sys.stderr.flush()
    devnull = os.open(os.devnull, os.O_WRONLY)
    libc = ctypes.CDLL(None)
    stderr_fileno = sys.__stderr__.fileno()
    libc.dup2(devnull, stderr_fileno)

suppress_stderr()

from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model("models/vosk-model-small-en-us-0.15")

def get_voice_command():
    recogniser = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    stream.start_stream()

    print("Listening...")

    while True:
        data = stream.read(4000, exception_on_overflow=False)

        if recogniser.AcceptWaveform(data):
            result = json.loads(recogniser.Result())
            cmd = result.get("text", "").strip()

            if cmd:
                stream.stop_stream()
                stream.close()
                p.terminate()
                return cmd
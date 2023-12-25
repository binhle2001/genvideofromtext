import re
import unicodedata
from argparse import ArgumentParser
from pathlib import Path
import time
import soundfile as sf
from pydub import AudioSegment
from .hifigan.mel2wave import mel2wave
from .nat.config import FLAGS
from .nat.text2mel import text2mel

import shutil
import os

OUTPUT_DIR = "ai_core/tts/output/chunks"
SAMPLE_RATE = 16000
silence_duration = 0.2




def nat_normalize_text(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.lower().strip()
    sil = FLAGS.special_phonemes[FLAGS.sil_index]
    text = re.sub(r"[,]+", f" {FLAGS.special_phonemes[0]} ", text)
    text = text.replace('"', " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[\n.:;?!]+", f" {FLAGS.special_phonemes[2]} ", text)
    text = re.sub("[ ]+", " ", text)
    text = re.sub(f"( {FLAGS.special_phonemes[0]}+)+ ", f" {FLAGS.special_phonemes[0]} ", text)
    return text.strip()


def convert_text_to_speech(string, speed = 1, vocal = "female", language = "VI"):
    lexicon_file = f"ai_core/tts/model/{language}/{vocal}/lexicon.txt"
    sample_rate = int(SAMPLE_RATE * speed)
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    array = string.split(".")
    for sentence in array:
        output_file = OUTPUT_DIR + '/' + str(time.time()) + ".wav"
        text = nat_normalize_text(sentence)
        # print("Normalized text input:", text)
        mel = text2mel(text, lexicon_file, silence_duration, vocal, language)
        wave = mel2wave(mel, language, vocal = vocal)
        # print("writing output to file", output_file)
        sf.write(str(output_file), wave, samplerate= sample_rate)
        
    shutil.rmtree("ai_core/wav2lip/data/output", ignore_errors=True)
    os.makedirs("ai_core/wav2lip/data/output", exist_ok=True)
    folder = os.listdir("ai_core/tts/output/chunks")

    # Danh sách tên file audio WAV
    file_names = ["ai_core/tts/output/chunks/" + file_name for file_name in folder]

    # Tạo một danh sách các đối tượng AudioSegment từ các file
    audio_segments = [AudioSegment.from_wav(file_name) for file_name in file_names]

    # Nối các đối tượng AudioSegment với nhau
    combined = sum(audio_segments)

    # Lưu kết quả
    combined.export("ai_core/wav2lip/data/output/output_audio.wav", format="wav")
    return "ai_core/wav2lip/data/output/output_audio.wav"
    


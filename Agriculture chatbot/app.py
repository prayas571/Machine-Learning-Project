import os
from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
from gtts import gTTS
import random
import string

from groq import Groq

from dotenv import load_dotenv




app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'webm', 'wav', 'mp3', 'm4a'}

groq_client = Groq(api_key=)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def transcribe_audio_groq(filepath):
    with open(filepath, "rb") as f:
        response = groq_client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=f,
        )
        return response.text


def get_answer_groq(question):
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ SAME WORKING MODEL
            messages=[
                {"role": "system", "content": "You are a helpful agriculture chatbot for Indian farmers."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("FULL ERROR:", e)
        return f"❌ Error fetching response: {str(e)}"





def text_to_audio(text, filename):
    tts = gTTS(text)
    audio_path = os.path.join("static/audio", f"{filename}.mp3")
    tts.save(audio_path)
    return audio_path


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    if 'audio' in request.files:
        audio = request.files['audio']
        if audio and allowed_file(audio.filename):
            filename = secure_filename(audio.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            audio.save(filepath)
            transcription = transcribe_audio_groq(filepath)
            answer = get_answer_groq(transcription)
            voice_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            text_to_audio(answer, voice_filename)
            return jsonify({
                'text': f"🎤 Transcribed: {transcription}\n\n🤖 Answer: {answer}",
                'voice': url_for('static', filename='audio/' + voice_filename + '.mp3')
            })

    elif 'text' in request.form:
        question = request.form['text']
        answer = get_answer_groq(question)
        voice_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        text_to_audio(answer, voice_filename)
        return jsonify({
            'text': answer,
            'voice': url_for('static', filename='audio/' + voice_filename + '.mp3')
        })

    return jsonify({'text': 'No valid input found'}), 400


if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static/audio", exist_ok=True)
    app.run(debug=True)

import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv
import assemblyai as aai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Replace with your AssemblyAI API key
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

transcript_data = None  # Global variable to store transcript data
transcript_obj = None  # Global variable to store the actual transcript object

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Transcribe the uploaded file using AssemblyAI
        transcriber = aai.Transcriber()
        config = aai.TranscriptionConfig(speaker_labels=True)
        global transcript_obj
        transcript_obj = transcriber.transcribe(file_path, config=config)

        global transcript_data
        transcript_data = [
            {
                'speaker': utterance.speaker,
                'start_time': f"{utterance.start // 1000}.{utterance.start % 1000:03d}",
                'end_time': f"{utterance.end // 1000}.{utterance.end % 1000:03d}",
                'text': utterance.text
            }
            for utterance in transcript_obj.utterances
        ]

        return redirect(url_for('transcript'))

@app.route('/transcript')
def transcript():
    global transcript_data
    return render_template('transcript.html', transcript_data=transcript_data)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message')

    global transcript_obj

    # Here, we use the lemur task to process the user message
    if transcript_obj and hasattr(transcript_obj, 'lemur') and hasattr(transcript_obj.lemur, 'task'):
        response_message = transcript_obj.lemur.task(user_message).response
    else:
        return jsonify({'error': 'Lemur task not available in transcript'}), 400
    
    # Print the response (for debugging purposes)
    print(response_message)

    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

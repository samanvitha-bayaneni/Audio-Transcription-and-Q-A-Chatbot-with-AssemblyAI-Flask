# [Audio Transcription and Q&A Chatbot](https://drive.google.com/file/d/1fM5ag9HYYQpXh6luFd04N_Bw2Ery6MqJ/view?usp=sharing)

<img src="https://www.dictalogic.com/assets/images/Dictalogic%20GIfs/Audio%20Only%20Header.gif" width=500>

```markdown

This Flask application allows users to upload an audio file, transcribe it using AssemblyAI, and then ask questions based on the transcript.

## Features

- Upload an audio file (mp3/mp4)
- Transcribe the audio file using AssemblyAI
- Display the transcript with speaker labels and timestamps
- Chat interface for asking questions based on the transcript

## Prerequisites

- Python 3.6+
- An AssemblyAI API key


1. Open your web browser and go to `[http://localhost:5000](https://final-llm.onrender.com/)`.

2. Upload an audio file. Once the file is uploaded and transcribed, the transcript will be displayed along with a chat interface for asking questions.

## File Structure

- `app.py`: Main application file containing Flask routes and logic.
- `requirements.txt`: List of dependencies.
- `templates/`: Directory containing HTML templates.
  - `upload.html`: Template for the file upload page.
  - `transcript.html`: Template for displaying the transcript and chat interface.

## Dependencies

Ensure you have the following dependencies in your `requirements.txt`:

- Flask==2.0.1
- assemblyai==0.10.0
- requests==2.25.1
- python-dotenv==0.19.2

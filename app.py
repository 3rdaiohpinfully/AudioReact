from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure upload directories exist
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'images'), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'audios'), exist_ok=True)
os.makedirs('processed/animations', exist_ok=True)

@app.route('/')
def index():
    animation = request.args.get('animation')
    return render_template('index.html', animation=animation)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files or 'audio' not in request.files:
        return redirect(request.url)
    
    image = request.files['image']
    audio = request.files['audio']

    if image.filename == '' or audio.filename == '':
        return redirect(request.url)

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'images', image.filename)
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audios', audio.filename)

    image.save(image_path)
    audio.save(audio_path)

    # Process the files to create reactive animation
    animation_path = create_reactive_animation(image_path, audio_path)

    return redirect(url_for('index', animation=animation_path))

def create_reactive_animation(image_path, audio_path):
    # Placeholder for actual processing code
    # Use the functions from the provided repository to process files
    animation_path = 'processed/animations/output.mp4'
    # Code to process the image and audio to create animation
    return animation_path

if __name__ == '__main__':
    app.run(debug=True)

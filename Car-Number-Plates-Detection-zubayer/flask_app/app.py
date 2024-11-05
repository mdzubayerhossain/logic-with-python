from flask import Flask, render_template, request, redirect, url_for, flash
import cv2
import os
import uuid
import glob



app = Flask(__name__)
app.secret_key = 'e35f28b67d6eeb7f5fbec49f7258103f'

@app.route('/')
def index():
    folder_path = 'static/plates'
    files = glob.glob(os.path.join(folder_path, '*'))
    # plates = []  # Initialize an empty list
    # detected_plate_filenames = detect_plate('static/uploads/car1.jpg')  # Provide a sample image path for initial display
    # plates.extend(detected_plate_filenames)  # Extend the plates list with detected plate filenames
    return render_template('index.html', plates=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)

        plate_number = detect_plate(file_path)
        flash('Car Number Plate Number: ' + plate_number, 'success')

        return redirect(url_for('index'))
    else:
        flash('No file uploaded.', 'error')
        return redirect(url_for('index'))

def detect_plate(image_path):
    harcascade = "model/haarcascade_russian_plate_number.xml"
    min_area = 500
    count = 0

    img = cv2.imread(image_path)
    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            img_roi = img[y: y+h, x:x+w]
            cv2.imwrite("static/plates/scaned_img_" + str(count) + ".jpg", img_roi)
            count += 1

    return f'Detected {count} plates'



if __name__ == '__main__':
    app.run(debug=True)

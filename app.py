from flask import Flask, jsonify, request
import yolo_v8
import helpers
import custom

app = Flask(__name__)

FOLDER_PATH = "images"

@app.route('/')
def hello():
    image_path = "pothole3.jpg"

    results = yolo_v8.detect_image(FOLDER_PATH + "/" + image_path)
    base64_image_string = custom.detection_result(results["save_dir_path"], image_path) 
    return jsonify({
        "save_dir_path": base64_image_string,
        "total_objects": results["total_objects"],
    })

# create route for post request and the request data contains base64 image
@app.route('/detect', methods=['POST'])
def detect():
    if 'base64_image_string' in request.json and request.json['base64_image_string']:
        # get the base64 image from the request data
        base64_image_string = request.json['base64_image_string']

        # convert the base64 image to jpg
        helpers.base64_to_jpg(base64_image_string, FOLDER_PATH +  "/uploaded_object.jpg")
        
        # detect the image
        results = yolo_v8.detect_image(FOLDER_PATH + "/uploaded_object.jpg")
        base64_result = custom.detection_result(results["save_dir_path"], "uploaded_object.jpg")
        return jsonify({
            "base64_image_string": base64_result,
            "total_objects": results["total_objects"],
        })

    return jsonify({
        "error": "parameter base64_image_string tidak boleh kosong!"
    })


if __name__ == '__main__':
    app.run(debug=True)
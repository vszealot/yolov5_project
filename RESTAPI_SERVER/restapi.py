"""
Run a rest API exposing the yolov5s object detection model
"""
import argparse
import io

import torch
from PIL import Image
from flask import Flask, request
import json
import numpy as np

app = Flask(__name__)

DETECTION_URL = "/rest"

# http://daplus.net/python-numpy-%EB%B0%B0%EC%97%B4%EC%9D%80-json-%EC%A7%81%EB%A0%AC%ED%99%94-%EA%B0%80%EB%8A%A5%ED%95%98%EC%A7%80-%EC%95%8A%EC%8A%B5%EB%8B%88%EB%8B%A4/
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route(DETECTION_URL, methods=["POST"])
def predict():
    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()

        img = Image.open(io.BytesIO(image_bytes))

        results = model(img, size=640)  # reduce size=320 for faster inference
        labels, cord = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy()

        response = {"result" : results.pandas().xyxy[0].to_json(orient="records"), "labels" : labels, "cord" : cord}
        json_dump = json.dumps(response, cls=NumpyEncoder)

        return json_dump

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    # model = torch.hub.load("ultralytics/yolov5", "yolov5s", force_reload=True)  # force_reload to recache
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best_30epoch.pt', force_reload=True)
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat

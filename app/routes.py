from app import app
from flask import request, jsonify, render_template, url_for

from app.services.database import connect_to_db
from app.services.encode import get_encoded_image
#astra_db_store = connect_to_db()

@app.route('/')
@app.route('/index')
def index():
  return "Hello World"


@app.route('/main', methods=['POST'])
def main():
  # expecting a json POST req with fields 'query' (string)
  # data = request.get_json()
  # query = data.get('query')

  # do some stuff with RAG and local CLIP embedding

  image_names = ['frame_150_track_24_class_0.jpg']
  encoded_images = [get_encoded_image(path) for path in image_names]
  video_url = url_for('static', filename='/videos/object_tracking.mp4')
  video_props = {'width': '560', 'height': '420', 'title': 'Video'}
  data = {
    "video": render_template('video.html', video_url=video_url, video_props=video_props),
    "images": encoded_images,
    "text": "this is dummy word data"
    }
  return jsonify(data)

# returns json with array of encoded images witch can be used directly in src field of img tag
# prepend encodeimg string with 'data:image/[image format];base64,[Base64 data]'
@app.route('/video/', methods=['GET'])
@app.route('/video', methods=['GET'])
def video():
  video_url = url_for('static', filename='/videos/object_tracking.mp4')
  video_props = {'width': '560', 'height': '420', 'title': 'Video'}
  return render_template('video.html', video_url=video_url, video_props=video_props)
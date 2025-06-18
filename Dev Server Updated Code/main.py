from flask import Flask, request, jsonify
from audio_processing import process_audio
import json


app = Flask(__name__)

@app.route('/fac-processing', methods=['POST'])
def processing():

    func_params = request.get_json(force=True)
    result = json.loads(process_audio(**func_params))
    try:
        print(result)
    except UnicodeEncodeError:
        pass

    return jsonify({"content":result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8007)



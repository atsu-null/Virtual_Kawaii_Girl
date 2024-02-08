# Flaskを使用した簡単なサーバー例
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/get_expression')
def get_expression():
    file_path = 'Expression.json'
    try:
        # ファイルを読み取り
        with open(file_path, 'r') as file:
            data = json.load(file)
            # 読み取ったデータをJSONとして返す
            return jsonify(data)
    except FileNotFoundError:
        # ファイルが見つからない場合はエラーメッセージを返す
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

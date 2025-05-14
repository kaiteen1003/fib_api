from flask import Flask, request, jsonify
from flask_cors import CORS
from my_package.fibonacci import fibonacci


app = Flask(__name__)


@app.route("/fib", methods=["GET"])
def dispFibo():
    # GETメソッドで取得したnを文字列取得
    n_str = request.args.get("n")

    if n_str is None:  # nがあるか判定
        return (
            jsonify({"status": 400, "message": "'n'の値を指定して下さい"}),
            400,
        )
    elif not n_str.isdigit():  # nが数字のみか判定
        return (
            jsonify(
                {"status": 400, "message": "'n'に数字でないものが含まれています。"}
            ),
            400,
        )
    try:
        n = int(n_str)  # int型に変換
        result = fibonacci(n)
    except ValueError as e:  # Valueerrorのキャッチ
        return (
            jsonify({"status": 400, "message": "0以下の数字は不適切です。"}),
            400,
        )
    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(debug=True)

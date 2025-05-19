from flask import Flask, request, jsonify
from flask_cors import CORS
from responses import RESPONSE_N_MISSING, RESPONSE_N_NOT_DIGIT, RESPONSE_N_NEGATIVE
from my_package.fibonacci import fibonacci


app = Flask(__name__)
CORS(app)


@app.route("/fib", methods=["GET"])
def dispFibo():
    # GETメソッドで取得したnを文字列取得
    n_str = request.args.get("n")

    if not n_str:  # nがあるか判定
        return (
            jsonify(RESPONSE_N_MISSING),
            400,
        )
    elif not n_str.isdigit():  # nが数字のみか判定
        return (
            jsonify(RESPONSE_N_NOT_DIGIT),
            400,
        )
    try:
        n = int(n_str)  # int型に変換
        result = fibonacci(n)

    except ValueError as e:  # Valueerrorのキャッチ
        return (
            jsonify(RESPONSE_N_NEGATIVE),
            400,
        )
    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(debug=True)

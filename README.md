# Fibonacci API with Flask

## 📌 プロジェクト概要

このプロジェクトは、Flask を使って作成された簡単な REST API です。  
指定された数値 `n` に対して、フィボナッチ数列の第 `n` 項の値を返します。

エンドポイント：  
`http://127.0.0.1:5000/fib?n=5`  
→ レスポンス：`{"result": 5}`

---

## 🚀 主な機能

- `n` をクエリパラメータで受け取り、フィボナッチ数列の値を計算
- エラーハンドリング（以下の例を含む）：
  - `n` が存在しない → 'n'の値を指定して下さい
  - `n` に数字以外が含まれる → 'n'に数字でないものが含まれています。
  - `n <= 0` → `0以下の数字は不適切です。`

---

## 📁 ディレクトリ構成
<pre>
fib_flask/
├── main.py # Flask アプリの本体
├── responses.py # 共通のレスポンス定義（エラーメッセージなど）
├── requirements.txt #環境設定用
├── my_package/
│ └── fibonacci.py # フィボナッチ計算ロジック
│ └── __init_.py   # my_packageをパッケージ認識させるためのファイル
├── tests/
│ └── test.py # ユニットテストコード
└── README.md # このファイル
</pre>

---

## ⚙️ 実行方法

### 1. 本体
```bash
python main.py
```
### 2. ユニットテスト
```bash
python -m tests.test
```

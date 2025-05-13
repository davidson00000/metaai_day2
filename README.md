# metaai_day2

このプロジェクトは、LangChain + GPT + DuckDuckGo を使って「検索→要約」するシンプルなエージェントのサンプルです。

## 🔧 セットアップ手順（Windows向け）

### 1. 仮想環境の作成
```bash
python -m venv agi_day2
.agi_day2\Scripts\activate
```

### 2. ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 3. OpenAI APIキーの設定
`main.py` のこの行を自分のAPIキーに書き換えてください：
```python
os.environ["OPENAI_API_KEY"] = "sk-..."
```

### 4. 実行
```bash
python main.py
```

---

## 📂 ファイル構成

| ファイル名 | 説明 |
|------------|------|
| `main.py` | 検索＋要約を行うメインスクリプト |
| `requirements.txt` | 必要なライブラリ一覧 |
| `.gitignore` | Git管理から除外するファイルの指定 |
| `README.md` | このファイル。セットアップ手順 |

---

## 🧠 実行例

```text
AGIとは、人間のように柔軟で汎用的な知能を持つAIのこと。
特定のタスクだけでなく幅広い問題を理解し解決できる。
まだ実現されていないが研究が進んでいる。
```

---

## 📌 注意
- このプロジェクトは教育目的で作成されています。
- OpenAIのAPI料金にご注意ください（無料枠が終わると課金されます）。


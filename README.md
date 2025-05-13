# metaai_day2

LangChain + GPT + DuckDuckGo を使って「検索→要約」するシンプルなエージェント。

## セットアップ手順（Windows向け）

### 1. 仮想環境の作成
```bash
python -m venv agi_day2
.\agi_day2\Scripts\activate
```

### 2. ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 3. .env ファイルを作成してAPIキーを記載
`.env.example` を `.env` にコピーして、OpenAIのAPIキーを書き込みます：

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

### 4. 実行
```bash
python main.py
```

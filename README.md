# metaai_day2 (SerpAPI版)

LangChain + GPT + SerpAPIを使って「Google検索→要約」するシンプルなエージェントです。

## セットアップ手順（Windows）

### 1. 仮想環境の作成と起動
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2. ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 3. .envファイルを作成
`.env.example` を `.env` にコピーし、以下を設定：

```
OPENAI_API_KEY=sk-xxxxxxxxxxxx
SERPAPI_API_KEY=xxxxxxxxxxxxxxxx
```

※ SerpAPIは https://serpapi.com から無料登録でAPIキー取得可能（月100回まで無料）

### 4. 実行
```bash
python main.py
```

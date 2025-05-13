# main.py - SerpAPI with キャッシュ機構つき

from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
import json
import hashlib

# 🔐 環境変数読み込み
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

# 🔎 キャッシュ付き検索関数
def cached_search(query: str) -> str:
    cache_file = "search_cache.json"
    key = hashlib.sha256(query.encode()).hexdigest()

    # キャッシュファイル読み込み
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            cache = json.load(f)
    else:
        cache = {}

    # キャッシュにあれば返す
    if key in cache:
        print(f"[Cache Hit] {query}")
        return cache[key]

    # SerpAPI実行（初回）
    print(f"[Cache Miss] {query} → SerpAPI 実行")
    search = SerpAPIWrapper()
    result = search.run(query)

    # キャッシュ保存
    cache[key] = result
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    return result

# 🛠 ツール定義（キャッシュ付き関数を使う）
tools = [
    Tool(
        name="Google Search (cached)",
        func=cached_search,
        description="検索結果を取得する。結果は自動でキャッシュされ、同じ検索ではAPIを使わない。"
    )
]

# 🤖 エージェント構築
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 🎯 実行
response = agent.run("AGIとは何かを簡単に3行で教えて")
print("\n🧠 Final Answer:\n" + response)

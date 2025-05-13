# metaai_day2 with SerpAPI
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# 🔐 環境変数読み込み
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

# 🔎 SerpAPIツール定義
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Google Search",
        func=search.run,
        description="最新情報を検索するときに使う。"
    )
]

# 🤖 LLM + エージェント設定
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# 🎯 実行
response = agent.run("AGIとは何かを簡単に3行で教えて")
print(response)

# metaai_day2 entry point
# 実行例: agent.run("AGIとは何かを簡単に3行で教えて")

from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# 🔐 .envからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

# 🔎 検索ツールの設定
search = DuckDuckGoSearchAPIWrapper()
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="最新情報を探すときに使う。検索クエリを渡すと情報が返る。"
    )
]

# 🤖 エージェント構築
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# 🎯 実行
response = agent.run("AGIとは何かを簡単に3行で教えて")
print(response)

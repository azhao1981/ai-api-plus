import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.utilities import BingSearchAPIWrapper

if not os.getenv("AZURE_OPENAI_ENDPOINT"):
    raise ValueError("Please set the environment variable AZURE_OPENAI_ENDPOINT")

if not os.getenv("AZURE_OPENAI_API_KEY"):
    raise ValueError("Please set the environment variable AZURE_OPENAI_API_KEY")

if not os.getenv("AZURE_CHAT_DEPLOYMENT"):
    raise ValueError("Please set the environment variable AZURE_CHAT_DEPLOYMENT")

if not os.getenv("BING_SEARCH_URL"):
    raise ValueError("Please set the environment variable AZURE_SEARCH_ENDPOINT")

if not os.getenv("BING_SUBSCRIPTION_KEY"):
    raise ValueError("Please set the environment variable AZURE_SEARCH_KEY")


api_version = os.getenv("OPENAI_API_VERSION", "2024-02-01")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME", "rag-azure-search")


# RAG prompt
template = """Answer the question based only on the following context:
{context}
Question: {question}
"""

_prompt = ChatPromptTemplate.from_template(template)

_model = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_CHAT_DEPLOYMENT"],
    api_version=api_version,
)
from langchain.agents import AgentType

search = BingSearchAPIWrapper(k=1)
def get_context(query):
    return search.run(query)

chain = (
    RunnableParallel({
        "context": lambda x: get_context(x), "question": RunnablePassthrough()
        })
    | _prompt
    | _model
    | StrOutputParser()
)


# Add typing for input
class Question(BaseModel):
    __root__: str


chain = chain.with_types(input_type=Question)

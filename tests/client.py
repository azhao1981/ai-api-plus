from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8100/rag-azure-search")
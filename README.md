# ai-api-plus

## Installation

Install the LangChain CLI if you haven't yet

```bash
uv venv .ai-api-plus -p /home/weiz/.py/python311
. .env
uv pip install -r requirements.txt
```


poetry
https://python-poetry.org/docs/

https://python.langchain.com/v0.2/docs/langserve/

```bash
poetry run langchain serve --port=8100

poetry lock 
poetry install
```

还不行，可以先看看
https://github.com/langchain-ai/langchain/blob/master/docs/docs/integrations/vectorstores/azuresearch.ipynb

## Adding packages

```bash
uv pip install -U langchain-cli

# adding packages from 
# https://github.com/langchain-ai/langchain/tree/master/templates
langchain app add $PROJECT_NAME

# https://github.com/langchain-ai/langchain/tree/master/templates/rag-azure-search
langchain app add rag-azure-search

# adding custom GitHub repo packages
langchain app add --repo $OWNER/$REPO
# or with whole git string (supports other git providers):
# langchain app add git+https://github.com/hwchase17/chain-of-verification

# with a custom api mount point (defaults to `/{package_name}`)
langchain app add $PROJECT_NAME --api_path=/my/custom/path/rag
```

Note: you remove packages by their api path

```bash
langchain app remove my/custom/path/rag
```

## Setup LangSmith (Optional)
LangSmith will help us trace, monitor and debug LangChain applications. 
You can sign up for LangSmith [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

## Launch LangServe

```bash
langchain serve
```

## Running in Docker

This project folder includes a Dockerfile that allows you to easily build and host your LangServe app.

### Building the Image

To build the image, you simply:

```shell
docker build . -t my-langserve-app
```

If you tag your image with something other than `my-langserve-app`,
note it for use in the next step.

### Running the Image Locally

To run the image, you'll need to include any environment variables
necessary for your application.

In the below example, we inject the `OPENAI_API_KEY` environment
variable with the value set in my local environment
(`$OPENAI_API_KEY`)

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8080:8080 my-langserve-app
```

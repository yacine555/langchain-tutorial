import getpass
import os


try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print("Error: The `python-dotenv` package is not installed. Please install it to load environment variables.")
    pass



if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass(prompt="Enter your LangSmith API key (optional): ")

if "LANGSMITH_PROJECT" not in os.environ:
    os.environ["LANGSMITH_PROJECT"] = getpass.getpass(prompt='Enter your LangSmith Project Name (default = "default"): ')
    if not os.environ.get("LANGSMITH_PROJECT"):
        os.environ["LANGSMITH_PROJECT"] = "default"


if not os.environ.get("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter API key for Anthropic: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Translate the following from English into French"),
    HumanMessage("hi!"),
]

model.invoke(messages)

for token in model.stream(messages):
    print(token.content, end="|")
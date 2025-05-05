# LangChain tutorial

## Description

[LangChain](https://python.langchain.com/docs/introduction/)

## Getting Started


### Prerequisites and Dependencies

Before you begin, ensure you have the following installed:
- Python 3.11.8 or later. Note that this was only tested on 3.11.8
- [Langchain](https://python.langchain.com/docs/get_started/introduction)


Here are the PIP module used

- [**python-dotenv (1.1.0)**](https://pypi.org/project/python-dotenv/): Reads key-value pairs from a `.env` file and sets them as environment variables.
- [**langchain (0.3.25)**](https://pypi.org/project/langchain/): Designed for building applications involving language models.



### Installation


Recommend using Install pipenv or other vitual environment tool. 

```bash
pipenv install
pipenv shell
pipenv --version
python --version
```


Clone the repository and install the required packages:

```bash
git clone https://github.com/yacine555/langchain-tutorial.git
cd langchain-tutorial
pipenv install -r requirements.txt
```

### Running the Application

Start the application by running:


```bash
pipenv run python app.py 
```

### Upgrade 

To upgrade a package
```
pip install <package_name> --upgrade
```
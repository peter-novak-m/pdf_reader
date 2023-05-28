# Pdf Reader

This small Python application allows you to load a single PDF and ask questions to it using an LLM. The program is created for ChatGpt but could easily be modified to other models.

## Installation

Start with cloning the repo and creating your own virtual enviroment for running it. Creating an virtual environment is not strictly nessecary but a good practice in general.

```
python -m venv .venv

```

To activate your virtual environment:

```
source .venv/bin/activate

```

Finally install the required packages:

```
pip install -r requirements.txt

```

You will also need to rename the `.env.example` file to `.env` and add your OpenAI API key to it.

## Usage

To use the application, run the `app.py` file with the streamlit CLI (after having installed streamlit):

```
streamlit run app.py

```

## Credits

This reposity has been created based of Alejandro's work. Check his project out here:
https://github.com/alejandro-ao/langchain-ask-pdf

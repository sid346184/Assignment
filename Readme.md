# A simple conversational AI bot


* Uses **SystemMessage, HumanMessage, AIMessage** for structured chat
* Maintains **chat history** so the conversation feels natural
* Frontend with **Streamlit’s chat UI**
* Loads API key from `.env` for security

Assignment/
│
├── app.py        # Streamlit frontend
├── main.py   # Backend chatbot logic
├── requirements.txt

├── Document_each_step.md # I documented each and every step used in making of the chatbot
└── README.md

```
git clone https://github.com/sid346184/Assignment.git
cd Assignment

# Activate Virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

# These are the requirements
langchain
langchain-groq
streamlit
python-dotenv


GROQ_API_KEY=your_groq_api_key_here

Start the server
streamlit run app.py

```

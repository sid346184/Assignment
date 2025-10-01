1. I downloaded the Python3 and activated the virtual environment venv and made main.py for chatbot logic
2. Installed all the requirements required for the project and put them all in requirements.txt
3. Used langchain to make the AI model and Groq for api keys as it is free, I also used streamlit for frontend
4. I first make a small demo ai bot i.e. just connected the api with user query and try to get the response.body, it is working correctly.
5. Now I used AIMessage and HumanMessage feature of langchain to get keep record of user historical chat.
6. I tested it and it is able to get answers from historical chats.
7. Now moving to frontend, I imported the chatbot function from app.py to main.py so that both scripts can be started with only one command rather than defining endpoints, I used Streamlit and made a simple UI in main.py.
8. I tested it with backend, got the error of model, i.e. I was no longer able to use the llama3 model of Groq, so I changed the model to deepseek and configured it to remove its Think feature because it is only a simple AI bot, I also put, max tokens to be 1000 and temperature 0.7.
9. After testing, I put the GROQ_API_KEY in .env to keep it as a secret and then pushed all the remaining files on github.
10. Then I used Render to deploy the project and gave the api secret manually to Render.
11. I made the readme file of the whole project.

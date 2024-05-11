Basic RAG project
==================

Pre-requisites
--------------
- Python 3.8
- OpenAI API key

Project overview
----------------
This project demonstrates how to develop a basic Retrieval Augmented Generation (RAG).
The project uses the OpenAI API to generate the embeddings for the documents and stores them in a local database.
Flow:
- The user asks a question
- The system retrieves the relevant documents that can help to answer the question
- The system generates a prompt that includes the question and the retrieved data as context
- The system sends the prompt to the OpenAI API to generate the answer
- The system returns the answer to the user


How to use
----------
1. Clone the repository
2. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Add your own data to the `data/books` directory
    - Your data should be in markdown (.md) format
    - Add one or more  `*.md` files with your own custom data
    - For example:
    - `data/books/tikal.md`
        ```markdown
       ## Who is Gaby Tal?
         Gaby Tal is a Devops engineer, with a passion for new technologies.
        ```

4. Set the OpenAI API key
    ```bash
    export OPENAI_API_KEY=<your-api-key>
    ```
5. Create the local Vector DB (Chroma in our case), split the data into chunks and store it in the DB
    ```bash
    python3 create_database.py
    ```
   
6. Run the project
    ```bash
    python3 query_data.py "Who is Gaby Tal?" 

   Response:
   Gaby Tal is a Devops engineer at Tikal.
    ```



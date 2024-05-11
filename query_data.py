import argparse
from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

{question}
"""


def get_user_query():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    return query_text


def get_relevant_documents(query_text):
    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=10)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        return

    return results


def prepare_prompt(results, query_text):
    # Prepare the context and question for the model.
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prepared_prompt = prompt_template.format(context=context_text, question=query_text)
    # print(f"Prompt: {prompt}")
    return prepared_prompt


def ask_model(prompt):
    model = ChatOpenAI()
    response = model.invoke(prompt)
    return response


if __name__ == "__main__":
    user_query = get_user_query()
    context = get_relevant_documents(user_query)
    if context:
        full_prompt = prepare_prompt(context, user_query)
        response_text = ask_model(full_prompt)
        print(f"Response: \n {response_text.content}")

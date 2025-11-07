from flask import Flask, render_template, request, jsonify
from llm import generate_response
from langchain.prompts import PromptTemplate

template = """Réponds toujours en français, même si la question est en anglais.
Utilise les informations suivantes pour répondre à la question. 
Si tu ne sais pas, dis que tu ne sais pas.

Contexte : {context}
Question : {question}
Réponse en français :"""

prompt = PromptTemplate(input_variables=["context", "question"], template=template)

app = Flask(__name__, static_folder='static', template_folder='templates')

history = []  # Liste des messages { "question": ..., "answer": ... }

def generate_answer(question):
    # Ici tu peux mettre ton code de génération de réponse
    return str(generate_response(question))

@app.route('/', methods=['GET'])
def ask():
    return render_template('ask.html')

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    question = data.get("question", "").strip()
    if question:
        answer_text = generate_answer(question)
        history.append({ "question": question, "answer": answer_text })
        return jsonify({"question": question, "answer": answer_text, "history": history})
    return jsonify({"error": "Aucune question reçue"}), 400

if __name__ == '__main__':
    app.run(debug=True)

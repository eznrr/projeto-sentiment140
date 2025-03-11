from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

CORS(app, origins=["https://projeto-sentiment140-six.vercel.app"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "modelo_vetor", "modelo.pkl")
vectorizer_path = os.path.join(BASE_DIR, "modelo_vetor", "vetor_tfidf.pkl")

# Carregar o modelo treinado
model = joblib.load(model_path)
# Carregar o vetor TF-IDF
tfidf_vectorizer = joblib.load(vectorizer_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Recebe os dados da request
        print("Recebido:", data)  
        if data and "text" in data:
            text = data["text"]

            # Transformar o texto usando o vetor TF-IDF
            text_tfidf = tfidf_vectorizer.transform([text])

            # Fazer a previsão
            prediction = model.predict(text_tfidf)

            result = "Positive" if prediction[0] == 1 else "Negative"
            
            return jsonify({'prediction': result})

        else:
            return jsonify({'error': 'Texto não fornecido'}), 400

    except Exception as e:
        print("Erro:", str(e)) 
        return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

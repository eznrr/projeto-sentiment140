from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app)

# puxo o modelo já treinado e binzarizado, aqui contem todas as funçõe e parametros do modelo
model = joblib.load(r'C:\Users\ezn52\OneDrive\Área de Trabalho\projeto-sentiment140\API_projeto\modelo_vetor\modelo.pkl')

# puxo o modelo de tfidf já treinado com o meu datasset previo, contendo os pesos atribuidos as palavras
tfidf_vectorizer = joblib.load(r'C:\Users\ezn52\OneDrive\Área de Trabalho\projeto-sentiment140\API_projeto\modelo_vetor\vetor_tfidf.pkl')

# defino o resquest para o caminho /predict, e recebo dados com metodo Post
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() # puxo os dados com minha request
        print("Recebido:", data)  
        if data and "text" in data:
            text = data["text"]

            # Transformar o texto usando o vetor TF-IDF
            text_tfidf = tfidf_vectorizer.transform([text])
            
            # Fazer a previsão
            prediction = model.predict(text_tfidf)
            
            if prediction[0] == 1:
                result = "Positive"
            else: result = "Negative"
            
            return jsonify({'prediction': result})
        
        else:
            return jsonify({'error': 'Texto não fornecido'}), 400
    
    except Exception as e:
        print("Erro:", str(e)) 
        return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
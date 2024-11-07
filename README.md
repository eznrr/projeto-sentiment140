
# API de Classificação de Sentimento

Esta API realiza a classificação de sentimento em um texto fornecido. O sistema recebe um texto em uma requisição POST e retorna uma análise de sentimento correspondente.

## Funcionalidades

- Recebe um texto como entrada
- Retorna a classificação de sentimento do texto enviado

## Estrutura do Projeto

- `api_textos.py`: Contém o código da API para processamento de textos e classificação de sentimentos.
- `index.html`: Frontend para interação com a API, permitindo que o usuário insira um texto e visualize o resultado da análise de sentimento.

## Tecnologias Utilizadas

- **Backend**: Python com Flask para a criação da API.
- **Frontend**: HTML, CSS e JavaScript para a interface do usuário.

## Endpoints

### `POST /predict`

Recebe um texto JSON e retorna o sentimento correspondente.

#### Exemplo de Requisição

```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "seu texto aqui"}'
```

#### Exemplo de Resposta

```json
{
  "prediction": "Positivo"
}
```

## Como Executar

1. **Instale as dependências** listadas no arquivo `requirements.txt`.
2. **Execute a API** com o seguinte comando:

   ```bash
   python api_textos.py
   ```

3. **Acesse o Frontend**: Abra o arquivo `index.html` em um navegador e insira o texto desejado para análise.

## Observação

Certifique-se de que o servidor Flask está rodando no endereço `http://localhost:5000` para que a interface web funcione corretamente.

## Possíveis Melhorias

- Implementar classificações de sentimento mais detalhadas.
- Adicionar suporte a múltiplos idiomas para a análise de sentimento.

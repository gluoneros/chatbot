import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    # Lógica simple: buscar palabras clave
    if any(word in tokens for word in ['hola', 'hi']):
        return "¡Hola! ¿En qué puedo ayudarte?"
    elif any(word in tokens for word in ['adios', 'bye']):
        return "¡Adiós! Hasta pronto."
    else:
        return "No entiendo, ¿puedes repetir?"

# Opcional: Usar transformers para respuestas más avanzadas
from transformers import pipeline
def get_advanced_response(user_input):
    generator = pipeline('text-generation', model='gpt2')
    response = generator(user_input, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
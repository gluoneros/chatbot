import nltk
import spacy
from nltk.tokenize import word_tokenize

nlp = spacy.load("es_core_news_sm")
#nltk.download('punkt')

# Diccionario de respuestas para el colegio
COLLEGE_RESPONSES = {
    "horarios": "El colegio opera de 7:30 a.m. a 2:30 p.m. para primaria y de 7:30 a.m. a 3:00 p.m. para secundaria. ¿Necesitas el calendario escolar?",
    "inscripción": "Para inscribir a tu hijo/a, debes completar el formulario en nuestra web, presentar el certificado de nacimiento y el último boletín. Contáctanos en admisiones@colegio.com para más detalles.",
    "extracurriculares": "Ofrecemos fútbol, baloncesto, robótica, arte y música. Las actividades son de 3:00 p.m. a 4:30 p.m. ¿Quieres información sobre alguna en particular?",
    "profesor": "Para contactar a un profesor, envía un correo a coordinacion@colegio.com con el nombre del profesor y el curso. También puedes agendar una cita en la secretaría.",
    "matrícula": "Los costos de matrícula varían según el grado. Por favor, contacta a admisiones@colegio.com para una cotización detallada."
}


def get_response(user_input):
    # Procesar la entrada con spacy
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]
    print(f"Tokens: {tokens}")  # Depuración

    # Identificar intenciones basadas en palabras clave
    if any(word in tokens for word in ['hola', 'hi', 'hello']):
        return "¡Hola! Bienvenido/a al servicio de atención al cliente del colegio. ¿En qué puedo ayudarte?"
    elif any(word in tokens for word in ['adios', 'bye']):
        return "¡Adiós! Gracias por contactarnos."
    elif any(word in tokens for word in ['horario', 'horarios', 'hora', 'horas']):
        return COLLEGE_RESPONSES["horarios"]
    elif any(word in tokens for word in ['inscripción', 'inscribir', 'admisiones', 'admisión']):
        return COLLEGE_RESPONSES["inscripción"]
    elif any(word in tokens for word in ['extracurriculares', 'actividades', 'deportes', 'clubes']):
        return COLLEGE_RESPONSES["extracurriculares"]
    elif any(word in tokens for word in ['profesor', 'maestro', 'docente', 'contactar']):
        return COLLEGE_RESPONSES["profesor"]
    elif any(word in tokens for word in ['matrícula', 'costos', 'pago', 'cuota']):
        return COLLEGE_RESPONSES["matrícula"]
    else:
        # Usar spacy para análisis semántico (opcional)
        for ent in doc.ents:
            if ent.label_ in ["ORG", "LOC", "DATE"]:  # Ejemplo: detectar nombres o fechas
                return "Parece que mencionaste algo específico. ¿Puedes dar más detalles? Por ejemplo, pregunta sobre horarios o inscripciones."
        return "Lo siento, no entendí tu pregunta. ¿Puedes reformularla? Por ejemplo, pregunta sobre horarios, inscripciones o actividades extracurriculares."
import google.generativeai as genai
import json
import logging
from django.conf import settings

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

logger = logging.getLogger(__name__)

def generate_cricket_questions(category, difficulty, count=5):
    """
    Generates cricket questions using the Gemini API based on category and difficulty.
    """
    prompt = f"""
    Generate {count} multiple-choice questions about Cricket.
    Category: {category}
    Difficulty: {difficulty}
    
    Each question must be unique and have 4 options (A, B, C, D).
    Format the output as a JSON list of objects:
    [
        {{
            "text": "Question text here?",
            "option_a": "Option A text",
            "option_b": "Option B text",
            "option_c": "Option C text",
            "option_d": "Option D text",
            "correct_answer": "A" (Must be A, B, C, or D)
        }}
    ]
    Only return the JSON and nothing else.
    """
    
    try:
        response = model.generate_content(prompt)
        # Clean the response to ensure it's valid JSON
        text = response.text.replace('```json', '').replace('```', '').strip()
        questions_data = json.loads(text)
        return questions_data
    except Exception as e:
        logger.error(f"Error generating questions with Gemini: {e}")
        return []

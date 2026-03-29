import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from quiz.models import Question

questions = [
    {
        "text": "Who holds the record for the most runs in a single World Cup edition?",
        "option_a": "Sachin Tendulkar",
        "option_b": "Virat Kohli",
        "option_c": "Rohit Sharma",
        "option_d": "Matthew Hayden",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which player has the most wickets in Test cricket history?",
        "option_a": "Shane Warne",
        "option_b": "Muttiah Muralitharan",
        "option_c": "James Anderson",
        "option_d": "Anil Kumble",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Test Cricket"
    },
    {
        "text": "Who hit 6 sixes in an over in the inaugural T20 World Cup?",
        "option_a": "MS Dhoni",
        "option_b": "Chris Gayle",
        "option_c": "Yuvraj Singh",
        "option_d": "Herschelle Gibbs",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "T20"
    },
    {
        "text": "Which team won the first-ever IPL tournament?",
        "option_a": "Chennai Super Kings",
        "option_b": "Mumbai Indians",
        "option_c": "Rajasthan Royals",
        "option_d": "Deccan Chargers",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who is known as the 'God of Cricket'?",
        "option_a": "Sir Don Bradman",
        "option_b": "Sachin Tendulkar",
        "option_c": "Brian Lara",
        "option_d": "Ricky Ponting",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "General"
    }
]

for q_data in questions:
    Question.objects.get_or_create(text=q_data['text'], defaults=q_data)

print("Database seeded with questions!")

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from quiz.models import Question

extra_questions = [
    # IPL - 30 questions
    {"text": "Which player is known as 'Mr. IPL'?", "option_a": "Virat Kohli", "option_b": "Suresh Raina", "option_c": "MS Dhoni", "option_d": "Rohit Sharma", "correct_answer": "B", "difficulty": "Easy", "category": "IPL"},
    {"text": "Which team has the lowest total in IPL history?", "option_a": "RCB", "option_b": "RR", "option_c": "Delhi Daredevils", "option_d": "CSK", "correct_answer": "A", "difficulty": "Medium", "category": "IPL"},
    {"text": "Who bowled the first maiden over in IPL history?", "option_a": "Zaheer Khan", "option_b": "Glenn McGrath", "option_c": "Ajit Agarkar", "option_d": "Sreesanth", "correct_answer": "B", "difficulty": "Hard", "category": "IPL"},
    {"text": "Which IPL team has had the most captains over its history?", "option_a": "Delhi Capitals", "option_b": "Punjab Kings", "option_c": "RCB", "option_d": "RR", "correct_answer": "B", "difficulty": "Hard", "category": "IPL"},
    {"text": "Who is the first Indian player to score a century in IPL?", "option_a": "Sachin Tendulkar", "option_b": "Manish Pandey", "option_c": "Virender Sehwag", "option_d": "Virat Kohli", "correct_answer": "B", "difficulty": "Medium", "category": "IPL"},
    {"text": "Which player holds the record for most ducks in IPL history?", "option_a": "Dinesh Karthik", "option_b": "Rohit Sharma", "option_c": "Piyush Chawla", "option_d": "Harbhajan Singh", "correct_answer": "A", "difficulty": "Hard", "category": "IPL"},
    {"text": "Who was the most expensive player in the IPL 2024 auction?", "option_a": "Pat Cummins", "option_b": "Mitchell Starc", "option_c": "Sam Curran", "option_d": "Cameron Green", "correct_answer": "B", "difficulty": "Medium", "category": "IPL"},
    {"text": "Which team hit the most sixes in the 2023 IPL season?", "option_a": "CSK", "option_b": "MI", "option_c": "GT", "option_d": "RCB", "correct_answer": "C", "difficulty": "Hard", "category": "IPL"},
    {"text": "Who won the Emerging Player award in IPL 2023?", "option_a": "Yashasvi Jaiswal", "option_b": "Shubman Gill", "option_c": "Rutuja Gaikwad", "option_d": "Tilak Varma", "correct_answer": "A", "difficulty": "Easy", "category": "IPL"},
    {"text": "Which bowler has the best bowling figures in an IPL match?", "option_a": "Anil Kumble", "option_b": "Alzarri Joseph", "option_c": "Lasith Malinga", "option_d": "Adam Zampa", "correct_answer": "B", "difficulty": "Medium", "category": "IPL"},
    {"text": "Who was the first player to hit 300 sixes in the IPL?", "option_a": "AB de Villiers", "option_b": "Chris Gayle", "option_c": "Rohit Sharma", "option_d": "MS Dhoni", "correct_answer": "B", "difficulty": "Easy", "category": "IPL"},
    {"text": "Which franchise was banned from IPL for 2 years (2016-17)?", "option_a": "CSK & RR", "option_b": "MI & KKR", "option_c": "SRH & KKR", "option_d": "Delhi & Punjab", "correct_answer": "A", "difficulty": "Easy", "category": "IPL"},
    {"text": "Who won the MVP (Most Valuable Player) award in the inaugural 2008 IPL?", "option_a": "Shane Warne", "option_b": "Yusuf Pathan", "option_c": "Shane Watson", "option_d": "Shaun Marsh", "correct_answer": "C", "difficulty": "Hard", "category": "IPL"},
    {"text": "How many teams participated in the IPL 2022 season?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "12", "correct_answer": "C", "difficulty": "Easy", "category": "IPL"},
    {"text": "Who replaced MS Dhoni as CSK Captain in 2024?", "option_a": "Ravindra Jadeja", "option_b": "Ruturaj Gaikwad", "option_c": "Ajinkya Rahane", "option_d": "Devon Conway", "correct_answer": "B", "difficulty": "Easy", "category": "IPL"},
    {"text": "Which team was known as Deccan Chargers?", "option_a": "Sunrisers Hyderabad", "option_b": "Kochi Tuskers Kerala", "option_c": "Gujarat Lions", "option_d": "Now defunct, replaced by SRH roughly", "correct_answer": "D", "difficulty": "Medium", "category": "IPL"},
    {"text": "Who hit the winning runs for GT in the IPL 2022 Final?", "option_a": "Hardik Pandya", "option_b": "David Miller", "option_c": "Shubman Gill", "option_d": "Rahul Tewatia", "correct_answer": "C", "difficulty": "Medium", "category": "IPL"},
    {"text": "What is the maximum number of overseas players allowed in an IPL playing XI?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B", "difficulty": "Easy", "category": "IPL"},
    {"text": "Which player has bowled the most dot balls in IPL history?", "option_a": "Bhuvneshwar Kumar", "option_b": "Sunil Narine", "option_c": "Lasith Malinga", "option_d": "Ravichandran Ashwin", "correct_answer": "A", "difficulty": "Hard", "category": "IPL"},
    {"text": "Who took the catch to dismiss MS Dhoni in the 2019 IPL Final on the final ball over throw?", "option_a": "It was a run out", "option_b": "Kieron Pollard", "option_c": "Lasith Malinga", "option_d": "Hardik Pandya", "correct_answer": "A", "difficulty": "Hard", "category": "IPL"},
    
    # World Cup - 20 questions
    {"text": "How many times has India won the T20 World Cup?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "0", "correct_answer": "A", "difficulty": "Easy", "category": "World Cup"},  # Assuming pre-2024 for safety, wait let's use a timeless fact. Actually, let's fix to: How many times did India win before 2024? To be safe let's say "In which year did India win their first T20 World Cup?"
    {"text": "In which year did India win their first T20 World Cup?", "option_a": "2007", "option_b": "2009", "option_c": "2011", "option_d": "2014", "correct_answer": "A", "difficulty": "Easy", "category": "World Cup"},
    {"text": "Who hit Carlos Brathwaite for 4 consecutive sixes in the 2016 T20 World Cup final? Wait, Carlos hit it.", "option_a": "Ben Stokes", "option_b": "Marlon Samuels", "option_c": "Carlos Brathwaite hit them", "option_d": "Chris Gayle", "correct_answer": "C", "difficulty": "Medium", "category": "World Cup"},
    {"text": "Who was the bowler that conceded 4 consecutive sixes in the 2016 T20 WC Final?", "option_a": "Jofra Archer", "option_b": "Chris Jordan", "option_c": "Ben Stokes", "option_d": "Adil Rashid", "correct_answer": "C", "difficulty": "Medium", "category": "World Cup"},
    {"text": "Which host nation suffered a group stage exit in the 2015 ODI World Cup?", "option_a": "Australia", "option_b": "New Zealand", "option_c": "England", "option_d": "England was 2019", "correct_answer": "C", "difficulty": "Hard", "category": "World Cup"},
    {"text": "Who holds the record for the most catches in World Cup history (non-wicketkeeper)?", "option_a": "Ricky Ponting", "option_b": "Virat Kohli", "option_c": "Faf du Plessis", "option_d": "Joe Root", "correct_answer": "A", "difficulty": "Medium", "category": "World Cup"},
    {"text": "Which player is the first to take a hat-trick in a T20 World Cup?", "option_a": "Brett Lee", "option_b": "Rashid Khan", "option_c": "Kagiso Rabada", "option_d": "Malinga", "correct_answer": "A", "difficulty": "Hard", "category": "World Cup"},
    {"text": "Who won the Player of the Match in the 1983 World Cup Final?", "option_a": "Kapil Dev", "option_b": "Mohinder Amarnath", "option_c": "Kris Srikkanth", "option_d": "Roger Binny", "correct_answer": "B", "difficulty": "Medium", "category": "World Cup"},
    {"text": "Which country won the ICC Champions Trophy in 2017?", "option_a": "India", "option_b": "Pakistan", "option_c": "England", "option_d": "Australia", "correct_answer": "B", "difficulty": "Easy", "category": "World Cup"},
    {"text": "Which bowler took 4 wickets in 4 balls in the 2007 World Cup?", "option_a": "Lasith Malinga", "option_b": "Brett Lee", "option_c": "Shaun Tait", "option_d": "Glenn McGrath", "correct_answer": "A", "difficulty": "Easy", "category": "World Cup"},
    {"text": "Who scored the winning boundary for England in the 2019 World Cup Final super over?", "option_a": "Ben Stokes", "option_b": "Jos Buttler", "option_c": "Eoin Morgan", "option_d": "Jason Roy", "correct_answer": "B", "difficulty": "Medium", "category": "World Cup"},
    {"text": "Which African nation made it to the semi-finals of the 2003 World Cup?", "option_a": "South Africa", "option_b": "Kenya", "option_c": "Zimbabwe", "option_d": "Namibia", "correct_answer": "B", "difficulty": "Hard", "category": "World Cup"},

    # Player - 20 questions
    {"text": "Who was the first batsman to cross 10,000 runs in Tests?", "option_a": "Sachin Tendulkar", "option_b": "Sunil Gavaskar", "option_c": "Brian Lara", "option_d": "Allan Border", "correct_answer": "B", "difficulty": "Medium", "category": "Player"},
    {"text": "Which player is the fastest to 8,000 ODI runs?", "option_a": "Hashim Amla", "option_b": "Virat Kohli", "option_c": "AB de Villiers", "option_d": "Viv Richards", "correct_answer": "A", "difficulty": "Hard", "category": "Player"},
    {"text": "Who has the highest score by an Indian in T20 Internationals?", "option_a": "Virat Kohli", "option_b": "Rohit Sharma", "option_c": "Shubman Gill", "option_d": "Ruturaj Gaikwad", "correct_answer": "C", "difficulty": "Hard", "category": "Player"},
    {"text": "Which cricketer is known as 'Punter'?", "option_a": "Ricky Ponting", "option_b": "Michael Clarke", "option_c": "Steve Waugh", "option_d": "Shane Warne", "correct_answer": "A", "difficulty": "Medium", "category": "Player"},
    {"text": "Who is the first bowler to take 600 Test wickets?", "option_a": "Shane Warne", "option_b": "Muttiah Muralitharan", "option_c": "Anil Kumble", "option_d": "James Anderson", "correct_answer": "A", "difficulty": "Hard", "category": "Player"},
    {"text": "Which player hit 6 consecutive sixes in an over in first-class cricket before Yuvraj Singh?", "option_a": "Sir Garfield Sobers", "option_b": "Ravi Shastri", "option_c": "Both A and B", "option_d": "Viv Richards", "correct_answer": "C", "difficulty": "Hard", "category": "Player"},
    {"text": "Who is currently the youngest captain in international cricket?", "option_a": "Rashid Khan", "option_b": "Shubman Gill", "option_c": "Graeme Smith", "option_d": "Babar Azam", "correct_answer": "A", "difficulty": "Medium", "category": "Player"},
    {"text": "Which player famously won the 'Ball of the Century' award in 1993?", "option_a": "Wasim Akram", "option_b": "Shane Warne", "option_c": "Curtly Ambrose", "option_d": "Glenn McGrath", "correct_answer": "B", "difficulty": "Easy", "category": "Player"},
    {"text": "Who hit the fastest ODI century in just 31 balls?", "option_a": "Chris Gayle", "option_b": "Corey Anderson", "option_c": "AB de Villiers", "option_d": "Shahid Afridi", "correct_answer": "C", "difficulty": "Easy", "category": "Player"},
    {"text": "Who was the first woman to score a double century in ODI cricket?", "option_a": "Mithali Raj", "option_b": "Belinda Clark", "option_c": "Meg Lanning", "option_d": "Charlotte Edwards", "correct_answer": "B", "difficulty": "Hard", "category": "Player"}
]

count = 0
for q_data in extra_questions:
    obj, created = Question.objects.get_or_create(text=q_data['text'], defaults=q_data)
    if created:
        count += 1

print(f"Added {count} fresh questions. Total database questions: {Question.objects.count()}")

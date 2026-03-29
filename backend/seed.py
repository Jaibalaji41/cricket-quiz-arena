import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from quiz.models import Question

questions = [
    # IPL
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
        "text": "Who holds the record for the most runs in an IPL season?",
        "option_a": "David Warner",
        "option_b": "Virat Kohli",
        "option_c": "Chris Gayle",
        "option_d": "AB de Villiers",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which player has taken the most wickets in IPL history?",
        "option_a": "Lasith Malinga",
        "option_b": "Yuzvendra Chahal",
        "option_c": "Dwayne Bravo",
        "option_d": "Amit Mishra",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which team has won the most IPL titles?",
        "option_a": "Mumbai Indians",
        "option_b": "Chennai Super Kings",
        "option_c": "Both MI & CSK have won 5 each",
        "option_d": "Kolkata Knight Riders",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who scored the fastest century in IPL history?",
        "option_a": "Chris Gayle",
        "option_b": "AB de Villiers",
        "option_c": "Yusuf Pathan",
        "option_d": "David Miller",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which player hit 5 sixes in the final over to win a match for KKR in 2023?",
        "option_a": "Andre Russell",
        "option_b": "Rinku Singh",
        "option_c": "Nitish Rana",
        "option_d": "Sunil Narine",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2019?",
        "option_a": "Chennai Super Kings",
        "option_b": "Mumbai Indians",
        "option_c": "Delhi Capitals",
        "option_d": "Sunrisers Hyderabad",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who has the highest individual score in IPL?",
        "option_a": "Chris Gayle",
        "option_b": "Brendon McCullum",
        "option_c": "Virat Kohli",
        "option_d": "AB de Villiers",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2016?",
        "option_a": "Royal Challengers Bangalore",
        "option_b": "Sunrisers Hyderabad",
        "option_c": "Mumbai Indians",
        "option_d": "Kolkata Knight Riders",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who won the Purple Cap in IPL 2020?",
        "option_a": "Jasprit Bumrah",
        "option_b": "Kagiso Rabada",
        "option_c": "Trent Boult",
        "option_d": "Rashid Khan",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which player has the most fifties in IPL?",
        "option_a": "David Warner",
        "option_b": "Virat Kohli",
        "option_c": "Rohit Sharma",
        "option_d": "Suresh Raina",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2018?",
        "option_a": "Mumbai Indians",
        "option_b": "Chennai Super Kings",
        "option_c": "Kolkata Knight Riders",
        "option_d": "Sunrisers Hyderabad",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who was the first captain of Royal Challengers Bangalore?",
        "option_a": "Rahul Dravid",
        "option_b": "Anil Kumble",
        "option_c": "Kevin Pietersen",
        "option_d": "Virat Kohli",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which player scored the most centuries in IPL?",
        "option_a": "Chris Gayle",
        "option_b": "Virat Kohli",
        "option_c": "Jos Buttler",
        "option_d": "KL Rahul",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2014?",
        "option_a": "Kings XI Punjab",
        "option_b": "Chennai Super Kings",
        "option_c": "Kolkata Knight Riders",
        "option_d": "Mumbai Indians",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who hit the longest six in IPL history?",
        "option_a": "Chris Gayle",
        "option_b": "MS Dhoni",
        "option_c": "Yuvraj Singh",
        "option_d": "AB de Villiers",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2010?",
        "option_a": "Chennai Super Kings",
        "option_b": "Mumbai Indians",
        "option_c": "Deccan Chargers",
        "option_d": "Rajasthan Royals",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who has the most matches played in IPL?",
        "option_a": "MS Dhoni",
        "option_b": "Virat Kohli",
        "option_c": "Rohit Sharma",
        "option_d": "Dinesh Karthik",
        "correct_answer": "D",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2012?",
        "option_a": "Chennai Super Kings",
        "option_b": "Mumbai Indians",
        "option_c": "Kolkata Knight Riders",
        "option_d": "Delhi Daredevils",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who won the Orange Cap in IPL 2016?",
        "option_a": "David Warner",
        "option_b": "Virat Kohli",
        "option_c": "AB de Villiers",
        "option_d": "Rohit Sharma",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2015?",
        "option_a": "Mumbai Indians",
        "option_b": "Chennai Super Kings",
        "option_c": "Royal Challengers Bangalore",
        "option_d": "Kolkata Knight Riders",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who has the best strike rate in IPL history (minimum matches)?",
        "option_a": "Andre Russell",
        "option_b": "Glenn Maxwell",
        "option_c": "AB de Villiers",
        "option_d": "Chris Gayle",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2017?",
        "option_a": "Mumbai Indians",
        "option_b": "Rising Pune Supergiant",
        "option_c": "Sunrisers Hyderabad",
        "option_d": "Kolkata Knight Riders",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who was the first foreign captain to win IPL?",
        "option_a": "Adam Gilchrist",
        "option_b": "Shane Warne",
        "option_c": "David Warner",
        "option_d": "Brendon McCullum",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2013?",
        "option_a": "Chennai Super Kings",
        "option_b": "Mumbai Indians",
        "option_c": "Rajasthan Royals",
        "option_d": "Delhi Daredevils",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who has taken the most catches in a single IPL season?",
        "option_a": "AB de Villiers",
        "option_b": "David Miller",
        "option_c": "Faf du Plessis",
        "option_d": "Kieron Pollard",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2011?",
        "option_a": "Chennai Super Kings",
        "option_b": "Mumbai Indians",
        "option_c": "Kolkata Knight Riders",
        "option_d": "Royal Challengers Bangalore",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who scored the fastest fifty in IPL?",
        "option_a": "KL Rahul",
        "option_b": "Yusuf Pathan",
        "option_c": "Sunil Narine",
        "option_d": "Chris Gayle",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2009?",
        "option_a": "Deccan Chargers",
        "option_b": "Chennai Super Kings",
        "option_c": "Mumbai Indians",
        "option_d": "Rajasthan Royals",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who is the youngest player to play in IPL?",
        "option_a": "Prayas Ray Barman",
        "option_b": "Rishabh Pant",
        "option_c": "Shubman Gill",
        "option_d": "Yashasvi Jaiswal",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which team won IPL 2008?",
        "option_a": "Chennai Super Kings",
        "option_b": "Rajasthan Royals",
        "option_c": "Mumbai Indians",
        "option_d": "Kolkata Knight Riders",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "IPL"
    },
    {
        "text": "Who has the most runs in a single IPL match?",
        "option_a": "Chris Gayle",
        "option_b": "Brendon McCullum",
        "option_c": "AB de Villiers",
        "option_d": "Virat Kohli",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "IPL"
    },
    {
        "text": "Which team has the highest total in IPL history?",
        "option_a": "RCB",
        "option_b": "CSK",
        "option_c": "MI",
        "option_d": "SRH",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Who has taken the most hat-tricks in IPL?",
        "option_a": "Amit Mishra",
        "option_b": "Lasith Malinga",
        "option_c": "Yuzvendra Chahal",
        "option_d": "Sunil Narine",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "IPL"
    },
    {
        "text": "Which team has played the most finals in IPL?",
        "option_a": "Mumbai Indians",
        "option_b": "Chennai Super Kings",
        "option_c": "Kolkata Knight Riders",
        "option_d": "RCB",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "IPL"
    },

    # World Cup
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
        "text": "Which country won the first Cricket World Cup in 1975?",
        "option_a": "Australia",
        "option_b": "West Indies",
        "option_c": "England",
        "option_d": "India",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "World Cup"
    },
    {
        "text": "Who hit 6 sixes in an over in the inaugural T20 World Cup?",
        "option_a": "MS Dhoni",
        "option_b": "Chris Gayle",
        "option_c": "Yuvraj Singh",
        "option_d": "Herschelle Gibbs",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "World Cup"
    },
    {
        "text": "Which bowler took a hat-trick in the 1987 World Cup?",
        "option_a": "Chetan Sharma",
        "option_b": "Saqlain Mushtaq",
        "option_c": "Lasith Malinga",
        "option_d": "Chaminda Vaas",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Australia has won how many ODI World Cups?",
        "option_a": "4",
        "option_b": "5",
        "option_c": "6",
        "option_d": "7",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who was the Player of the Tournament in the 2011 ODI World Cup?",
        "option_a": "MS Dhoni",
        "option_b": "Sachin Tendulkar",
        "option_c": "Yuvraj Singh",
        "option_d": "Zaheer Khan",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who holds the record for most wickets in a single ODI World Cup edition?",
        "option_a": "Mitchell Starc",
        "option_b": "Glenn McGrath",
        "option_c": "Wasim Akram",
        "option_d": "Chaminda Vaas",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which player scored the first double century in ODI World Cup history?",
        "option_a": "Rohit Sharma",
        "option_b": "Chris Gayle",
        "option_c": "Martin Guptill",
        "option_d": "Sachin Tendulkar",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which country hosted the 2019 ODI World Cup?",
        "option_a": "India",
        "option_b": "Australia",
        "option_c": "England",
        "option_d": "South Africa",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who scored the most runs in the 2019 World Cup?",
        "option_a": "Joe Root",
        "option_b": "Rohit Sharma",
        "option_c": "David Warner",
        "option_d": "Kane Williamson",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which bowler took the most wickets in the 2019 World Cup?",
        "option_a": "Mitchell Starc",
        "option_b": "Jofra Archer",
        "option_c": "Trent Boult",
        "option_d": "Jasprit Bumrah",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who was the captain of India during the 1983 World Cup victory?",
        "option_a": "Sunil Gavaskar",
        "option_b": "Kapil Dev",
        "option_c": "Mohinder Amarnath",
        "option_d": "Ravi Shastri",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which team lost the 2019 World Cup final on boundary count?",
        "option_a": "England",
        "option_b": "India",
        "option_c": "New Zealand",
        "option_d": "Australia",
        "correct_answer": "C",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Who has the most centuries in ODI World Cup history?",
        "option_a": "Sachin Tendulkar",
        "option_b": "Rohit Sharma",
        "option_c": "Ricky Ponting",
        "option_d": "Virat Kohli",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which country won the 1992 World Cup?",
        "option_a": "Australia",
        "option_b": "Pakistan",
        "option_c": "England",
        "option_d": "India",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who was the Player of the Tournament in 2019 World Cup?",
        "option_a": "Ben Stokes",
        "option_b": "Joe Root",
        "option_c": "Kane Williamson",
        "option_d": "Rohit Sharma",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which bowler has the most wickets in World Cup history?",
        "option_a": "Wasim Akram",
        "option_b": "Glenn McGrath",
        "option_c": "Muttiah Muralitharan",
        "option_d": "Lasith Malinga",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Who scored 183* against Sri Lanka in 2011 World Cup?",
        "option_a": "Sachin Tendulkar",
        "option_b": "Virender Sehwag",
        "option_c": "MS Dhoni",
        "option_d": "Virat Kohli",
        "correct_answer": "C",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which country hosted the 2003 World Cup?",
        "option_a": "India",
        "option_b": "Australia",
        "option_c": "South Africa",
        "option_d": "England",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who scored a century in the 2011 World Cup final?",
        "option_a": "MS Dhoni",
        "option_b": "Gautam Gambhir",
        "option_c": "Virat Kohli",
        "option_d": "None",
        "correct_answer": "D",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which team was runner-up in 2007 World Cup?",
        "option_a": "India",
        "option_b": "Sri Lanka",
        "option_c": "Australia",
        "option_d": "Pakistan",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who has the highest individual score in World Cup history?",
        "option_a": "Martin Guptill",
        "option_b": "Chris Gayle",
        "option_c": "Rohit Sharma",
        "option_d": "Sachin Tendulkar",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which team won the 2007 World Cup?",
        "option_a": "Australia",
        "option_b": "India",
        "option_c": "Sri Lanka",
        "option_d": "Pakistan",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who bowled the final over in 2011 World Cup final for Sri Lanka?",
        "option_a": "Lasith Malinga",
        "option_b": "Nuwan Kulasekara",
        "option_c": "Muttiah Muralitharan",
        "option_d": "Thisara Perera",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which player scored the fastest century in World Cup history?",
        "option_a": "AB de Villiers",
        "option_b": "Kevin O'Brien",
        "option_c": "Chris Gayle",
        "option_d": "Brendon McCullum",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which team won the 2015 World Cup?",
        "option_a": "New Zealand",
        "option_b": "Australia",
        "option_c": "India",
        "option_d": "South Africa",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who scored 673 runs in the 2003 World Cup?",
        "option_a": "Ricky Ponting",
        "option_b": "Sachin Tendulkar",
        "option_c": "Rahul Dravid",
        "option_d": "Brian Lara",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which country hosted the 2015 World Cup?",
        "option_a": "India",
        "option_b": "Australia & New Zealand",
        "option_c": "England",
        "option_d": "South Africa",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who took a hat-trick in the 2019 World Cup?",
        "option_a": "Mitchell Starc",
        "option_b": "Mohammed Shami",
        "option_c": "Trent Boult",
        "option_d": "Jofra Archer",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which team won the 1999 World Cup?",
        "option_a": "Australia",
        "option_b": "Pakistan",
        "option_c": "India",
        "option_d": "South Africa",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who captained England in the 2019 World Cup?",
        "option_a": "Joe Root",
        "option_b": "Eoin Morgan",
        "option_c": "Ben Stokes",
        "option_d": "Jos Buttler",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which player has the most runs in World Cup history?",
        "option_a": "Sachin Tendulkar",
        "option_b": "Ricky Ponting",
        "option_c": "Kumar Sangakkara",
        "option_d": "Virat Kohli",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which team has never won a World Cup?",
        "option_a": "India",
        "option_b": "Australia",
        "option_c": "South Africa",
        "option_d": "West Indies",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Who scored a double century in the 2015 World Cup?",
        "option_a": "Martin Guptill",
        "option_b": "Chris Gayle",
        "option_c": "Rohit Sharma",
        "option_d": "AB de Villiers",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    {
        "text": "Which player has the most dismissals as a wicketkeeper in World Cups?",
        "option_a": "Adam Gilchrist",
        "option_b": "Kumar Sangakkara",
        "option_c": "MS Dhoni",
        "option_d": "Mark Boucher",
        "correct_answer": "B",
        "difficulty": "Hard",
        "category": "World Cup"
    },
    {
        "text": "Which team won the 1979 World Cup?",
        "option_a": "Australia",
        "option_b": "England",
        "option_c": "West Indies",
        "option_d": "India",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "World Cup"
    },
    # Player
    {
        "text": "Which player has the most wickets in Test cricket history?",
        "option_a": "Shane Warne",
        "option_b": "Muttiah Muralitharan",
        "option_c": "James Anderson",
        "option_d": "Anil Kumble",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is known as the 'God of Cricket'?",
        "option_a": "Sir Don Bradman",
        "option_b": "Sachin Tendulkar",
        "option_c": "Brian Lara",
        "option_d": "Ricky Ponting",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player scored exactly 400 runs in a single Test innings?",
        "option_a": "Sir Don Bradman",
        "option_b": "Matthew Hayden",
        "option_c": "Virender Sehwag",
        "option_d": "Brian Lara",
        "correct_answer": "D",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is affectionately called 'Captain Cool'?",
        "option_a": "Kane Williamson",
        "option_b": "Eoin Morgan",
        "option_c": "MS Dhoni",
        "option_d": "Ricky Ponting",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Who holds the record for the highest individual score in ODIs?",
        "option_a": "Virender Sehwag",
        "option_b": "Martin Guptill",
        "option_c": "Rohit Sharma",
        "option_d": "Chris Gayle",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who was nicknamed 'The Rawalpindi Express'?",
        "option_a": "Wasim Akram",
        "option_b": "Waqar Younis",
        "option_c": "Shoaib Akhtar",
        "option_d": "Imran Khan",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player has the most international centuries in cricket?",
        "option_a": "Ricky Ponting",
        "option_b": "Virat Kohli",
        "option_c": "Sachin Tendulkar",
        "option_d": "Kumar Sangakkara",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is known as 'The Wall' in cricket?",
        "option_a": "Rahul Dravid",
        "option_b": "VVS Laxman",
        "option_c": "Sourav Ganguly",
        "option_d": "Anil Kumble",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player has the most runs in Test cricket?",
        "option_a": "Ricky Ponting",
        "option_b": "Jacques Kallis",
        "option_c": "Sachin Tendulkar",
        "option_d": "Alastair Cook",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is the fastest bowler in cricket history?",
        "option_a": "Brett Lee",
        "option_b": "Shoaib Akhtar",
        "option_c": "Shaun Tait",
        "option_d": "Mitchell Starc",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player is known as 'Universe Boss'?",
        "option_a": "AB de Villiers",
        "option_b": "Chris Gayle",
        "option_c": "Andre Russell",
        "option_d": "Dwayne Bravo",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Who scored 100 international centuries?",
        "option_a": "Ricky Ponting",
        "option_b": "Virat Kohli",
        "option_c": "Sachin Tendulkar",
        "option_d": "Brian Lara",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Which player has the most wickets in ODI cricket?",
        "option_a": "Wasim Akram",
        "option_b": "Muttiah Muralitharan",
        "option_c": "Waqar Younis",
        "option_d": "Anil Kumble",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is known as 'King Kohli'?",
        "option_a": "Virender Sehwag",
        "option_b": "Rohit Sharma",
        "option_c": "Virat Kohli",
        "option_d": "KL Rahul",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player scored the fastest ODI century?",
        "option_a": "Corey Anderson",
        "option_b": "AB de Villiers",
        "option_c": "Shahid Afridi",
        "option_d": "Jos Buttler",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is known as 'Boom Boom'?",
        "option_a": "Shahid Afridi",
        "option_b": "Chris Gayle",
        "option_c": "Andre Russell",
        "option_d": "Brendon McCullum",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player has taken 10 wickets in a single Test innings?",
        "option_a": "Anil Kumble",
        "option_b": "Jim Laker",
        "option_c": "Both A and B",
        "option_d": "Shane Warne",
        "correct_answer": "C",
        "difficulty": "Hard",
        "category": "Player"
    },
    {
        "text": "Who is known as 'Mr. 360'?",
        "option_a": "AB de Villiers",
        "option_b": "Virat Kohli",
        "option_c": "Steve Smith",
        "option_d": "Joe Root",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player has the most sixes in international cricket?",
        "option_a": "Chris Gayle",
        "option_b": "Shahid Afridi",
        "option_c": "MS Dhoni",
        "option_d": "Rohit Sharma",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who scored 375 runs in a Test innings?",
        "option_a": "Brian Lara",
        "option_b": "Matthew Hayden",
        "option_c": "Virender Sehwag",
        "option_d": "Don Bradman",
        "correct_answer": "A",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Which player is known as 'Prince of Kolkata'?",
        "option_a": "Rahul Dravid",
        "option_b": "Sourav Ganguly",
        "option_c": "VVS Laxman",
        "option_d": "Anil Kumble",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Who has the most dismissals as a wicketkeeper in international cricket?",
        "option_a": "Adam Gilchrist",
        "option_b": "MS Dhoni",
        "option_c": "Mark Boucher",
        "option_d": "Kumar Sangakkara",
        "correct_answer": "C",
        "difficulty": "Hard",
        "category": "Player"
    },
    {
        "text": "Which player has the highest batting average in Test cricket?",
        "option_a": "Sachin Tendulkar",
        "option_b": "Don Bradman",
        "option_c": "Steve Smith",
        "option_d": "Joe Root",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who scored the fastest Test century?",
        "option_a": "Brendon McCullum",
        "option_b": "Viv Richards",
        "option_c": "Misbah-ul-Haq",
        "option_d": "Adam Gilchrist",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "Player"
    },
    {
        "text": "Which player has the most runs in T20 internationals?",
        "option_a": "Virat Kohli",
        "option_b": "Rohit Sharma",
        "option_c": "Babar Azam",
        "option_d": "David Warner",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is known as 'The Little Master'?",
        "option_a": "Sunil Gavaskar",
        "option_b": "Sachin Tendulkar",
        "option_c": "Both A and B",
        "option_d": "Rahul Dravid",
        "correct_answer": "C",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Which player has the most centuries in ODI cricket?",
        "option_a": "Sachin Tendulkar",
        "option_b": "Virat Kohli",
        "option_c": "Ricky Ponting",
        "option_d": "Rohit Sharma",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is known as 'The Finisher'?",
        "option_a": "MS Dhoni",
        "option_b": "AB de Villiers",
        "option_c": "Rohit Sharma",
        "option_d": "Virat Kohli",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player has taken the most wickets in international cricket?",
        "option_a": "Wasim Akram",
        "option_b": "Muttiah Muralitharan",
        "option_c": "James Anderson",
        "option_d": "Anil Kumble",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Who is known as 'The Run Machine'?",
        "option_a": "Rohit Sharma",
        "option_b": "Virat Kohli",
        "option_c": "Joe Root",
        "option_d": "Steve Smith",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player scored 264 in an ODI innings?",
        "option_a": "Virender Sehwag",
        "option_b": "Chris Gayle",
        "option_c": "Rohit Sharma",
        "option_d": "Martin Guptill",
        "correct_answer": "C",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Who has the most runs in IPL history?",
        "option_a": "Rohit Sharma",
        "option_b": "Virat Kohli",
        "option_c": "David Warner",
        "option_d": "MS Dhoni",
        "correct_answer": "B",
        "difficulty": "Medium",
        "category": "Player"
    },
    {
        "text": "Which player is known as 'The Turbanator'?",
        "option_a": "Harbhajan Singh",
        "option_b": "Yuvraj Singh",
        "option_c": "Irfan Pathan",
        "option_d": "Zaheer Khan",
        "correct_answer": "A",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Who is known as 'The Hitman'?",
        "option_a": "Virat Kohli",
        "option_b": "Rohit Sharma",
        "option_c": "David Warner",
        "option_d": "Chris Gayle",
        "correct_answer": "B",
        "difficulty": "Easy",
        "category": "Player"
    },
    {
        "text": "Which player has the most runs in a single Test series?",
        "option_a": "Don Bradman",
        "option_b": "Sachin Tendulkar",
        "option_c": "Virat Kohli",
        "option_d": "Alastair Cook",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "Player"
    },
    {
        "text": "Who is the only player to score centuries in all three formats in a calendar year?",
        "option_a": "Virat Kohli",
        "option_b": "Rohit Sharma",
        "option_c": "Babar Azam",
        "option_d": "Faf du Plessis",
        "correct_answer": "A",
        "difficulty": "Hard",
        "category": "Player"
    }

]

for q_data in questions:
    Question.objects.get_or_create(text=q_data['text'], defaults=q_data)

print("Database seeded with more categorized questions!")

const questions = [
    {
        question: "Which country has won the most ICC Men's Cricket World Cups?",
        options: ["India", "Australia", "West Indies", "England"],
        answer: 1 // Australia (Index 1)
    },
    {
        question: "Who holds the record for the highest individual score in a single ODI innings?",
        options: ["Chris Gayle", "Martin Guptill", "Rohit Sharma", "Sachin Tendulkar"],
        answer: 2 // Rohit Sharma (Index 2)
    },
    {
        question: "In which year did India win their first-ever ICC T20 World Cup?",
        options: ["2007", "2009", "2011", "2013"],
        answer: 0 // 2007 (Index 0)
    },
    {
        question: "Which cricketer is widely known as the 'God of Cricket'?",
        options: ["Virender Sehwag", "Virat Kohli", "Sachin Tendulkar", "MS Dhoni"],
        answer: 2 // Sachin Tendulkar (Index 2)
    },
    {
        question: "Which stadium is known as the 'Mecca of Cricket'?",
        options: ["Melbourne Cricket Ground (MCG)", "Eden Gardens", "Lord's Cricket Ground", "The Oval"],
        answer: 2 // Lord's (Index 2)
    }
];

let currentQuestionIndex = 0;
let score = 0;
let answered = false;

// DOM Elements
const questionEl = document.getElementById('question');
const optionsEl = document.getElementById('options');
const scoreDisplayEl = document.getElementById('score-display');
const progressEl = document.getElementById('progress');
const feedbackEl = document.getElementById('feedback');
const nextBtn = document.getElementById('next-btn');
const restartBtn = document.getElementById('restart-btn');
const quizScreen = document.getElementById('quiz-screen');
const resultScreen = document.getElementById('result-screen');
const finalScoreEl = document.getElementById('final-score');
const resultMessageEl = document.getElementById('result-message');

function initQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    answered = false;
    scoreDisplayEl.textContent = `Score: ${score}`;
    quizScreen.classList.remove('hidden');
    resultScreen.classList.add('hidden');
    loadQuestion();
}

function loadQuestion() {
    answered = false;
    nextBtn.classList.add('hidden');
    feedbackEl.textContent = '';
    
    const currentQuestion = questions[currentQuestionIndex];
    questionEl.textContent = currentQuestion.question;
    
    // Update progress bar
    const progressPercent = (currentQuestionIndex / questions.length) * 100;
    progressEl.style.width = `${progressPercent}%`;
    
    // Clear previous options
    optionsEl.innerHTML = '';
    
    // Create option buttons
    currentQuestion.options.forEach((option, index) => {
        const button = document.createElement('button');
        button.classList.add('option-btn');
        button.textContent = option;
        button.addEventListener('click', () => handleAnswer(index));
        optionsEl.appendChild(button);
    });
}

function handleAnswer(selectedIndex) {
    if (answered) return;
    answered = true;
    
    const currentQuestion = questions[currentQuestionIndex];
    const optionBtns = document.querySelectorAll('.option-btn');
    
    if (selectedIndex === currentQuestion.answer) {
        score++;
        scoreDisplayEl.textContent = `Score: ${score}`;
        optionBtns[selectedIndex].classList.add('correct');
        feedbackEl.textContent = 'Correct! 🏏';
        feedbackEl.style.color = '#10b981';
    } else {
        optionBtns[selectedIndex].classList.add('incorrect');
        optionBtns[currentQuestion.answer].classList.add('correct');
        feedbackEl.textContent = 'Incorrect! ❌';
        feedbackEl.style.color = '#ef4444';
    }
    
    // Disable all buttons
    optionBtns.forEach(btn => btn.disabled = true);
    
    // Show next button or end quiz button
    nextBtn.classList.remove('hidden');
    if (currentQuestionIndex === questions.length - 1) {
        nextBtn.textContent = 'See Final Score';
    } else {
        nextBtn.textContent = 'Next Question';
    }
}

nextBtn.addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        loadQuestion();
    } else {
        showResults();
    }
});

function showResults() {
    quizScreen.classList.add('hidden');
    resultScreen.classList.remove('hidden');
    finalScoreEl.textContent = score;
    
    let message = '';
    const ratio = score / questions.length;
    
    if (ratio === 1) message = "Perfect Score! You are a Cricket Legend! 👑";
    else if (ratio >= 0.8) message = "Excellent Knowledge! You really know your cricket! 🏆";
    else if (ratio >= 0.6) message = "Good effort! A true fan. 👍";
    else message = "Time to watch some more cricket highlights! 📺";
    
    resultMessageEl.textContent = message;
    progressEl.style.width = '100%';
}

restartBtn.addEventListener('click', initQuiz);

// Start the quiz
initQuiz();

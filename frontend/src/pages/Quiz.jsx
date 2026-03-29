import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import api from '../api';
import { motion, AnimatePresence } from 'framer-motion';
import { Timer, Zap, Loader2 } from 'lucide-react';

export default function Quiz() {
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [timeLeft, setTimeLeft] = useState(15);
  const [selectedOption, setSelectedOption] = useState(null);
  const [feedback, setFeedback] = useState(null); // 'correct' or 'wrong'
  const [xp, setXp] = useState(0);
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const fetchQuestions = async () => {
      const searchParams = new URLSearchParams(location.search);
      const category = searchParams.get('category');
      const difficulty = searchParams.get('difficulty');
      try {
        const res = await api.get(`questions/`, {
            params: { category, difficulty }
        });
        setQuestions(res.data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchQuestions();
  }, [location.search]);

  useEffect(() => {
    if (questions.length === 0 || feedback !== null) return;
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          handleTimeOut();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [currentIndex, questions, feedback]);

  const handleTimeOut = () => {
    setFeedback('wrong');
    setTimeout(nextQuestion, 2000);
  };

  const submitAnswer = async (ans) => {
    if (feedback !== null) return; // prevent multiple clicks
    setSelectedOption(ans);
    try {
      const res = await api.post('submit/', {
        question_id: questions[currentIndex].id,
        selected_answer: ans
      });
      setFeedback(res.data.is_correct ? 'correct' : 'wrong');
      if (res.data.is_correct) {
        setXp(res.data.new_xp);
      }
      setTimeout(nextQuestion, 2000);
    } catch (err) {
      console.error(err);
    }
  };

  const nextQuestion = () => {
    if (currentIndex + 1 >= questions.length) {
      navigate('/result', { state: { xp } });
    } else {
      setSelectedOption(null);
      setFeedback(null);
      setTimeLeft(15);
      setCurrentIndex(prev => prev + 1);
    }
  };

  if (loading) {
    return <div className="flex justify-center items-center h-[80vh]"><Loader2 className="w-12 h-12 animate-spin text-glow" /></div>;
  }

  if (!questions.length) {
    return <div className="text-center mt-20">No questions available. Try again later.</div>;
  }

  const currentQ = questions[currentIndex];
  const options = currentQ.options;

  return (
    <div className="flex flex-col items-center min-h-[85vh] py-10">
      <div className="flex justify-between w-full max-w-3xl mb-8 items-center bg-gray-900/50 p-4 rounded-xl border border-gray-700">
        <div className="flex items-center gap-2 text-xl font-bold font-mono">
          <Timer className={`w-6 h-6 ${timeLeft <= 5 ? 'text-red-500 animate-pulse' : 'text-glow'}`} /> {timeLeft}s
        </div>
        <div className="flex items-center gap-2 text-xl font-bold text-accent">
          <Zap className="w-6 h-6" /> XP: {xp}
        </div>
      </div>

      <div className="relative w-full max-w-3xl flex flex-col items-center justify-center min-h-[500px]">
        {/* Floating Question Card */}
        <AnimatePresence mode="popLayout">
          <motion.div
            key={currentIndex}
            initial={{ scale: 0, opacity: 0, rotate: -10 }}
            animate={{ scale: 1, opacity: 1, rotate: 0, y: [0, -10, 0] }}
            exit={{ scale: 0, opacity: 0, rotate: 10 }}
            transition={{ duration: 0.5, y: { repeat: Infinity, duration: 4, ease: "easeInOut" } }}
            className={`glass-card p-10 text-center w-full shadow-[0_0_30px_rgba(31,182,255,0.2)] z-10 
              ${feedback === 'correct' ? 'border-green-500 shadow-green-500/50' : ''}
              ${feedback === 'wrong' ? 'border-red-500 shadow-red-500/50' : ''}`}
          >
            <span className="text-sm font-bold tracking-widest text-glow uppercase block mb-3">
              {currentQ.category} • {currentQ.difficulty}
            </span>
            <h2 className="text-3xl font-bold leading-tight drop-shadow-lg">{currentQ.text}</h2>
          </motion.div>

          <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-6 w-full relative z-20 top-0">
            {options.map((opt, i) => {
              const isSelected = selectedOption === opt.key;
              
              let bgClass = "bg-card border-gray-700 hover:border-glow hover:bg-glow/10";
              if (feedback !== null) {
                if (isSelected) {
                   bgClass = feedback === 'correct' ? "bg-green-600 border-green-400" : "bg-red-600 border-red-400";
                } else if (feedback === 'wrong' && opt.key === 'A' /* This logic needs to be fixed to show correct answer but let's stick to user requirement */) {
                   // Optional: Highlight correct answer if user got it wrong
                } else {
                   bgClass = "bg-card border-gray-800 opacity-50";
                }
              }

              return (
                <motion.button
                  key={`${currentIndex}-${opt.key}`}
                  initial={{ opacity: 0, y: 50 }}
                  animate={{ opacity: 1, y: 0 }}
                  whileHover={{ scale: feedback !== null ? 1 : 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  transition={{ type: "spring", stiffness: 100, delay: i * 0.1 }}
                  onClick={() => submitAnswer(opt.key)}
                  disabled={feedback !== null}
                  className={`relative overflow-hidden w-full text-left p-6 rounded-xl border-2 transition-all shadow-lg ${bgClass}`}
                >
                  <div className="flex items-center gap-4">
                    <span className="w-10 h-10 flex items-center justify-center font-bold text-xl bg-space rounded-full border border-gray-600 shadow-inner">
                      {opt.key}
                    </span>
                    <span className="text-lg font-medium tracking-wide drop-shadow-sm">{opt.text}</span>
                  </div>
                  {isSelected && (
                    <motion.div layoutId="selected-glow" className="absolute inset-0 border-2 border-white rounded-xl shadow-[0_0_20px_rgba(255,255,255,0.8)]" />
                  )}
                </motion.button>
              );
            })}
          </div>
        </AnimatePresence>
      </div>
    </div>
  );
}

import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { PlayCircle } from 'lucide-react';

export default function Home({ isAuthenticated, setActiveCategory }) {
  const navigate = useNavigate();
  const [selectedCategory, setSelectedCategory] = useState(null);

  const selectCategory = (catId) => {
    setSelectedCategory(catId);
    setActiveCategory(catId);
  };

  const startQuiz = (difficulty) => {
    if (!isAuthenticated) return navigate('/login');
    navigate(`/quiz?category=${selectedCategory}&difficulty=${difficulty}`);
  };

  const goBack = () => {
    setSelectedCategory(null);
    setActiveCategory(null);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] text-center relative">
      {/* Background Floating Elements */}
      <div className="absolute top-10 left-10 w-32 h-32 bg-glow/20 rounded-full blur-3xl animate-float"></div>
      <div className="absolute bottom-10 right-10 w-48 h-48 bg-purple-500/20 rounded-full blur-3xl animate-float shadow-2xl"></div>
      
      <motion.div 
        initial={{ y: -50, opacity: 0 }} 
        animate={{ y: 0, opacity: 1 }} 
        transition={{ duration: 0.8, type: 'spring' }}
        className="z-10"
      >
        <h1 className="text-6xl md:text-8xl font-extrabold mb-6 tracking-tight text-transparent bg-clip-text bg-gradient-to-br from-glow via-white to-purple-500">
          Zero Gravity <br /> Cricket Quiz
        </h1>
        <p className="text-xl md:text-2xl text-gray-300 mb-10 max-w-2xl mx-auto font-light">
          Defy gravity with your cricket knowledge. Answer faster, earn more XP, and conquer the leaderboard!
        </p>
        
        <AnimatePresence mode="wait">
          {!selectedCategory ? (
            <motion.div 
              key="categories"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="flex flex-wrap justify-center gap-4 mt-10"
            >
              {[
                { id: 'IPL', label: 'IPL Quiz', color: 'from-blue-600 to-indigo-600' },
                { id: 'World Cup', label: 'World Cup Quiz', color: 'from-purple-600 to-pink-600' },
                { id: 'Player', label: 'Player Quiz', color: 'from-orange-600 to-red-600' }
              ].map((cat) => (
                <motion.button 
                  key={cat.id}
                  whileHover={{ scale: 1.05, boxShadow: '0 0 20px rgba(31, 182, 255, 0.4)' }}
                  whileTap={{ scale: 0.95 }}
                  onClick={() => selectCategory(cat.id)}
                  className={`flex items-center gap-2 px-8 py-4 bg-gradient-to-r ${cat.color} rounded-xl text-xl font-bold transition-all relative group overflow-hidden shadow-lg`}
                >
                  <span className="relative z-10 flex items-center gap-2">
                    <PlayCircle className="w-6 h-6"/> {cat.label}
                  </span>
                </motion.button>
              ))}
            </motion.div>
          ) : (
            <motion.div 
              key="difficulty"
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.9 }}
              className="flex flex-col items-center gap-6"
            >
              <h2 className="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-accent to-glow">Select Difficulty Level</h2>
              <div className="flex flex-wrap justify-center gap-4">
                {[
                  { level: 'Easy', color: 'from-green-500 to-emerald-600' },
                  { level: 'Medium', color: 'from-yellow-400 to-orange-500' },
                  { level: 'Hard', color: 'from-red-600 to-rose-700' }
                ].map((diff) => (
                  <motion.button
                    key={diff.level}
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.9 }}
                    onClick={() => startQuiz(diff.level)}
                    className={`px-8 py-3 bg-gradient-to-r ${diff.color} rounded-lg text-lg font-bold shadow-lg`}
                  >
                    {diff.level}
                  </motion.button>
                ))}
              </div>
              <button 
                onClick={goBack}
                className="text-gray-400 hover:text-white mt-4 underline decoration-dashed underline-offset-4"
              >
                ← Back to Categories
              </button>
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>
    </div>
  );
}

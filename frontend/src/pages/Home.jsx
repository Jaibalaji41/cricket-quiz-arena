import React from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { PlayCircle } from 'lucide-react';

export default function Home({ isAuthenticated }) {
  const navigate = useNavigate();

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
        
        <motion.button 
          whileHover={{ scale: 1.1, boxShadow: '0 0 20px rgba(31, 182, 255, 0.6)' }}
          whileTap={{ scale: 0.95 }}
          onClick={() => navigate(isAuthenticated ? '/quiz' : '/login')}
          className="flex items-center gap-2 mx-auto px-8 py-4 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-full text-2xl font-bold transition-all relative group overflow-hidden"
        >
          <span className="absolute inset-0 bg-white/20 group-hover:w-full w-0 transition-all duration-300 z-0"></span>
          <span className="relative z-10 flex items-center gap-2"><PlayCircle className="w-8 h-8"/> Start Match</span>
        </motion.button>
      </motion.div>
    </div>
  );
}

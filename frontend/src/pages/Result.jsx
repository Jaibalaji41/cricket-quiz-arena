import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Trophy, RefreshCcw, Home } from 'lucide-react';

export default function Result() {
  const location = useLocation();
  const navigate = useNavigate();
  const xp = location.state?.xp || 0;

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh]">
      <motion.div 
        initial={{ scale: 0.5, opacity: 0 }} 
        animate={{ scale: 1, opacity: 1 }} 
        transition={{ type: "spring", stiffness: 120 }}
        className="glass-card p-10 text-center rounded-3xl w-full max-w-lg shadow-[0_0_50px_rgba(31,182,255,0.3)] relative overflow-hidden"
      >
        <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-glow to-purple-500"></div>
        <motion.div 
          animate={{ rotate: 360 }} 
          transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
          className="mx-auto w-32 h-32 rounded-full border-4 border-dashed border-glow flex items-center justify-center mb-6 shadow-glow"
        >
          <Trophy className="w-16 h-16 text-yellow-500 drop-shadow-[0_0_10px_rgba(234,179,8,0.8)]" />
        </motion.div>
        
        <h2 className="text-4xl font-extrabold mb-2 text-transparent bg-clip-text bg-gradient-to-r from-glow to-accent drop-shadow-lg">Match Over!</h2>
        <p className="text-xl text-gray-300 mb-8 font-light tracking-wide">You earned <span className="font-bold text-glow">{xp} XP</span></p>

        <div className="flex justify-center gap-6">
          <button 
            onClick={() => navigate('/quiz')}
            className="flex items-center gap-2 px-6 py-3 bg-space/80 border border-glow text-white rounded-full hover:bg-glow hover:text-black font-bold transition-all"
          >
            <RefreshCcw className="w-5 h-5" /> Play Again
          </button>
          <button 
            onClick={() => navigate('/')}
            className="flex items-center gap-2 px-6 py-3 bg-purple-600/80 border border-purple-400 text-white rounded-full hover:bg-purple-500 font-bold transition-all"
          >
            <Home className="w-5 h-5" /> Home
          </button>
        </div>
      </motion.div>
    </div>
  );
}

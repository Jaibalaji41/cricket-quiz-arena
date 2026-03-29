import React, { useState, useEffect } from 'react';
import api from '../api';
import { motion } from 'framer-motion';
import { Medal, Loader2 } from 'lucide-react';

export default function Leaderboard() {
  const [leaders, setLeaders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const res = await api.get('leaderboard/');
        setLeaders(res.data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchLeaderboard();
  }, []);

  if (loading) {
    return <div className="flex justify-center items-center h-[80vh]"><Loader2 className="w-12 h-12 animate-spin text-glow" /></div>;
  }

  return (
    <div className="flex flex-col items-center py-10 min-h-[80vh]">
      <motion.div initial={{ y: -50, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="flex items-center gap-4 mb-10">
        <Medal className="w-12 h-12 text-yellow-400 drop-shadow-[0_0_15px_rgba(250,204,21,0.8)]" />
        <h2 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-yellow-600">Global Rankings</h2>
      </motion.div>
      
      <div className="w-full max-w-2xl space-y-4">
        {leaders.map((leader, index) => {
          let rankClass = "bg-card border-gray-700 text-gray-300";
          let icon = null;
          if (index === 0) {
            rankClass = "bg-yellow-500/10 border-yellow-500 text-yellow-400 font-bold scale-105 shadow-yellow-500/20";
            icon = "🏆";
          } else if (index === 1) {
            rankClass = "bg-gray-300/10 border-gray-300 text-gray-200 shadow-gray-300/20";
            icon = "🥈";
          } else if (index === 2) {
            rankClass = "bg-orange-600/10 border-orange-600 text-orange-500 shadow-orange-600/20";
            icon = "🥉";
          }

          return (
            <motion.div 
              key={index} 
              initial={{ x: -50, opacity: 0 }} 
              animate={{ x: 0, opacity: 1 }} 
              transition={{ delay: index * 0.1, type: "spring" }}
              className={`flex justify-between items-center p-6 rounded-2xl border-2 backdrop-blur-md shadow-lg ${rankClass} hover:brightness-125 transition-all`}
            >
              <div className="flex items-center gap-4">
                <span className="text-2xl w-8 text-center">{icon || `#${index + 1}`}</span>
                <span className="text-xl tracking-wider">{leader.username}</span>
              </div>
              <div className="text-xl flex gap-2 items-center">
                <span>{leader.score}</span> <span className="text-sm font-light uppercase tracking-widest text-gray-500">XP</span>
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}

import React, { useState, useEffect } from 'react';
import api from '../api';
import { motion } from 'framer-motion';
import { Flame, Star, Award, Loader2 } from 'lucide-react';

export default function Profile() {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const res = await api.get('profile/');
        setProfile(res.data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchProfile();
  }, []);

  if (loading) {
    return <div className="flex justify-center items-center h-[80vh]"><Loader2 className="w-12 h-12 animate-spin text-glow" /></div>;
  }

  if (!profile) {
    return <div className="text-center mt-20">Please log in to see profile.</div>;
  }

  // Calculate progress to next level (each level is 100 XP)
  const currentXP = profile.xp;
  const progressPercent = currentXP % 100;

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] py-10">
      <motion.div 
        initial={{ scale: 0.9, opacity: 0 }} 
        animate={{ scale: 1, opacity: 1 }} 
        className="glass-card w-full max-w-3xl p-10 rounded-[2rem] shadow-[0_10px_50px_rgba(0,0,0,0.5)] border-t border-white/10 relative overflow-hidden"
      >
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-glow/20 rounded-full blur-3xl mix-blend-screen pointer-events-none"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-purple-600/20 rounded-full blur-3xl mix-blend-screen pointer-events-none"></div>

        <div className="relative z-10">
          <div className="flex items-center gap-6 mb-12">
            <div className="w-24 h-24 rounded-full bg-gradient-to-tr from-accent to-glow p-1 mask-hexagon flex items-center justify-center shadow-[0_0_20px_rgba(31,182,255,0.4)]">
               <div className="w-full h-full bg-space rounded-full flex items-center justify-center font-bold text-4xl text-white">
                 {profile.username[0].toUpperCase()}
               </div>
            </div>
            <div>
              <h2 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400">{profile.username}</h2>
              <p className="text-gray-400 text-lg">{profile.email}</p>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
            <motion.div whileHover={{ y: -5 }} className="bg-white/5 border border-white/10 p-6 rounded-2xl flex flex-col items-center text-center">
              <Star className="w-10 h-10 text-yellow-400 mb-2 drop-shadow-[0_0_10px_rgba(250,204,21,0.6)]" />
              <span className="text-3xl font-bold">{profile.total_score}</span>
              <span className="text-gray-400 text-sm tracking-widest uppercase mt-1">Total XP</span>
            </motion.div>
            
            <motion.div whileHover={{ y: -5 }} className="bg-white/5 border border-white/10 p-6 rounded-2xl flex flex-col items-center text-center">
              <Award className="w-10 h-10 text-glow mb-2 drop-shadow-[0_0_10px_rgba(31,182,255,0.6)]" />
              <span className="text-3xl font-bold">{profile.level}</span>
              <span className="text-gray-400 text-sm tracking-widest uppercase mt-1">Level</span>
            </motion.div>
            
            <motion.div whileHover={{ y: -5 }} className="bg-white/5 border border-white/10 p-6 rounded-2xl flex flex-col items-center text-center">
              <Flame className="w-10 h-10 text-orange-500 mb-2 drop-shadow-[0_0_10px_rgba(249,115,22,0.6)]" />
              <span className="text-3xl font-bold text-white">{profile.streak} <span className="text-lg">🔥</span></span>
              <span className="text-gray-400 text-sm tracking-widest uppercase mt-1">Streak</span>
            </motion.div>
          </div>

          <div className="bg-white/5 border border-white/10 p-6 rounded-2xl">
            <div className="flex justify-between text-sm text-gray-400 mb-2 font-bold tracking-widest">
              <span>LEVEL {profile.level}</span>
              <span>LEVEL {profile.level + 1}</span>
            </div>
            <div className="w-full bg-space rounded-full h-4 overflow-hidden border border-gray-700 relative">
              <motion.div 
                initial={{ width: 0 }} 
                animate={{ width: `${progressPercent}%` }} 
                transition={{ duration: 1.5, ease: "easeOut" }}
                className="h-full bg-gradient-to-r from-glow to-accent relative"
              >
                <div className="absolute top-0 right-0 bottom-0 w-8 bg-white/30 blur opacity-50"></div>
              </motion.div>
            </div>
            <p className="text-center text-sm text-gray-400 mt-4 tracking-wide">{100 - progressPercent} XP to Next Level</p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

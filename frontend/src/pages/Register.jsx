import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../api';
import { motion } from 'framer-motion';

export default function Register({ setIsAuthenticated }) {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await api.post('register/', { username, email, password });
      const res = await api.post('login/', { username, password });
      localStorage.setItem('access', res.data.access);
      localStorage.setItem('refresh', res.data.refresh);
      setIsAuthenticated(true);
      navigate('/');
    } catch (err) {
      setError('Registration failed. Username may exist.');
    }
  };

  return (
    <div className="flex items-center justify-center h-[80vh]">
      <motion.div initial={{ scale: 0.9, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="glass-card p-8 rounded-xl w-96 text-center">
        <h2 className="text-3xl font-bold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-glow to-accent">Register</h2>
        {error && <p className="text-red-400 mb-4">{error}</p>}
        <form onSubmit={handleRegister} className="flex flex-col gap-4">
          <input className="bg-space/50 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:border-glow text-white" 
                 placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
          <input className="bg-space/50 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:border-glow text-white" 
                 type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
          <input className="bg-space/50 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:border-glow text-white" 
                 type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
          <button className="bg-gradient-to-r from-purple-500 to-indigo-600 hover:from-purple-600 hover:to-indigo-700 font-bold py-2 rounded-lg transition-all" type="submit">
            Join Arena
          </button>
        </form>
        <p className="mt-4 text-gray-400">Already a player? <Link to="/login" className="text-glow hover:underline">Login</Link></p>
      </motion.div>
    </div>
  );
}

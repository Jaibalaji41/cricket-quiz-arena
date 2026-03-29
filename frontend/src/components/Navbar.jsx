import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Home, Trophy, User, LogOut, Shield } from 'lucide-react';
import { motion } from 'framer-motion';

export default function Navbar({ isAuthenticated, setIsAuthenticated }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    setIsAuthenticated(false);
    navigate('/');
  };

  return (
    <nav className="fixed w-full z-50 glass top-0">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center space-x-2">
            <motion.div animate={{ rotate: 360 }} transition={{ duration: 10, repeat: Infinity, ease: "linear" }}>
               <Shield className="w-8 h-8 text-glow" />
            </motion.div>
            <span className="font-bold text-xl tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-glow to-accent">
              Cricket Quiz Arena
            </span>
          </Link>
          <div className="flex space-x-4 items-center">
            <Link to="/" className="text-gray-300 hover:text-white flex items-center gap-1 transition-colors"><Home className="w-4 h-4" /> Home</Link>
            <Link to="/leaderboard" className="text-gray-300 hover:text-white flex items-center gap-1 transition-colors"><Trophy className="w-4 h-4" /> Leaderboard</Link>
            {isAuthenticated ? (
              <>
                <Link to="/profile" className="text-gray-300 hover:text-white flex items-center gap-1 transition-colors"><User className="w-4 h-4" /> Profile</Link>
                <button onClick={handleLogout} className="text-red-400 hover:text-red-300 flex items-center gap-1 transition-colors">
                  <LogOut className="w-4 h-4" /> Logout
                </button>
              </>
            ) : (
              <Link to="/login" className="px-4 py-2 rounded-full bg-blue-600/20 border border-blue-500 hover:bg-blue-600/40 transition-all font-semibold">
                Login
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}

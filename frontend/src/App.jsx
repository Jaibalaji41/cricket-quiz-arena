import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Quiz from './pages/Quiz';
import Result from './pages/Result';
import Leaderboard from './pages/Leaderboard';
import Profile from './pages/Profile';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('access'));

  return (
    <Router>
      <div className="min-h-screen text-white">
        <Navbar isAuthenticated={isAuthenticated} setIsAuthenticated={setIsAuthenticated} />
        <div className="pt-20 pb-10 px-4 max-w-7xl mx-auto">
          <Routes>
            <Route path="/" element={<Home isAuthenticated={isAuthenticated} />} />
            <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
            <Route path="/register" element={<Register setIsAuthenticated={setIsAuthenticated} />} />
            <Route path="/quiz" element={isAuthenticated ? <Quiz /> : <Navigate to="/login" />} />
            <Route path="/result" element={isAuthenticated ? <Result /> : <Navigate to="/login" />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/profile" element={isAuthenticated ? <Profile /> : <Navigate to="/login" />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;

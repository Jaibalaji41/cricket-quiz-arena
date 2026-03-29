import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Quiz from './pages/Quiz';
import Result from './pages/Result';
import Leaderboard from './pages/Leaderboard';
import Profile from './pages/Profile';

function BackgroundManager({ activeCategory }) {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const urlCategory = searchParams.get('category');

  const category = activeCategory || urlCategory;

  let bgClass = "bg-default";
  if (category === "IPL") bgClass = "bg-ipl";
  else if (category === "World Cup") bgClass = "bg-wc";
  else if (category === "Player") bgClass = "bg-player";
  else bgClass = "bg-default";

  return <div className={`dynamic-bg ${bgClass}`} />;
}

function AppContent() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('access'));
  const [activeCategory, setActiveCategory] = useState(null);
  const location = useLocation();

  useEffect(() => {
    // Clear activeCategory if we navigate away from Home and NOT to a URL with a category
    const searchParams = new URLSearchParams(location.search);
    if (location.pathname !== '/' && !searchParams.get('category')) {
      setActiveCategory(null);
    }
  }, [location]);

  return (
    <div className="min-h-screen text-white relative">
      <BackgroundManager activeCategory={activeCategory} />
      <Navbar isAuthenticated={isAuthenticated} setIsAuthenticated={setIsAuthenticated} />
      <div className="pt-20 pb-10 px-4 max-w-7xl mx-auto">
        <Routes>
          <Route path="/" element={<Home isAuthenticated={isAuthenticated} setActiveCategory={setActiveCategory} />} />
          <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
          <Route path="/register" element={<Register setIsAuthenticated={setIsAuthenticated} />} />
          <Route path="/quiz" element={isAuthenticated ? <Quiz /> : <Navigate to="/login" />} />
          <Route path="/result" element={isAuthenticated ? <Result /> : <Navigate to="/login" />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/profile" element={isAuthenticated ? <Profile /> : <Navigate to="/login" />} />
        </Routes>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}

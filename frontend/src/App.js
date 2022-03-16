import React from "react";
import Test from "./components/Test";
import Header from "./components/Header";
import Profile from "./components/Profile";
import Signup from "./components/signup/Signup";
import Login from "./components/login/Login";
import Blog from "./components/blog/Blog";
import Footer from "./components/Footer";

import { ToastContainer } from "react-toastify";

import { Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <div>
      <Header />
      <ToastContainer
        hideProgressBar={true}
        newestOnTop={true}
        autoClose={3000}
      />
      <Routes>
        <Route path="/" element={<Test />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/blogs" element={<Blog />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
      </Routes>
      <Footer />
    </div>
  );
};

export default App;

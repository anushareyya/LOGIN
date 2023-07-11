import './App.css';
import Login from './Login-form'
import Profile from './Profile';
import { BrowserRouter, Routes, Route,NavLink } from "react-router-dom";


function App() {
  return (
    <>
      <BrowserRouter>
        <NavLink to="/LoginPage">
          <button>login</button>
        </NavLink>
        <Routes>
          <Route path="/LoginPage" element={<Login />} />
          <Route path="/Profile" element={<Profile />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;

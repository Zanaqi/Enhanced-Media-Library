import './App.css';

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from './components/Home';
import Navbar from './components/templates/Navbar';

function App() {
  return(
    <>
      <Navbar/>
      <BrowserRouter>
        <Routes>
          {/* Define your routes using the Route component */}
          <Route exact path="/" element={<Home/>} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;

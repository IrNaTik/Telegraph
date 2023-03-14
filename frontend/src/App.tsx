import React, { useState } from 'react';
import { Route, BrowserRouter, Routes } from 'react-router-dom';


import './App.scss';

import Auth from  './components/Auth/auth';
import Home from './components/Home/home'; 



function App() {
//   const [username, setUsername] = useState('')

  return (
    <BrowserRouter>
        <Routes>
        <Route path='/login' element={<Auth/>}></Route>
        <Route path='/' element={<Home props={'home'}/>}></Route>
        <Route path='/:username' 
          element={<Home props={'certainChat'}/>}></Route>
        </Routes>

        
    </BrowserRouter>
  );
}

export default App;

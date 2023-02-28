import React from 'react';
import { Route, BrowserRouter, Routes } from 'react-router-dom';
import './App.scss';

import Auth from './components/Auth/auth';

function App() {
  

  return (
    <BrowserRouter>
        <Routes>
        <Route path='/login' element={<Auth/>}></Route>
        </Routes>
    </BrowserRouter>
  );
}

export default App;

import React, { useState, useEffect } from 'react';
import { Route, BrowserRouter, Routes } from 'react-router-dom';
import './App.scss';

import Auth from './components/Auth/auth';

import Chat from './components/Auth/Chat/Chat';
import CertainChat from './components/Auth/Chat/CertainChat';

function App() {
  
  const [chatId, setChatId] = useState<number>()

  useEffect(()=> {
    console.log(chatId)
  }, [chatId])
  return (
    <BrowserRouter>
        <Routes>
        <Route path='/login' element={<Auth/>}></Route>
        <Route path='/chat' element={<Chat/>}></Route>
        
        <Route path='/chat/:chatId' element={<CertainChat    />}></Route>  
        </Routes>
    </BrowserRouter>
  );
}

export default App;

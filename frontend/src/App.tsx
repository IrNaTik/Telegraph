import React, { useState, useEffect } from 'react';
import { Route, BrowserRouter, Routes } from 'react-router-dom';

import './App.scss';

import Auth from  './components/Auth/auth';
import Home from './components/Home/home'; 

import Chat from './components/Chat/Chat';
import CertainChat from './components/Chat/CertainChat';
import MediaChat from './components/MediaChat/Chat';

function App() {
  

  return (
    <BrowserRouter>
        <Routes>
        <Route path='/login' element={<Auth/>}></Route>
        <Route path='/chat' element={<Chat/>}></Route>
        <Route path='/media-chat' element={<MediaChat/>}></Route>
        <Route path='chats' element={<Home/>}></Route>
        <Route path='/chat/:chatId' element={<CertainChat    />}></Route>  
        </Routes>
    </BrowserRouter>
  );
}

export default App;

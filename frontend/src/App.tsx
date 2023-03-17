import {  BrowserRouter } from 'react-router-dom';


import './App.scss';
import { AppRouter } from './components/AppRouter';


function App() {

  return (
    <BrowserRouter>
        <AppRouter></AppRouter>
    </BrowserRouter>
  );
}

export default App;

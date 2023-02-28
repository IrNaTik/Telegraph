import React, { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [data, setData] = useState('None');

  useEffect(() => {
    axios.get("http://localhost:8080")
      .then((response) => {
          console.log(response);
          console.log(response.data)
    })
  }, [])

  return (
    <div className="App">
      
    </div>
  );
}

export default App;

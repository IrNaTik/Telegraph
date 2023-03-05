import React, { useState, useEffect } from 'react';
import useWebSocket from 'react-use-websocket';
import { Navigate } from 'react-router-dom';


const WS_URL = 'ws://localhost:8000/ws/chat';


function Chat() {
    const [chatId, setChatId] = useState('')
    const [submitChat, setSubmitChat] = useState<Boolean>(false);
   
    const [navigate, setNavigate] = useState<any>()
    
    

    function openChat(e: any) {
      
      
      setSubmitChat(true)
      setNavigate( <Navigate to={"/chat/" + chatId} replace={false} />)
        
    }

    function handleChange(e: any){
      setChatId(e.target.value)
    }

    return (
      <>
        Введите номер чата:
        <input type="text" value={ chatId } placeholder='Номер чата' onChange={e => handleChange(e)}></input>
        <button onClick={e =>  openChat(e)} >Открыть чат</button>

        {
          navigate
        }
      </>
    );
  }
  
  export default Chat;
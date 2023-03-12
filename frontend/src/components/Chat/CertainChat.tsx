import React, { useState, useEffect } from 'react';
import useWebSocket from 'react-use-websocket';





function CertainChat() {
    const [messages, setMessages] = useState<Array<String>>([])
    const [userMessage, setUserMessage] = useState('')
    
    const WS_URL = 'ws://localhost:8000/ws/chat/' // Подключение к сокету
    const { sendJsonMessage } = useWebSocket(decodeURI(WS_URL), {
        onOpen: () => {

          // Отправка chat_id
          const chatId = window.location.pathname.split('/').pop()
          sendJsonMessage({
            'type': 'chatId',
            'chatId': chatId
          })    
        },
        onMessage: (response) => {
          const data = JSON.parse(response.data) 

          if (data.type === "message"){
            setMessages([...messages, data.message])
          }
          
        }
      });

    function submitMessage(e: any){
        const chatId= window.location.pathname.split('/').pop()
        sendJsonMessage({
            'type': 'message',
            'message': userMessage, 
            'chatId': chatId
        })
        setUserMessage('')
    }
    
    function handleChange(e: any){
    setUserMessage(e.target.value)
    }

    return (
      <>
        
        <input type="text" value={ userMessage } onChange={e => handleChange(e)} placeholder='Новое сообщение'></input>
        <button onClick={e =>  submitMessage(e)} >Отправить</button>

      </>
    );
  }
  
  export default CertainChat;
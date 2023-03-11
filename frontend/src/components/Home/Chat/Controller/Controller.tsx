import React, { useState } from "react";

import {AiOutlineSend} from 'react-icons/ai'
import useWebSocket from 'react-use-websocket'

export function Controller(props:any) {

    const [message, setMessages] = useState<Array<String>>([])
    const [userMessage, setUserMessage] = useState('')
    
    const WS_URL = 'ws://localhost:8000/ws/chat/' // Подключение к сокету

    const { sendJsonMessage } = useWebSocket(decodeURI(WS_URL), {
        onOpen: () => {

          const chatId = window.location.pathname.split('/').pop()
          sendJsonMessage({
            'type': 'chatId',
            'chatId': chatId
          })    
        },
        onMessage: (response) => {
          const data = JSON.parse(response.data) 

          if (data.type === "message"){
            setMessages([...message, data.message])
          }
          
        }
      });

    function submitMessage(e: any){
        // const chatId= window.location.pathname.split('/').pop()
        const chatId = 1
        sendJsonMessage({
            'type': 'message',
            'message': userMessage, 
            'chatId': chatId
        })
        setUserMessage('')
    }

    function handleChange(e: any) {
        setUserMessage(e.target.value)
    }


    return (
        <div className="ConrollerIns">
            <div className="Input-Controller">
                <textarea value={userMessage} 
                onChange={e=> handleChange(e)} autoCorrect="on"  autoFocus={true} rows={4} placeholder="Message" className="TextArea-Controller"></textarea>
                <AiOutlineSend className="Send-Button" onClick={e => submitMessage(e)} />
            </div>
        </div>
    )
}
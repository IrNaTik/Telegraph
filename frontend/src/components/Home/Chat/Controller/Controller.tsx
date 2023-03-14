import React, { useState } from "react";

import {AiOutlineSend} from 'react-icons/ai'
import useWebSocket from 'react-use-websocket'

import MessageSlice from "src/store/messsages";
import { useAppDispatch } from "src/store/store";

export function Controller(props:any) {
    const dispatch = useAppDispatch()
    // const [message, setMessages] = useState<Array<String>>([])
    const [userMessage, setUserMessage] = useState('')
    
    const WS_URL = 'ws://localhost:8000/ws/chat/' // Подключение к сокету

    const { sendJsonMessage } = useWebSocket(decodeURI(WS_URL), {
        onOpen: () => {

        //   const chatId = window.location.pathname.split('/').pop()
        const chatId = 1   
        sendJsonMessage({
            'type': 'chatId',
            'chatId': chatId
          })    
        },
        onMessage: (response) => {
          const data = JSON.parse(response.data) 
          
          if (data.type === "message"){
            dispatch(MessageSlice.actions.add(data.message))
          }
          
        }
      });

    function submitMessage(){
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

    function handleKey(e: React.KeyboardEvent<HTMLTextAreaElement>) {
        if (e.code === 'Enter' || e.code === "NumpadEnter" ) {
            e.preventDefault()
            submitMessage()
        }
    }


    return (
        <div className="ConrollerIns">
            <div className="Input-Controller">
                <textarea value={userMessage} 
                onChange={e=> handleChange(e)} autoCorrect="on"  autoFocus={true} rows={4} placeholder="Message" className="TextArea-Controller" onKeyDown={e => handleKey(e)}></textarea>
                <AiOutlineSend className="Send-Button" id="Control-Button" onClick={e => submitMessage()} />
            </div>
        </div>
    )
}
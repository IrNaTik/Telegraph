import React, { useState, useEffect } from "react";

import {AiOutlineSend} from 'react-icons/ai'
import { useAppDispatch } from "src/store/store";
import MessageSlice from "src/store/messsages";

import $api from "src/utils/api/axios";

interface PropsInterface{
    myUsername: string,
    sendJsonMessage: Function
}

export function Controller({ myUsername, sendJsonMessage }: PropsInterface) {
    const dispatch = useAppDispatch()
    // const [message, setMessages] = useState<Array<String>>([])
    const [userMessage, setUserMessage] = useState('')
    const [getterUsername, setGetterUsername] = useState('')

    useEffect(() => {
        const arr = window.location.href.split('/')
        const last = arr.length - 1
        

        if (arr[last]) {
            setGetterUsername(arr[last])
            $api.get('http://127.0.0.1:8000/get-chat-existing/?username=' + arr[last] + '&myUsername=' + myUsername)
            .then((response) => {
                const data = response.data
                console.log(data)
                if (data.chatExists) {
                    // Получение сообщений по пагинации
                    // $api.get('http://127.0.0.1:8000/get-chat-messages/?username=' + arr[last] + '&myUsername=' + myUsername)
                    // .then((response) => {
                    //     const data = response.data
                    //     console.log(data)k
                        
                    // })
                }
                localStorage.setItem('token', response.data.AssesToken)
            })
        }
        
    }, [])
    

    function submitMessage(){
        dispatch(MessageSlice.actions.add({'username': myUsername, 'message': userMessage}))
        sendJsonMessage({
            'type': 'message',
            'message': userMessage, 
            'senderUsername': myUsername,
            'getterUsername': getterUsername 
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
import React, { useEffect } from "react";
import { Message } from "./Message/Message";
import { Controller } from "./Controller/Controller";
import { useAppSelector } from "src/store/store";
import $api from "src/api/axios";



export function ChatIns(props: any) {
    const isOpen = useAppSelector(state => state.ChatStore.isOpen)
    const messageList = useAppSelector(state => state.MessageStore.messages)

    useEffect(() => {
<<<<<<< HEAD
        const arr = window.location.href.split('/')
        const last = arr.length - 1
        
        if (arr[last]) {
            console.log('good')

            $api.get('get-chat-with-user/' + arr[last])
            .then(function (response) {
                console.log(response)
            });
        
        } else {
            console.log('User is not choosen')
        }
    }, [])

    

    useEffect(() => {
        const elem = document.getElementById("Chat-Scroll")
        elem!.scrollTop = elem!.scrollHeight
=======
        if (isOpen) {
            const elem = document.getElementById("Chat-Scroll")
            elem!.scrollTop = elem!.scrollHeight
        }
        
>>>>>>> 3a0918f2b12d4ac36056e4bd0e388765c27b216d
    }, [messageList])

    const OpenChat = <>
        <div className="Chat-Scrollable" id="Chat-Scroll">
            <div className="ChatIns" >
                {messageList.length > 0 ? messageList.map((str, idx) => <Message key={idx}  content={str} isSender={true}/>) : null} 
            </div>
        </div>
            <Controller/>
    </>



    return (
        <>
            {
                isOpen? OpenChat: <></> 
            }
        </>
    )
} 
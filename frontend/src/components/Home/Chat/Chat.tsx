import React, { useEffect, useState } from "react";
import { Message } from "./Message/Message";
import { Controller } from "./Controller/Controller";
import { useAppSelector } from "src/store/store";
import $api from "src/utils/api/axios";



export function ChatIns({myUsername, sendJsonMessage }: any) {
    const isOpen = useAppSelector(state => state.ChatStore.isOpen)
    const messageList = useAppSelector(state => state.MessageStore.messages)
    

    useEffect(() => {
        if (isOpen) {
            const elem = document.getElementById("Chat-Scroll")
            elem!.scrollTop = elem!.scrollHeight 
        }
        
    }, [messageList])

    

    const OpenChat = <>
        <div className="Chat-Scrollable" id="Chat-Scroll">
            
            <div className="ChatIns" >
                {messageList.length > 0 ? messageList.map((str, idx) => <Message key={idx}  content={str} isSender={true}/>) : null} 
            </div>
        </div>
            <Controller myUsername={ myUsername } sendJsonMessage={ sendJsonMessage }/>
    </>



    return (
        <>
            {
                isOpen? OpenChat: <></> 
            }
        </>
    )
} 
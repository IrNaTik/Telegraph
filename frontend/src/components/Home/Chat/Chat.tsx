import React, { useEffect } from "react";
import { Message } from "./Message/Message";
import { Controller } from "./Controller/Controller";
import { useAppSelector } from "src/store/store";

export function ChatIns(props: any) {
    const messageList = useAppSelector(state => state.MessageStore.messages)

    useEffect(() => {
        
    }, [messageList])

    return (
        <>
        <div className="ChatIns">
            {messageList.length > 0 ? messageList.map((str, idx) => <Message key={idx}  content={str} isSender={true}/>) : null} 
        </div>
        <Controller/>
        </>
    )
} 
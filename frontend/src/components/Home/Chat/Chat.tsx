import React, { useEffect } from "react";
import { Message } from "./Message/Message";
import { Controller } from "./Controller/Controller";
import { useAppSelector } from "src/store/store";

export function ChatIns(props: any) {
    const messageList = useAppSelector(state=> state.MessageStore.messages)

    useEffect(() => {
        console.log(messageList.length)
    }, [messageList])

    return (
        <>
        <div className="ChatIns">
            {messageList.length > 0 ? messageList.map(str => <Message content={str}/>) : null} 
        </div>
        <Controller/>
        </>
    )
} 
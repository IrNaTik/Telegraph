import React from "react";
import { Message } from "./Message/Message";

export function ChatIns(props: any) {
    return (
        <div className="ChatIns">
            <Message isSender={true}/>
            <Message isSender={true}/>
            <Message />
            <Message />
            <Message />

        </div>
            
    )
} 
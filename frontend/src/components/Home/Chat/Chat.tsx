import React, { useEffect } from "react";
import { Message } from "./Message/Message";
import { Controller } from "./Controller/Controller";
import { useAppSelector, useAppDispatch } from "src/store/store";
import $api from "src/utils/api/axios";
import MessageSlice, { IMessage } from "src/store/messsages";

export function ChatIns({ myUsername, sendJsonMessage }: any) {
    const isOpen = useAppSelector((state) => state.ChatStore.isOpen);
    const messageList = useAppSelector((state) => state.MessageStore.messages);
    const disp = useAppDispatch();

    useEffect(() => {
        $api.get("http://localhost:8000/message", {
            params: {
                first_id: 1,
                second_id: 2,
                start: 1000,
            },
        }).then((response) => {
            disp(MessageSlice.actions.add([...response.data.messages]));
        });
    }, []);

    useEffect(() => {
        if (isOpen) {
            const elem = document.getElementById("Chat-Scroll");
            elem!.scrollTop = elem!.scrollHeight;
        }
    }, [messageList]);

    const OpenChat = (
        <>
            <div className="Chat-Scrollable" id="Chat-Scroll">
                <div className="ChatIns">
                    {messageList.length > 0
                        ? messageList.map((obj: IMessage, idx) => (
                              <Message
                                  key={idx}
                                  content={obj.content}
                                  isSender={true}
                              />
                          ))
                        : null}
                </div>
            </div>
            <Controller
                myUsername={myUsername}
                sendJsonMessage={sendJsonMessage}
            />
        </>
    );

    return <>{isOpen ? OpenChat : <></>}</>;
}

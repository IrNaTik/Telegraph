import React from "react";
import { Clist } from "./ChatList/Clist";
import { ChatIns } from "./Chat/Chat";

export default function Home(props: any) {
    return (
        <div className="Home-Wrapper">
            <div className="Home-Clist">
            <Clist></Clist>
            </div>
            <div className="Home-ChatIns">
                <ChatIns />

            </div>
        </div>
    )
}
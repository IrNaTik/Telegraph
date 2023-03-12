import React, { useState, useEffect } from "react";
import { Clist } from "./ChatList/Clist";
import { ChatIns } from "./Chat/Chat";
import SearchArea from "./Search/SearchArea";


export default function Home(props: any) {
    const url = window.location.href;
    console.log(url)
    const [friendUsername, setFriendUsername] = useState<string>()

    useEffect(() => {
        const url = window.location.href;
        const arr = url.split('/')
        const username = arr[arr.length-1]

        if (username) {
            // Get chat pagination or empty chat or redirect if user doesn't exist
            setFriendUsername(username)
        } 
    }, [])

    return (
        <div className="Home-Wrapper">
            <SearchArea/>
            <div className="Home-Clist">
            <Clist></Clist>
            </div>
            <div className="Home-ChatIns">
                <ChatIns />

            </div>
        </div>
    )
}
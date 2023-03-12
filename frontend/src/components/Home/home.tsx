import React, { useState, useEffect } from "react";
import { Clist } from "./ChatList/Clist";
import { ChatIns } from "./Chat/Chat";
import SearchArea from "./Search/SearchArea";
import { useNavigate } from "react-router";


export default function Home(props: any) {
    const navigate = useNavigate() 
    
    function changeHref(username: string) {
        navigate('/' + username)
    }

    return (
        <div className="Home-Wrapper">
            <SearchArea changeHref={ changeHref }/>
            <div className="Home-Clist">
            <Clist></Clist>
            </div>
            <div className="Home-ChatIns">
                <ChatIns />

            </div>
            
        </div>
    )
}
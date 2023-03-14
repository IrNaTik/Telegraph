import React, { useState, useEffect } from "react";
import { Clist } from "./ChatList/Clist";
import { ChatIns } from "./Chat/Chat";
import SearchArea from "./Search/SearchArea";
import { useNavigate } from "react-router";
import axios from "src/api/axios";


export default function Home(props: any) {
    const navigate = useNavigate() 
    
    function changeHref(username: string) {
        navigate('/' + username)

        axios.get('get-chat-with-user', {
            'headers': {
                'myUsername': 'Titan',
                'otherUsername': username
            }})
                .then(function (response) {
                    console.log(response)
                    // setGlobalUsers(response.data)
                });

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
import { Clist } from "../components/Home/ChatList/Clist";
import { ChatIns } from "../components/Home/Chat/Chat";
import SearchArea from "../components/Home/Search/SearchArea";
import { useNavigate } from "react-router";
import axios from "src/utils/api/axios";
import { useState } from "react";

import useWebSocket from 'react-use-websocket'
import MessageSlice from "src/store/messsages";
import { useAppDispatch } from "src/store/store";


export default function Home({ myUsername }: any) {
    const dispatch = useAppDispatch()
    const navigate = useNavigate() 
    const [getterUsername, setGetterUsername] = useState('')

    const WS_URL = 'ws://localhost:8000/ws/chat/' // Подключение к сокету
    

    const { sendJsonMessage } = useWebSocket(decodeURI(WS_URL) + "?username=" + myUsername, {
        // onOpen: () => {

        //     const arr = window.location.href.split('/')
        //     const last = arr.length - 1
            
        //     if (arr[last]) {
        //         console.log('good')
                
        //         setGetterUsername(arr[last])
        //         sendJsonMessage({
        //             'type': 'chatBegin',
        //             'personUsername': arr[last],
        //             'myUsername': myUsername // Здесь должны быть данные из storage
        //         })
                
        //     } else {
        //         console.log('User is not choosen')
        //     }
                
            

        // }
        // ,
        onMessage: (response) => {
          const data = JSON.parse(response.data) 
          console.log(data)
          if (data.type === "message"){
            dispatch(MessageSlice.actions.add({'username': data.senderUsername, 'message': data.message} ))
          }
          
        }
      });
    
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
            
            <div className="Home-Clist">
                <SearchArea changeHref={ changeHref }/>
                <Clist></Clist>
            </div>
            <div className="Home-ChatIns">
                <ChatIns myUsername = { myUsername } sendJsonMessage={ sendJsonMessage }/>
            </div>
            
        </div>
    )
}
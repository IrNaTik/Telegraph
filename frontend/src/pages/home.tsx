import { Clist } from "../components/Home/ChatList/Clist";
import { ChatIns } from "../components/Home/Chat/Chat";
import SearchArea from "../components/Home/Search/SearchArea";
import { useNavigate } from "react-router";
import axios from "src/utils/api/axios";


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
            
            <div className="Home-Clist">
                <SearchArea changeHref={ changeHref }/>
                <Clist></Clist>
            </div>
            <div className="Home-ChatIns">
                <ChatIns />
            </div>
            
        </div>
    )
}
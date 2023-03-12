import { set } from "immer/dist/internal";
import React, { useState, useEffect } from "react";
import axios from "src/api/axios";
import { Navigate } from "react-router";

export default function SearchArea(props: any) {
    const [prefix, setPrefix] = useState('')
    const [globalUsers, setGlobalUsers] = useState<Array<string>>([])
    const [navigate, setNavigate] = useState<any>()

    useEffect(()=> {
        if (prefix.length >= 4) {
            axios.get('users-by-prefix', {
                'headers': {
                    'prefix': prefix
                }})
                    .then(function (response) {
                    
                        setGlobalUsers(response.data)
                    });
        } else {
            setGlobalUsers([])
        }
    }, [prefix])

    function handleChange(e: any){
        setPrefix(e.target.value)
    }

    function openChat( idx: number){
        setNavigate( <Navigate to={"/" + globalUsers[idx]} replace={false} />)
    }
    return (
        <div className="Area-Wrapper">
            <input className='input-area' onChange={handleChange} value={ prefix }></input>
            <div className="global-userlist" >
                {
                    globalUsers.map((username, idx) =>{
                        return <div key={idx} onClick={e => openChat(idx)}>{ username }</div>
                    })
                }
            </div>
            {
                navigate
            }
        </div>
    )
}
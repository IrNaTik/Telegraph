import React, { useState, useEffect, memo } from "react";
import $api from "src/utils/api/axios";
import { useAppSelector } from "src/store/store";


interface PropsInterface {
    changeHref: Function
}

function SearchArea({ changeHref }: PropsInterface) {
    const [prefix, setPrefix] = useState('')
    const [globalUsers, setGlobalUsers] = useState<Array<string>>([])
    const [navigate, setNavigate] = useState<any>()

    useEffect(()=> {
        if (prefix.length >= 4) {

            $api.get('users-by-prefix', {
                'headers': {
                    'prefix': prefix
                }})
            .catch((error) => {
                console.log(error)
            })
            .then(function (response) {
                console.log(response)
                if (response) {
                    setGlobalUsers(response.data)
                }
                // 
            });
        } else {
            setGlobalUsers([])
        }
    }, [prefix])

    function handleChange(e: any){
        setPrefix(e.target.value)
    }

    function openChat( idx: number){
        changeHref(globalUsers[idx])
        // setNavigate( <Navigate to={"/" + globalUsers[idx]} replace={false} />)
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

export default memo(SearchArea);
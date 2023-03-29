import React, { useEffect } from "react";
import {  useNavigate } from "react-router";
import Form from "../components/Auth/form/form";
import { useAppSelector } from "src/store/store";


export default function Auth(props: any) {
    const navigate = useNavigate()
    const isAuth = useAppSelector(state=> state.UserStore.isAuth)
    
    useEffect(() => {
        if (isAuth) {
            navigate('/chats')
        }
    }, [isAuth]) 

    return(
        <div className="Auth">
            <div className="Auth-Placeholder"></div>
            <Form></Form>
        </div>
        
    )
}
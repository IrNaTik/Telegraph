import React, { useEffect } from "react";
import { Navigate, useNavigate } from "react-router";

import Form from "./form/form";
import { useAppSelector } from 'src/store/store';
import axios from "src/api/axios";


export default function Auth(props: any) {
    const navigate = useNavigate()
    const Atoken = useAppSelector(state => state.TokenStore.Atoken)
    
    useEffect (() => {

        axios.get('login', {
            'headers': {
                'Authorization': `Bearer ${Atoken}`
            }
        }).then((responce) => {
            console.log(responce.status)
            if (responce.status === 200) {
                // navigate('/')
                console.log('register')
            }
        })
    },[])

    return(
        <div className="Auth">
            <div className="Auth-Placeholder"></div>
            <Form></Form>
        </div>
    )
}
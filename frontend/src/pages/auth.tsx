import React, { useEffect } from "react";
import {  useNavigate } from "react-router";

import Form from "../components/Auth/form/form";

import $api from "src/utils/api/axios";


export default function Auth(props: any) {
    const navigate = useNavigate()
    // const Atoken = useAppSelector(state => state.TokenStore.Atoken)
    
    useEffect (() => {

        $api.get('login',)
        .then((responce) => {
            if (responce.status === 200) {
                navigate('/')
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
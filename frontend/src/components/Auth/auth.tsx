import React, { useEffect } from "react";

import Form from "./form/form";
import { useAppSelector } from 'src/store/store';
import axios from "src/api/axios";


export default function Auth(props: any) {
    const Atoken = useAppSelector(state => state.TokenStore.Atoken)
    
    useEffect (() => {

        axios.get('login/', {
            'headers': {
                'Authorization': `Bearer ${Atoken}`
            }
        }).then(() => {
            console.log("GET")
        })
    },[])
    return(
        <Form></Form>
    )
}
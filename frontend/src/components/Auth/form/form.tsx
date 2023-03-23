import React, { useRef, useState } from "react";
import axios from "axios";

import Logo from "src/components/common/logo/logo";
import $api from "src/utils/api/axios";
import { NavLink } from "react-router-dom";
import { CHATS_ROUTE } from "src/utils/consts";

interface LoginForm {
    login: string,
    password: string
}


export default function Form(props: any) {
    const inpRef = useRef<HTMLInputElement>(null)
    const inpRef1 = useRef<HTMLInputElement>(null)
    const [form, setForm] = useState<LoginForm>({
        login: "",
        password: ""
    })

    function handleForm(e: React.ChangeEvent<HTMLInputElement>) {
        setForm({ ...form, 
            [e.target.name]: e.target.value
        })
    }

    function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault()
        
        console.log(form)
        $api.post('http://localhost:8000/login', {data: form})
        .then((response) => {
            
            localStorage.setItem('token', response.data.AssesToken)
        })
        .catch((error) => {
            console.log('Error')
        })
       
        setForm({
            login: '',
            password: ''
        })
        
        inpRef.current!.value = ''
        inpRef1.current!.value = ''
    }

    return (
        <div className="Form">
            <form onSubmit={handleSubmit} className="Auth-Form">
                <Logo></Logo>
                <h4 className="Header-Form">Sing in to Telegraf</h4>
                <p className="Title-Form">Please enter you login and password</p> 
                <input className="Input-Form" type="text" name="login" placeholder="Login" onChange={handleForm} ref={inpRef}/>  

                <input className="Input-Form" type="password" name="password"  placeholder="password" onChange={handleForm} ref={inpRef1} />
                <input className="Submit-Form" type="submit" value="Sign In" />
                <NavLink to={CHATS_ROUTE} className="Link-Form"> Forgot Passord</NavLink>
            </form>
        </div>
    )
} 
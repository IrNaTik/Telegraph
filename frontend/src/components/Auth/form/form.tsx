import React, { useState } from "react";
import axios from 'src/api/axios';

import { useAppDispatch } from "src/store/store";
import { update } from "src/store/tokens";

import Logo from "src/common/logo/logo";

interface LoginForm {
    login: string,
    password: string
}

export default function Form(props: any) {
    const dispatch = useAppDispatch()
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
        
        axios.post('/login', form)
        .then((response) => {
            const AssessToken = response.data.AssesToken
            dispatch(update(AssessToken)) 
        })
    }

    return (
        <div className="Form">
            <form onSubmit={handleSubmit} className="Auth-Form">
                <Logo></Logo>
                <h4 className="Header-Form">Sing in to Telegraf</h4>
                <p className="Title-Form">Please enter you login and password</p> 
                <input className="Input-Form" type="text" name="login" placeholder="Login" onChange={handleForm}/>  

                <input className="Input-Form" type="password" name="password"  placeholder="password" onChange={handleForm}/>
                <input className="Submit-Form" type="submit" value="Sign In" />
                <a className="Link-Form"  href="#">Forgot Passord</a>
            </form>
        </div>
    )
} 
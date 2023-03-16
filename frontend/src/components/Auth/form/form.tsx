import React, { useRef, useState } from "react";
import axios from "axios";

import Logo from "src/components/common/logo/logo";
import $api from "src/api/axios";

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
        
        $api.post('http://localhost:8000/login', form)
        .then((response) => {
            localStorage.setItem('token', response.data.AssesToken)
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
                <a className="Link-Form"  href="#">Forgot Passord</a>
            </form>
        </div>
    )
} 
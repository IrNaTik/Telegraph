import React, { useState } from "react";
import axios from '../../../api/axios';

import { useAppDispatch } from "src/store/store";
import { update } from "src/store/tokens";

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
                <p>Welcome</p> 
                <input type="text" name="login" placeholder="Login" onChange={handleForm}/> {// set for email
                }
                <input type="password" name="password"  placeholder="password" onChange={handleForm}/>
                <input type="submit" value="Sign In" />
                <a href="#">Forgot Passord</a>
            </form>
        </div>
    )
}
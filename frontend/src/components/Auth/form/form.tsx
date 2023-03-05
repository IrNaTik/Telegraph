import React, { useEffect, useState } from "react";
import axios from '../../../api/axios';
import { useAppSelector } from "../../../store/store";

interface LoginForm {
    login: string,
    password: string
}

export default function Form(props: any) {
    const Atoken = useAppSelector(state => state.TokenStore.Atoken)
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
<<<<<<< HEAD
        console.log("asd")
        console.log(Atoken);
        axios.post(`${host}/login`, form, {
=======

        setForm({'login': '',
                'password': ''})
        
        axios.post('/login', form, {
>>>>>>> 1fde46b97935ba570dcf07b87b75183e855f6ac1
            headers: {
                "Authorization": `Bearer ${Atoken}`,
            },
            withCredentials: true
        } )
    }

    useEffect(() => {
        axios.get('/login')

        
        .then((response) => {
            
              // check tokens
        })
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

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
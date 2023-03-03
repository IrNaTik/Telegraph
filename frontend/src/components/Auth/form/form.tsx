import React, { useEffect, useState } from "react";
import axios from "axios";
import { useAppSelector } from "../../../store/store";

interface LoginForm {
    login: string,
    password: string
}

export default function Form(props: any) {
    const host = useAppSelector(state => state.HostStore.host)
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
        console.log("asd")
        axios.post(`${host}/login`, form, {
            headers: {
                "Authorization": `Bearer ${Atoken}`
            } 
        } )
    }

    useEffect(() => {
        axios.get(`${host}/login`)
        .then((response) => {
            console.log(response)  // check tokens
        })
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    return (
        <div className="Auth-Form">
            <form onSubmit={handleSubmit}>
                <p>Welcome</p>
                <input type="email" name="login" placeholder="Login" onChange={handleForm}/>
                <input type="password" name="password"  placeholder="password" onChange={handleForm}/>
                <input type="submit" value="Sign In" />
                <a href="#">Forgot Passord</a>
            </form>
        </div>
    )
}
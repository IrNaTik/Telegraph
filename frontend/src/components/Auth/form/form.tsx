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
        
        
        axios.post('/login', form, {
            // headers: {
            //     "Authorization": `Bearer ${Atoken}`,
            // },
            withCredentials: true
        })
        .then((response) => {
            const AssessToken = response.data.AssesToken
            console.log(AssessToken)
            localStorage.setItem('AssessToken', AssessToken)
        })

        
    }
    
    useEffect(() => {

        const AssessToken = localStorage.getItem('AssessToken')
        axios.get('/login', {headers: {'content-Type': 'application/json', 'Cookie': document.cookie, 'AssessToken': AssessToken },
                            withCredentials: true})

        
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
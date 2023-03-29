import React, { useRef, useState } from "react";

import Logo from "src/components/common/logo/logo";
import $api from "src/utils/api/axios";
import { NavLink } from "react-router-dom";
import { CHATS_ROUTE } from "src/utils/consts";
import { useAppDispatch } from "src/store/store";
import { setUsername, update } from "src/store/Auth";

interface LoginForm {
    login: string,
    password: string
}


export default function Form(props: any) {
    const inpRef = useRef<HTMLInputElement>(null)
    const inpRef1 = useRef<HTMLInputElement>(null)
    const [isValid, setIsValid] = useState(false)
    const [form, setForm] = useState<LoginForm>({
        login: "",
        password: ""
    })
    const disp = useAppDispatch()

    function handleForm(e: React.ChangeEvent<HTMLInputElement>) {
        

        if (e.target.name === 'login') {
   
            if (form.login.length < 8) {
                inpRef.current!.classList.add('Input-MinLenght')
             }else {
                setIsValid(true)
                inpRef.current!.classList.remove('Input-MinLenght')
            }
        } 

        if (e.target.name === 'password') {

            if (form.password.length < 4) {
                inpRef1.current!.classList.add('Input-MinLenght')
            }else if (form.password.length < 7) {
                inpRef1.current!.classList.add('Input-MiddleLevel')
            }else {
                inpRef1.current!.classList.add('Input-HighLevel')
                inpRef1.current!.classList.remove('Input-MinLenght')
            }
        } 
        

        setForm({ ...form, 
            [e.target.name]: e.target.value
        })
    }

    function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault()

        if (isValid) {

            $api.post('http://localhost:8000/login', form)
            .then((response) => {
                localStorage.setItem('token', response.data.AssesToken)
            })
            disp(update())
            disp(setUsername(form.login))

            setForm({
                login: '',
                password: ''
            })
            
            inpRef.current!.value = ''
            inpRef1.current!.value = ''

            inpRef1.current?.classList.remove('Input-HighLevel')
        }        
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
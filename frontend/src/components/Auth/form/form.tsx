import React, { useEffect } from "react";
import axios from "axios";

export default function Form(props: any) {

    useEffect(() => {
        axios.get('http://localhost:8000/login')
        .then((response) => {
            console.log(response)
        })
    }, [])

    return (
        <div>Form</div>
    )
}
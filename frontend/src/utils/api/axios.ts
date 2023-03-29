import axios from "axios";
import { useEffect } from "react";
import UserSlice from "src/store/Auth";


const $api = axios.create({
    baseURL: "http://localhost:8000/",
    withCredentials: true
}) 

$api.interceptors.request.use( config => {
    config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
    return config
})

$api.interceptors.response.use(config => {
    return config
}, (error => {

    if (error.response.status === 401) {
        $api.post('/api/refresh')
        .then(resp => {
            
            if (resp) {
                console.log('Tokens has been updated')
                localStorage.setItem('token', resp.data.AssesToken)
                return $api.request(error.config)
            }     
        })
    } 
}))

export default $api;
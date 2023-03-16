import axios from "axios";


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
            localStorage.setItem('token', resp.data.AssesToken)
            return $api.request(error.config)
        })
    } 
}))

export default $api;
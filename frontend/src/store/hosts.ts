import { createSlice } from "@reduxjs/toolkit";


const HostSlice = createSlice({
    name: "hosts",
    initialState: {
        host: "http://localhost:8000"
    },
    reducers: {}
})

export default HostSlice;
import { createSlice } from "@reduxjs/toolkit";

const initialState =  {
    Atoken: '',
}

 const tokenSlice = createSlice({
    name: 'tokens',
    initialState,
    reducers: {
        update(state) {
            state.Atoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2Nzc4NjE4MDF9.OErNNP2fNDGWXrCiVdipFlzdj23cex5sP0KUQrLdxh8"
        }
    }

})

export default tokenSlice
export  const {update} = tokenSlice.actions
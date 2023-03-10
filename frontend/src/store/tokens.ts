import { createSlice } from "@reduxjs/toolkit";

const initialState =  {
    Atoken: '',
}

 const tokenSlice = createSlice({
    name: 'tokens',
    initialState,
    reducers: {
        update(state, actions) {
            state.Atoken = actions.payload
        }
    }

})

export default tokenSlice
export  const {update} = tokenSlice.actions
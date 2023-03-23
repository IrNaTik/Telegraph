import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    isAuth: true
}

const UserSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        update(state) {
            state.isAuth = !state.isAuth
        }
    }
})

export default UserSlice;
export const {update} = UserSlice.actions
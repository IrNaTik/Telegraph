import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    isAuth: true,
    username: 'dd'
}

const UserSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        update(state) {
            state.isAuth = !state.isAuth
        },
        setUsername(state, actions) {
            state.username = actions.payload
        }
    }
})

export default UserSlice;
export const {update, setUsername} = UserSlice.actions

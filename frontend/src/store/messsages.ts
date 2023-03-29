import  { createSlice } from '@reduxjs/toolkit';

const initialState = {
    messages: ['']
}

const MessageSlice = createSlice({
    name: 'messages',
    initialState,
    reducers: {
        add(state, actions) {
            console.log(actions.payload)
            state.messages.push(actions.payload.username + ': ', actions.payload.message)
        }
    }
})

export default MessageSlice;
export const  {add} = MessageSlice.actions
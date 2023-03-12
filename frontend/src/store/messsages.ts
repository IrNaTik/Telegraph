import  { createSlice } from '@reduxjs/toolkit';

const initialState = {
    messages: ['']
}

const MessageSlice = createSlice({
    name: 'messages',
    initialState,
    reducers: {
        add(state, actions) {
            state.messages.push(actions.payload)
        }
    }
})

export default MessageSlice;
export const  {add} = MessageSlice.actions
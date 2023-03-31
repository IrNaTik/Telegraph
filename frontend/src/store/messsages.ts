import  { createSlice } from '@reduxjs/toolkit';

export interface IMessage {
    sender_id: number;
    content: string;
    date: string;
    is_readen: string;
}


const initialState = {
    messages: [
    {} as IMessage
    ] 
}

const MessageSlice = createSlice({
    name: 'messages',
    initialState,
    reducers: {
        add(state, actions) {
            state.messages.push(...actions.payload)
        }
   }
})

export default MessageSlice;
export const  {add} = MessageSlice.actions
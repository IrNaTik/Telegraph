import {createSlice} from '@reduxjs/toolkit';

const initialState = {
    isOpen: false
}

const ChatSlice = createSlice({
    name: 'chatIns',
    initialState,
    reducers: {
        updateOpen(state) {
            state.isOpen = !state.isOpen
        }
    }
})

export default ChatSlice;
export const {updateOpen} = ChatSlice.actions

 
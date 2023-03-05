import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { useDispatch } from "react-redux";
import { useSelector, TypedUseSelectorHook } from "react-redux";
import HostSlice from "./hosts";
import tokenSlice from "./tokens";


const rootReducer = combineReducers({
    TokenStore: tokenSlice.reducer,
    HostStore: HostSlice.reducer
})

export const store = configureStore({
    reducer: rootReducer
})
export type RootState = ReturnType<typeof store.getState>

export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
export const useAppDispatch: () => typeof store.dispatch = useDispatch
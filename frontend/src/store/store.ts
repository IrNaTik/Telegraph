import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { useDispatch } from "react-redux";
import { useSelector, TypedUseSelectorHook } from "react-redux";


import { 
    persistStore,
    persistReducer,
    FLUSH,
    REHYDRATE,
    PAUSE,
    PERSIST,
    PURGE,
    REGISTER, } from "redux-persist";
import storage from "redux-persist/lib/storage";

import tokenSlice from "./tokens";
import MessageSlice from "./messsages";

const rootReducer = combineReducers({
    TokenStore: tokenSlice.reducer,
    MessageStore: MessageSlice.reducer
})

const persistConfig = {
    key: 'root',
    storage: storage,
    whitelist: ['TokenStore']
}

const PersistReducer = persistReducer(persistConfig, rootReducer)

const store = configureStore({
        reducer: PersistReducer,
        middleware: (getDefaultMiddleware) =>
            getDefaultMiddleware({
            serializableCheck: {
                ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
            },
        
        }),
})

export const persistor = persistStore(store) 
export default store;

export type RootState = ReturnType<typeof store.getState>

export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
export const useAppDispatch: () => typeof store.dispatch = useDispatch
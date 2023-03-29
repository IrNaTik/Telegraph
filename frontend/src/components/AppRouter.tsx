import { ReactNode, useState, useEffect } from "react";
import {Routes, Route} from "react-router-dom";
import { authRoutes, publicRoutes } from "src/routes";
import { useAppSelector } from "src/store/store";

export const AppRouter = () => {
    const isAuth = useAppSelector(state=> state.UserStore.isAuth)
    const [myUsername, setMyUsername] = useState('Ignat')

    // function handleChange(e: any) {
    //     setMyUsername(e.target.value)
    // }
    return (
        <>
        {/* <input style={{height: "50px"}} type="text" value={ myUsername } onChange={e => handleChange(e)}/> */}
        <Routes>
            {isAuth ? authRoutes.map(({path, Component}) => 
                <Route key={path} path={path + ":username?"} element={<Component myUsername={ 'Ignat' }/>} ></Route>
            )
            :
            publicRoutes.map(({path, Component}) => 
                <Route key={path} path={path} element={<Component/>} ></Route>    
            )}
        </Routes>
        </>
    )
}
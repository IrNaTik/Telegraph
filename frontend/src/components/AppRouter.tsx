import { ReactNode } from "react";
import {Routes, Route} from "react-router-dom";
import { authRoutes, publicRoutes } from "src/routes";
import { useAppSelector } from "src/store/store";

export const AppRouter = () => {
    const isAuth = useAppSelector(state=> state.UserStore.isAuth)

    return (
        <Routes>
            {isAuth ? authRoutes.map(({path, Component}) => 
                <Route key={path} path={path} element={<Component/>} ></Route>
            )
            :
            publicRoutes.map(({path, Component}) => 
                <Route key={path} path={path} element={<Component/>} ></Route>    
            )}
        </Routes>
    )
}
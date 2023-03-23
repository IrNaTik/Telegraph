import { ReactNode } from "react";
import {Routes, Route} from "react-router-dom";
import { authRoutes, publicRoutes } from "src/routes";
import Auth from "src/pages/auth";

interface PropsInt{
    path?: string;
    Component?: ReactNode
}

export const AppRouter = () => {
    const isAuth = true

    return (
        <Routes>
            {isAuth && authRoutes.map(({path, Component}) => 
                <Route key={path} path={path} element={<Component />} ></Route>
            )}
            {publicRoutes.map(({path, Component}) => 
                <Route key={path} path={path} element={<Component />}></Route>    
            )}
        </Routes>
    )
}
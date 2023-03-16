import {Routes, Route} from "react-router-dom";
import { authRoutes, publicRoutes } from "src/routes";

export const AppRouter = () => {
    const isAuth = true

    return (
        <Routes>
            {isAuth && authRoutes.map(({path, Component}) => 
                <Route key={path} path={path} Component={Component} ></Route>
            )}
            {publicRoutes.map(({path, Component}) => 
                <Route key={path} path={path} Component={Component}></Route>    
            )}
        </Routes>
    )
}
import Auth from "./pages/auth";
import Home from "./pages/home";
import { CHATS_ROUTE, LOGIN_ROUTE } from "./utils/consts";

export const publicRoutes = [
    {
        path: LOGIN_ROUTE,
        Component: Auth
    }
]

export const authRoutes = [
    {
        path: CHATS_ROUTE,
        Component: Home
    }
]
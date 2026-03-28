import {BrowserRouter , Route , Routes} from "react-router-dom";

import Home from "./pages/Home";
import LoginPage from "./pages/account/Login";


const MainRoutes = ()=>{
    return (
        <BrowserRouter>
            <Routes>
                <Route path="" element={<Home/>} />
                <Route path="account/login/" element={<LoginPage/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default MainRoutes;
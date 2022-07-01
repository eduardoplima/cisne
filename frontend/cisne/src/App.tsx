import React from 'react';
import AuthenticationPage from './pages/authentication';
import MainPage from './pages/mainpage';

import { selectAuth } from "./features/auth/authSlice";
import { store, RootState } from './app/store';
import { CombinedState } from '@reduxjs/toolkit';
import { useNavigate } from 'react-router-dom';

function App() {
    const auth: CombinedState<any> = selectAuth(store.getState());
    let navigate = useNavigate();

    if (!auth.token) {
        navigate("/login", { replace: true });
    }

    return (<MainPage />);  

}

export default App;

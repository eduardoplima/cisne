import { createSlice } from '@reduxjs/toolkit';
import { RootState } from '../../app/store';

const initialState = {
    token: localStorage.getItem('cisneToken'),
    //tokenRefresh: localStorage.getItem('tokenRefresh'),
    username: localStorage.getItem('cisneUsername'),
    firstName: localStorage.getItem('cisneFirstName'),
    lastName: localStorage.getItem('cisneLastName')
};

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        authInsert: (state, action) => {
            const user = action.payload;

            state.token = user.access;
            //state.tokenRefresh = user.refresh;
            state.username = user.username;
            state.firstName = user.first_name;
            state.lastName = user.last_name;

            localStorage.setItem('cisneToken', user.access);
            localStorage.setItem('tokenRefresh', user.refresh);
            localStorage.setItem('cisneUsername', user.username);
            localStorage.setItem('cisneFirstname', user.first_name);
            localStorage.setItem('cisneLastname', user.last_name);
        },
        authRemove: (state) => {
            localStorage.removeItem('cisneToken');
            localStorage.removeItem('tokenRefresh');
            localStorage.removeItem('cisneUsername');
            localStorage.removeItem('cisneFirstname');
            localStorage.removeItem('cisneLastname');

            state.token = null;
            //state.tokenRefresh = null;
            state.username = '';
            state.firstName = '';
            state.lastName = '';
        }
    }
});

export const { authInsert, authRemove } = authSlice.actions;

export const selectAuth = (state: RootState) => state.auth;

export default authSlice.reducer;

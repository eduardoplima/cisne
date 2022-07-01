import {
    render,
    screen,
    fireEvent,
    waitFor,
    cleanup,
    prettyDOM
} from '@testing-library/react';
import { Provider } from 'react-redux';
import { store } from '../../app/store';

import AuthenticationPage from './AuthenticationPage';

import { BrowserRouter as Router } from 'react-router-dom';
import userEvent from '@testing-library/user-event';

afterEach(cleanup);

describe('AuthenticationPage', () => {
    it('should render successfully', () => {
        const { baseElement } = render(
            <Router>
                <Provider store={store}>
                    <AuthenticationPage />
                </Provider>
            </Router>
        );

        expect(baseElement).toBeTruthy();
        expect(screen.getByLabelText(/Username-field/i)).toBeTruthy();
        expect(screen.getByLabelText(/Password-field/i)).toBeTruthy();
        expect(screen.getByRole('button', { name: /Login/i })).toBeTruthy();
        expect(screen.getByRole('button', { name: /Sign/i })).toBeTruthy();
    });

    it('should login with correct username and password', async () => {
        render(
            <Router>
                <Provider store={store}>
                    <AuthenticationPage />
                </Provider>
            </Router>
        );

        const userField = screen.getByLabelText(/Username-field/i);
        const passField = screen.getByLabelText(/Password-field/i);

        const username = process.env.TEST_USER;
        const password = process.env.TEST_PASSWORD;

        console.log(username);
        console.log(password);

        const user = userEvent.setup();

        
        fireEvent.change(userField, { target: { value: username! } });
        fireEvent.change(passField, { target: { value: password! } });
        user.click(screen.getByLabelText(/Login/i));

        console.log(store.getState());

        expect(store.getState().auth.token).toBeTruthy();
    });

    /*it('should show error with wrong username and password', async () => {
        render(
            <Router>
                <Provider store={store}>
                    <AuthenticationPage />
                </Provider>
            </Router>
        );

        const userField = screen.getByLabelText(/Username-field/i);
        const passField = screen.getByLabelText(/Password-field/i);

        fireEvent.change(userField, { target: { value: 'test' } });
        fireEvent.change(passField, { target: { value: 'test' } });

        const submitButton = screen.getByRole('button', { name: /Login/i });
        fireEvent.click(submitButton);

        await waitFor(() => {
            expect(screen.getByText(/error/i)).toBeTruthy();
        });
    });*/

    
});

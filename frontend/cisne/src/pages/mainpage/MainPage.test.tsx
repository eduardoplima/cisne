import MainPage from './MainPage';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import { store } from '../../app/store';
import { BrowserRouter } from 'react-router-dom';
//import { createMockStore } from 'redux-test-utils';

describe('MainPage', () => {
    it('should render successfully', () => {
        const { baseElement } = render(
            <BrowserRouter>
                <Provider store={store}>
                    <MainPage />
                </Provider>
            </BrowserRouter>
        );
        expect(baseElement).toBeTruthy();
        expect(screen.getByText('MainPage')).toBeTruthy();
    });

    /*it('should login', async () => {
        expect(process.env.TEST_USER).toBeTruthy();
        expect(process.env.TEST_PASSWORD).toBeTruthy();

        const store = createMockStore("");

        render(
            <Provider store={store}>
                <MainPage />
            </Provider>
        );

        const inputTextField = screen.getByLabelText('Username');
        const passwordTextField = screen.getByLabelText('Password');
        const loginButton = screen.getByRole('button', { name: /Login/i });

        fireEvent.change(inputTextField, { target: { value: process.env.TEST_USER } });
        fireEvent.change(passwordTextField, { target: { value: process.env.TEST_PASSWORD } });
        fireEvent.click(loginButton);

        await waitFor(() => {
            expect(screen.getByRole('button', { name: /Logout/i })).toBeTruthy();
        });
    });*/
});

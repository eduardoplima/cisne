import React, { BaseSyntheticEvent, useEffect, useRef } from 'react';
import { useAppDispatch } from '../../app/hooks';
import { authInsert } from '../../features/auth/authSlice';
import { useTokenAuthMutation } from '../../features/api/apiSlice';
import { useForm } from 'react-hook-form';
import { useTranslation } from 'react-i18next';
import { useNavigate } from 'react-router-dom';

import { MessageBar, MessageBarHandle } from '../../components/message';
import { Button, Grid, TextField } from '@mui/material';

import {
    isErrorWithMessage,
    isFetchBaseQueryError
} from '../../services/helpers';
import { isEmpty } from 'lodash';

type AuthFormData = {
    username: string;
    password: string;
};

const AuthenticationPage = () => {
    const dispatch = useAppDispatch();
    const [authenticate] = useTokenAuthMutation();
    const {
        register,
        setValue,
        handleSubmit,
        formState: { errors: formErrors }
    } = useForm<AuthFormData>();
    const navigate = useNavigate();

    const { t } = useTranslation();

    const messageBarRef = useRef<MessageBarHandle>(null);

    const handleLogin = async (data: AuthFormData) => {
        try {
            const resultAuthenticate: any = await authenticate({
                username: data.username,
                password: data.password
            });
            if ('error' in resultAuthenticate) {
                console.log(resultAuthenticate.error);
                messageBarRef.current?.errorSnack(
                    t('authentication.errors.login')
                );
            } else {
                dispatch(
                    authInsert({
                        payload: {
                            username: resultAuthenticate.data.username,
                            token: resultAuthenticate.data.token,
                            firstName: resultAuthenticate.data.first_name,
                            lastName: resultAuthenticate.data.last_name
                        }
                    })
                );
                navigate('/home', { replace: true });
            }
        } catch (err) {
            if (isFetchBaseQueryError(err)) {
                if (isFetchBaseQueryError(err)) {
                    const errMsg =
                        'error' in err ? err.error : JSON.stringify(err.data);
                    messageBarRef.current?.errorSnack(errMsg);
                } else if (isErrorWithMessage(err)) {
                    messageBarRef.current?.errorSnack((err as any).message);
                }
            }
        }
    };

    useEffect(() => {
        if (!isEmpty(formErrors)) {
            console.log(formErrors);
            messageBarRef.current?.errorSnack(t('authentication.errors.login'));
            formErrors.username &&
                formErrors.username.type === 'required' &&
                messageBarRef.current?.errorSnack(
                    t('authentication.errors.required.username')
                );
            formErrors.password &&
                formErrors.password.type === 'required' &&
                messageBarRef.current?.errorSnack(
                    t('authentication.errors.required.password')
                );
        }
    }, [formErrors, t]);

    const onSubmit = (data: AuthFormData, e: BaseSyntheticEvent) => {
        e.preventDefault();
        handleLogin(data);
    };

    return (
        <>
            <form onSubmit={handleSubmit((data, e) => onSubmit(data, e!))}>
                <Grid container direction="column">
                    <Grid item>
                        <TextField
                            inputProps={{ 'aria-label': 'username-field' }}
                            label={t('authentication.username')}
                            id="username"
                            aria-label="username"
                            variant="standard"
                            {...register('username', { required: true })}
                        />
                    </Grid>
                    <Grid item>
                        <TextField
                            inputProps={{ 'aria-label': 'password-field' }}
                            type="password"
                            label={t('authentication.password')}
                            id="password"
                            aria-label="password"
                            variant="standard"
                            {...register('password', { required: true })}
                        />
                    </Grid>

                    <Grid container>
                        <Grid item>
                            <Button
                                variant="contained"
                                color="primary"
                                type="submit"
                                aria-controls="login"
                                aria-label="login"
                            >
                                {t('authentication.login')}
                            </Button>
                        </Grid>
                        <Grid item>
                            <Button
                                variant="contained"
                                color="secondary"
                                aria-controls="signup"
                                aria-label="signup"
                            >
                                {t('authentication.signup')}
                            </Button>
                        </Grid>
                    </Grid>
                </Grid>
            </form>
            <MessageBar ref={messageBarRef} />
        </>
    );
};

export default AuthenticationPage;

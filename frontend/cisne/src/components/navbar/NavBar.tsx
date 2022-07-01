import React from 'react';
import { AppBar, Button, Grid, Toolbar } from '@mui/material';
import { MenuOutlined } from '@mui/icons-material';
import { LogoutOutlined } from '@mui/icons-material';

import { authRemove } from '../../features/auth/authSlice';
import { useAppDispatch } from '../../app/hooks';

import { useTranslation } from 'react-i18next';

import { useNavigate } from 'react-router-dom';

const NavBar = () => {
    const dispatch = useAppDispatch();
    const navigate = useNavigate();
    const { t } = useTranslation();

    const handleLogout = () => {
        dispatch(authRemove());
        navigate('/login', { replace: true });
    };

    return (
        <AppBar position="static">
            <Toolbar variant="dense">
                <Grid
                    container
                    alignItems="center"
                    justifyContent="space-between"
                    direction="row"
                >
                    <Grid item md xs>
                        <Button
                            color="inherit"
                            aria-controls="simple-menu"
                            aria-haspopup="true"
                        >
                            <MenuOutlined />
                        </Button>
                    </Grid>
                    <Grid item md={10} xs={6}>
                        <h2>CISNE - Risk Management</h2>
                    </Grid>
                    <Grid item md xs>
                        <Button
                            color="inherit"
                            aria-label={t('authentication.logout')}
                            aria-controls="logout"
                            onClick={() => handleLogout()}
                        >
                            <LogoutOutlined />
                        </Button>
                    </Grid>
                </Grid>
            </Toolbar>
        </AppBar>
    );
};

export default NavBar;

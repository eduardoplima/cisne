import { Toolbar, Typography } from '@mui/material';
import { useTranslation } from 'react-i18next';
//import React from 'react'

const Footer = () => {
    const { t } = useTranslation();
    return (
        <>
            <Toolbar variant="dense"></Toolbar>
            <footer>
                <Typography>
                    {t("footer.copyright")}
                    <br/>
                </Typography>
            </footer>
        </>
    );
};

export default Footer;

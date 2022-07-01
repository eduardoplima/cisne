import React, { forwardRef, useImperativeHandle, useState } from 'react';

import Snackbar from '@mui/material/Snackbar';
import Alert, { AlertColor } from '@mui/material/Alert';

export type MessageBarHandle = {
    errorSnack: (msg: string) => void;
    successSnack: (msg: string) => void;
};

export type MessageBarProps = {};

const MessageBar = forwardRef<MessageBarHandle, MessageBarProps>(
    (props, ref) => {
        const [open, setOpen] = useState(false);
        const [message, setMessage] = useState('');
        const [severity, setSeverity] = useState<AlertColor>('success');

        const handleCloseSnackBar = () => {
            setOpen(false);
            setMessage('');
        };

        const errorSnack = (msg: string) => {
            setOpen(true);
            setMessage(msg);
            setSeverity('error');
        };

        const successSnack = (msg: string) => {
            setOpen(true);
            setMessage(msg);
            setSeverity('success');
        };

        useImperativeHandle(ref, () => ({ errorSnack, successSnack }));

        return (
            <Snackbar
                open={open}
                autoHideDuration={6000}
                onClose={handleCloseSnackBar}
                anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
            >
                <Alert
                    onClose={handleCloseSnackBar}
                    severity={severity}
                    key="al1"
                >
                    {message}
                </Alert>
            </Snackbar>
        );
    }
);

export { MessageBar };

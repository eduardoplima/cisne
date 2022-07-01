import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
    en: {
        translation: {
            title: 'Cisne - A risk management system',
            cancel: 'Cancel',
            authentication: {
                username: 'username',
                password: 'password',
                login: 'login',
                logout: 'logout',
                signup: 'signup',
                errors: {
                    login: 'Login failed',
                    signup: 'Signup failed',
                    required: {
                        username: 'Username is required',
                        password: 'Password is required',
                    }
                }
            },
            footer: {
                copyright: 'Cisne - A risk management system'
            }
        }
    },
    'pt-BR': {
        translation: {
            title: 'Cisne - Um sistema de gestão de riscos',
            cancel: 'Cancelar',
            authentication: {
                username: 'usuário',
                password: 'senha',
                login: 'entrar',
                logout: 'sair',
                signup: 'cadastrar',
                errors: {
                    login: 'Falha ao entrar',
                    signup: 'Falha ao cadastrar',
                    required: {
                        username: 'O nome de usuário é obrigatório',
                        password: 'A senha é obrigatória',
                    }
                }
            },
            footer: {
                copyright: 'Cisne - Um sistema de gestão de riscos'
            }
        }
    }
};

i18n.use(initReactI18next) // passes i18n down to react-i18next
    .init({
        resources,
        lng: 'en',
        fallbackLng: 'pt-BR',
        debug: true
    });

export default i18n;

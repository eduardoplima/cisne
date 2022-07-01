import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { RootState } from '../../app/store'


const domain = window.location.origin.split(/:\d+/)[0]
const apiPort = 8000
const DJANGO_ADDRESS = `${domain}:${apiPort}/api/`

export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({
        baseUrl: DJANGO_ADDRESS,
        prepareHeaders: (headers, { getState }) => {
            const state = getState() as RootState
            const token = state.auth.token
            if (token) {
                headers.set('Authorization', `Bearer ${token}`)
            }
            return headers
        },
    }),
    tagTypes: ['Organization', 'Macroprocess'],
    endpoints: (builder) => ({
        tokenAuth: builder.mutation({ query: (body) => {
            console.log(body);
            return {
                url: 'authenticate/',
                method: 'POST',
                body: body,
            }
        }}),
        getOrganization: builder.query({ query: () => {
            return {
                url: 'risk/organization/',
                method: 'GET',
            }
        }}),
        getMacroprocess: builder.query({ query: () => {
            return {
                url: 'risk/macroprocess/',
                method: 'GET',
            }
        }}),        
    }),
})

export const {
    useTokenAuthMutation,
    useGetOrganizationQuery,
    useGetMacroprocessQuery,
} = apiSlice
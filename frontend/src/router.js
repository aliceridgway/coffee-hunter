import { createRouter, createWebHistory } from "vue-router";

import CafeList from "./views/CafeList.vue"
import CreateUser from "./views/CreateUser.vue"

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: CafeList
        },
        {
            path: "/register",
            component: CreateUser
        }
    ]
})
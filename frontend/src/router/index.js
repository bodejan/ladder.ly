import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Data from '@/components/Data'
import About from '@/components/About'
import Hvm from '@/components/Hvm'
import Aim from '@/components/Aim'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/data',
      name: 'Data',
      component: Data
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/hvm',
      name: 'Hvm',
      component: Hvm
    },
    {
      path: '/aim',
      name: 'Aim',
      component: Aim
    }
  ]
})

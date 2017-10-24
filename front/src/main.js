import Vue from 'vue'
import Vonic from 'vonic/src/index.js'

// Page Components
import Index from './components/Index.vue'
import About from './components/About.vue'
import Intro from './components/Intro.vue'
import Login from './components/Login.vue'
import Welcome from './components/Welcome.vue'
import Register from './components/Register.vue'





// Routes
const routes = [
  { path: '/Index', component: Index },
  { path: '/about', component: About },
  { path: '/intro', component: Intro,
    children:[
        {path:'welcome', component:Welcome},
        {path:'login', component:Login},
        {path:'register', component:Register},
    ]
 },
  // { path: '/login', component: Login },
   {path:'*', redirect:'/intro/welcome'}  //404


]

Vue.use(Vonic.app, {
  routes: routes
})

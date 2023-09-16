import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import articlesPages from './pages/ArticlesPage.vue'
import articlePage from './pages/ArticlePage.vue'
import mainPage from './pages/MainPage.vue'
import loginForm from './pages/LoginForm.vue'
import registrationForm from './pages/RegistrationForm.vue'

Vue.config.productionTip = false

const routes = [
  { path: '/', component: mainPage },
  { path: '/articles', component: articlesPages },
  { path: '/articles/:id', component: articlePage, name: 'articleId', props: true },
  { path: '/login', component: loginForm },
  { path: '/registration', component: registrationForm }

]

const router = new VueRouter({
  routes
})

new Vue({ 
  render: h => h(App),
  router
}).$mount('#app')
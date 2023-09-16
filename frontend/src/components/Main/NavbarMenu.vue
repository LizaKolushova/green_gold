<template>
  
    <div class="container header__container">
      <nav>
        <div class="navbar">
          <div class="container nav-container">
            <input class="checkbox" type="checkbox" name="" id="" />
            <div class="hamburger-lines">
              <span class="line line1"></span>
              <span class="line line2"></span>
              <span class="line line3"></span>
            </div>  
            <div class="menu_info">
              <div class="logo">
                <h1>Green Gold</h1>
              </div>
              <div class="contacts">
                <li class="contact">
                  <span class="phone-title"><img src="images/place.svg" alt="place"></span>
                  <a class="adress" href="https://yandex.ru/maps/213/moscow/?ll=37.710300%2C55.784832&z=14">Москва</a></li>
                <li class="contact">
                  <span class="phone-title"><img src="images/phone.svg" alt="phone"></span>
                  <a class="phone" href="https://yandex.ru/maps/213/moscow/?ll=37.710300%2C55.784832&z=14">+7(927)933-88-85</a></li>
              </div>
            </div>
            <div class="menu-items">
              <li><router-link to="/">Главная</router-link></li>
              <li><router-link to="/articles">Новости</router-link></li>
              <li><router-link to="/articles/1">Новость недели</router-link></li>
              <li><router-link to="/registration">Вступить в клуб</router-link></li>
              <li><router-link to="/login">Войти</router-link></li>
            </div>
          </div>
        </div>
      </nav>
        </div>
    
</template>

<script>

export default {
 
};
</script>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.contacts{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding-right: 50px;
}
.menu_info{
  display: flex;
  height: 75px;
  width: 55%;
  margin-left: auto;
  justify-content: space-between;
  align-items: center;
}
.phone-title{
  color: #0e2431;
  font-size: 10px;
  text-transform: uppercase;
}
.adress, .phone{
  padding-bottom: 5px;
}
.navbar {
  width: 100%;
  box-shadow: 0 1px 4px rgb(146 161 176 / 15%);
  position: fixed;
  top: 0;
  z-index: 101;
}
.navbar .menu-items {
  display: flex;
  background-color: white;
}
.navbar .nav-container li {
  list-style: none;
    display: flex;
    align-items: center;
}
.navbar .menu-items a {
  text-decoration: none;
  color: white;
}
.navbar .nav-container a:hover{
    font-weight: bolder;
}
.nav-container {
  display: block;
  position: relative;
  height: 75px;
  background-color: white;
}
.nav-container .checkbox {
  position: absolute;
  display: block;
  height: 50px;
  width: 50px;
  top: 10px;
  left: 50px;
  z-index: 5;
  opacity: 0;
  cursor: pointer;
}
.nav-container .hamburger-lines {
  display: block;
  height: 33px;
  width: 50px;
  position: absolute;
  top: 21px;
  left: 50px;
  z-index: 2;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.nav-container .hamburger-lines .line {
  display: block;
  height: 3px;
  width: 100%;
  border-radius: 10px;
  background: #0e2431;
}
.nav-container .hamburger-lines .line1 {
  transform-origin: 7%;
  transition: transform 0.4s ease-in-out;
}
.nav-container .hamburger-lines .line2 {
  transition: transform 0.2s ease-in-out;
}
.nav-container .hamburger-lines .line3 {
  transform-origin: 8%;
  transition: transform 0.4s ease-in-out;
}
.navbar .menu-items {
  padding-top: 35px;
  /* box-shadow: inset 0 0 2000px rgb(255 255 255 / 50%); */
  height: 100vh;
  width: 26%;
  transform: translate(-150%);
  display: flex;
  flex-direction: column;
  padding-left: 40px;
  transition: transform 0.5s ease-in-out;
  text-align: center;
  align-content: flex-start;
  flex-wrap: wrap;
  align-items: flex-start;
}
.navbar .menu-items li {
  margin-bottom: 1.2rem;
  font-size: 1.5rem;
  font-weight: 500;
}
.logo {
  /* position: absolute; */
  top: 5px;
  right: 15px;
  font-size: 1.2rem;
  color: #0e2431;
  /* z-index: 2; */
}
h1{
  font-weight: 500;
}
.nav-container input[type="checkbox"]:checked ~ .menu-items {
  transform: translateX(0);
  background-color: #0e2431;
}
.nav-container input[type="checkbox"]:checked ~ .menu-items a {
  color: white;
  font-weight: 500;
  font-size: 1.2rem;
  padding: 0.7rem;
}
.nav-container input[type="checkbox"]:checked ~ .hamburger-lines .line1 {
  transform: rotate(45deg);
}
.nav-container input[type="checkbox"]:checked ~ .hamburger-lines .line2 {
  transform: scaleY(0);
}
.nav-container input[type="checkbox"]:checked ~ .hamburger-lines .line3 {
  transform: rotate(-45deg);
}
</style>
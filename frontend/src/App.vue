<template>
  <div id="app">
    <NavbarMenu/>
    <div class="content">
    <router-view></router-view>
    </div>
    <Footer/>
  </div>
</template>

<script>

import NavbarMenu from "./components/Main/NavbarMenu";
import Footer from "./components/Main/FooterMain";

export default {
  name: 'App',
  components: {
    NavbarMenu,
    Footer,
  }
}
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap");
*{
  margin: 0;
  padding: 0;
}
.content {
	min-height: calc(100vh - 80px);
}
a, a:visited {
  // color: black;
  text-decoration: none;
}
#app {
  font-family: 'Playfair Display';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  margin: 0 auto;
}
.header {
  height: 7vh;
  padding: 1vh 2vh;
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  &__nav {
    height: 7vh;
  }
}

.nav {
  height: 100%;
  &__list {
    height: 100%;
    display: flex;
    align-items: center;
    column-gap: 3vh;
  }
  &__point {
    list-style: none;
  }
  &__link {
    font-size: 2rem;
  }
}
</style>

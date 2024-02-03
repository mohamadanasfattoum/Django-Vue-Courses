
<template>
  <body :class="{ 'dark-mode':darkMode }">
    <Navbar :darkMode="darkMode" @dark-mode-change="toggleDarkMode" />

    <RouterView />
  </body>
</template>


<script>
  import { RouterLink, RouterView } from 'vue-router'
  import Navbar from './components/Navbar.vue';

  export default {
    name:'App',
    components: {
      Navbar,
    },
    data() {
      return{
        darkMode: false
      }        
    },
    mounted() {
      this.darkMode = localStorage.getItem('darkMode') == 'true';
    },
    methods: {
      toggleDarkMode(darkMode) {
        this.darkMode = darkMode
        localStorage.setItem('darkMode',this.darkMode)
      }
    }
  }

</script>

<style>
html.dark-mode{
  background-color: white;
}

body.dark-mode{
  background-color: black;
  color: white;
  width: 100%;
  height: 100vh;
}
</style>


<template>
  <nav class="navbar navbar-expand-lg" :class="{'bg-dark' : darkMode}">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Online Courses</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink class="nav-link active" aria-current="page" to="/">Courses</RouterLink>
          </li>
        </ul>
        <DarkMode :darkMode="darkMode" @dark-mode-change="toggleDarkMode" />
      </div>
    </div>
  </nav>
</template>



<script>
  import DarkMode from './DarkMode.vue';

  export default {
    name: 'Navbar',
    components: {
      DarkMode,
    },
    props: {
      darkMode: {
        type: Boolean , defaulte: false
      }
    },
    methods: {
      toggleDarkMode() {
        this.$emit('dark-mode-change' , !this.darkMode)

      }
    }

  }
</script>
<template>
  <NavbarCo></NavbarCo>
  <router-view/>
</template>

<script>
import NavbarCo from "@/components/NavbarCo.vue";

export default {
  components: {NavbarCo},
  methods: {
    handleLogout() {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      alert("Logout successful!");
      this.$router.push('/login');
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

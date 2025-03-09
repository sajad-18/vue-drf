<template>
  <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/register">register</router-link> |
      <router-link to="/login">Login</router-link> |
     <button @click="handleLogout">Logout</button>
  </nav>
</template>

<script>
export default {
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

<style scoped>

</style>
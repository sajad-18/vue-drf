<template>
  <div class="about">
    <img alt="Vue logo" src="../assets/logo.png">
    <RegisterPage/>
  </div>
</template>

<script>
// @ is an alias to /src
import RegisterPage from '@/components/RegisterPage.vue'

export default {
  name: 'RegisterView',
  components: {
    RegisterPage
  }
}
</script>
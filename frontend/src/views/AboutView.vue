<template>
  <div class="about">
    <img alt="Vue logo" src="../assets/logo.png">
    <AboutPage/>
  </div>
</template>

<script>
// @ is an alias to /src
import AboutPage from '@/components/AboutPage.vue'

export default {
  name: 'AboutView',
  components: {
    AboutPage
  }
}
</script>
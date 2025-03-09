<template>
  <div class="hello">
    <ul v-for="item in items" :key="item.id">
      <li>{{ item }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: []
    };
  },
  mounted() {
    axios.post('http://127.0.0.1:8000/question/create/')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

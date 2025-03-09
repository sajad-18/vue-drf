<template>
  <div class="login-container">
    <h2>Login</h2>
    <!-- نمایش پیام عمومی ارور -->
    <div v-if="errorMessage" class="error-message general-error">
      {{ errorMessage }}
    </div>
    <form @submit.prevent="handleLogin" class="login-form">
      <!-- Username -->
      <div class="form-group">
        <label>Username:</label>
        <input type="text" v-model="username" placeholder="Enter your username" required />
        <div v-if="formErrors.username" class="error-message">
          {{ formErrors.username[0] }}
        </div>
      </div>
      <!-- Password -->
      <div class="form-group">
        <label>Password:</label>
        <input type="password" v-model="password" placeholder="Enter your password" required />
        <div v-if="formErrors.password" class="error-message">
          {{ formErrors.password[0] }}
        </div>
      </div>
      <button type="submit" class="submit-button">Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "", // پیام عمومی ارور
      formErrors: {}, // ذخیره خطاهای مرتبط با فیلدها
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/accounts/token/", {
          username: this.username,
          password: this.password,
        });
        // ذخیره توکن‌ها
        localStorage.setItem("accessToken", response.data.access);
        localStorage.setItem("refreshToken", response.data.refresh);
        alert("Login successful!");
        this.$router.push("/"); // هدایت به صفحه اصلی
      } catch (error) {
        console.error(error.response?.data || error);
        if (error.response && error.response.data) {
          if (error.response.status === 401) {
            // اعتبارنامه‌ها نامعتبر هستند
            this.errorMessage = "Invalid username or password.";
          } else {
            this.formErrors = error.response.data;
          }
        } else {
          this.errorMessage = "An error occurred. Please try again later.";
        }
      }
    },
  },
};
</script>

<style scoped>
/* استایل‌های زیبا و مرتب */
.login-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 80%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

input[type="text"]:focus,
input[type="password"]:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 3px #007bff;
}

.error-message {
  color: red;
  font-size: 12px;
  margin-top: 5px;
}

.general-error {
  margin-bottom: 15px;
  padding: 10px;
  background-color: #ffe5e5;
  border: 1px solid #ff0000;
  border-radius: 5px;
  color: #ff0000;
}

.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>

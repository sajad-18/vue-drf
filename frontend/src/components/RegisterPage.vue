<template>
  <div class="register-container">
    <h2>Register</h2>
    <!-- نمایش پیام عمومی ارورها -->
    <div v-if="formErrors.non_field_errors" class="error-message general-error">
      {{ formErrors.non_field_errors[0] }}
    </div>
    <form @submit.prevent="handleRegister" class="register-form">
      <!-- Username -->
      <div class="form-group">
        <label>Username:</label>
        <input type="text" v-model="username" required />
        <div v-if="formErrors.username" class="error-message">
          {{ formErrors.username[0] }}
        </div>
      </div>
      <!-- Email -->
      <div class="form-group">
        <label>Email:</label>
        <input type="email" v-model="email" required />
        <div v-if="formErrors.email" class="error-message">
          {{ formErrors.email[0] }}
        </div>
      </div>
      <!-- Password -->
      <div class="form-group">
        <label>Password:</label>
        <input type="password" v-model="password" required />
        <div v-if="formErrors.password" class="error-message">
          {{ formErrors.password[0] }}
        </div>
      </div>
      <!-- Confirm Password -->
      <div class="form-group">
        <label>Confirm Password:</label>
        <input type="password" v-model="password2" required />
        <div v-if="formErrors.password2" class="error-message">
          {{ formErrors.password2[0] }}
        </div>
      </div>
      <button type="submit" class="submit-button">Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      password2: "",
      formErrors: {}, // ذخیره ارورها
    };
  },
  methods: {
    async handleRegister() {
      try {
        await axios.post("http://127.0.0.1:8000/accounts/register/", {
          username: this.username,
          email: this.email,
          password: this.password,
          password2: this.password2,
        });
        alert("Registration successful!");
        this.$router.push("/");
      } catch (error) {
        console.error(error.response?.data || error);
        if (error.response && error.response.data) {
          this.formErrors = error.response.data; // ارورها ذخیره شوند
        } else {
          this.formErrors = { general: "An error occurred. Please try again." };
        }
      }
    },
  },
};
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.register-form .form-group {
  margin-bottom: 15px;
}

.register-form label {
  display: block;
  margin-bottom: 5px;
  color: #555;
}

.register-form input {
  width: 100%;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.register-form input:focus {
  border-color: #007bff;
  outline: none;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.submit-button {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

.error-message {
  color: #dc3545;
  font-size: 0.9rem;
  margin-top: 5px;
}

.general-error {
  margin-bottom: 15px;
  text-align: center;
  font-weight: bold;
}
</style>


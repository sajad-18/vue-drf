<template>
  <div class="questions-container">
    <h2>Questions List</h2>
    <div v-if="questions.length" class="questions-list">
      <ul>
        <li v-for="question in questions" :key="question.id" class="question-item">
          <!-- نمایش سوال یا فرم ویرایش -->
          <div v-if="editingQuestionId !== question.id">
            <div class="question-header">
              <h3>{{ question.title }}</h3>
              <div class="actions">
                <button @click="startEditing(question)">Edit</button>
                <button @click="deleteQuestion(question.id)">Delete</button>
              </div>
            </div>
            <p>{{ question.body }}</p>
          </div>

          <!-- فرم ویرایش -->
          <div v-else class="edit-form">
            <form @submit.prevent="updateQuestion(question.id)">
              <input v-model="editedQuestion.title" placeholder="Title" required />
              <textarea v-model="editedQuestion.body" placeholder="Body" required></textarea>
              <div class="edit-actions">
                <button type="submit">Save</button>
                <button type="button" @click="cancelEditing">Cancel</button>
              </div>
            </form>
          </div>
        </li>
      </ul>
    </div>
    <div v-else>
      <p class="no-questions">No questions available.</p>
    </div>

    <h2>Add New Question</h2>
    <form @submit.prevent="addQuestion" class="question-form">
      <input v-model="newQuestion.title" placeholder="Title" required />
      <div v-if="formErrors.title" class="error-message">
        {{ formErrors.title[0] }}
      </div>

      <input v-model="newQuestion.slug" placeholder="Slug" required />
        <div v-if="formErrors.slug" class="error-message">
          {{ formErrors.slug[0] }}
        </div>

      <textarea v-model="newQuestion.body" placeholder="Body" required></textarea>
      <div v-if="formErrors.body" class="error-message">
        {{ formErrors.body[0] }}
      </div>

      <button type="submit">Add Question</button>
    </form>
  </div>
</template>


<script>
import apiClient from '@/services/authService';

export default {
  data() {
    return {
      questions: [],
      newQuestion: {
        title: '',
        slug: '',
        body: '',
      },
      formErrors: {}, // برای ذخیره پیام خطا
      editingQuestionId: null,
      editedQuestion: {
        title: '',
        body: '',
      },
    };
  },
  mounted() {
    this.fetchQuestions();
  },
  methods: {
    // GET: Fetch all questions
    async fetchQuestions() {
      try {
        const response = await apiClient.get('api/items/');
        this.questions = response.data;
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    },

    // POST: Add a new question
    async addQuestion() {
      try {
        const response = await apiClient.post('question/create/', this.newQuestion);
        console.log('Question created successfully:', response.data);
        await this.fetchQuestions(); // Refresh the questions list
        this.newQuestion = { title: '', slug: '', body: '' }; // Reset form
        this.formErrors = {}; // پاک کردن ارورها در صورت موفقیت
      } catch (error) {
        console.error('Error adding question:', error.response?.data || error);
        if (error.response && error.response.data) {
          this.formErrors = error.response.data; // ذخیره ارورها
        } else {
          this.formErrors = { general: 'An error occurred. Please try again.' };
        }
      }
    },

    // DELETE: Delete a question
    async deleteQuestion(id) {
      try {
        await apiClient.delete(`question/del/${id}/`);
        await this.fetchQuestions(); // Refresh the questions list
      } catch (error) {
        console.error('Error deleting question:', error.response?.data || error);
      }
    },

    // PUT: Update question
    async updateQuestion(id) {
      try {
        const response = await apiClient.put(
          `question/update/${id}/`,
          this.editedQuestion
        );
        const updatedQuestion = response.data;

        // به‌روزرسانی سوال در لیست
        const index = this.questions.findIndex((q) => q.id === id);
        if (index !== -1) {
          this.questions.splice(index, 1, updatedQuestion);
        }
        this.cancelEditing();
      } catch (error) {
        console.error('Error updating question:', error.response?.data || error);
      }
    },

    // شروع ویرایش
    startEditing(question) {
      this.editingQuestionId = question.id;
      this.editedQuestion = { title: question.title, body: question.body };
    },

    // لغو ویرایش
    cancelEditing() {
      this.editingQuestionId = null;
      this.editedQuestion = { title: '', body: '' };
    },
  },
};
</script>



<style scoped>
.questions-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 30px;
  background-color: #f8f9fa;
  border-radius: 12px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #007BFF;
  text-align: center;
  margin-bottom: 25px;
  font-size: 1.8rem;
  font-weight: bold;
}

.questions-list {
  margin: 20px 0;
}

.question-item {
  background-color: white;
  padding: 20px;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
  position: relative;
  list-style: none;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.question-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.question-header h3 {
  margin: 0;
  color: #333;
  font-size: 1.2rem;
  font-weight: 600;
}

.actions {
  display: flex;
  gap: 12px;
}

.actions button {
  padding: 8px 15px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.3s ease;
}

.actions button:first-child {
  background-color: #ffc107;
  color: white;
}

.actions button:last-child {
  background-color: #dc3545;
  color: white;
}

.actions button:hover {
  opacity: 0.8;
}

.no-questions {
  text-align: center;
  color: #888;
  font-size: 1.1rem;
}

.edit-form form {
  display: flex;
  flex-direction: column;
}

.edit-form input,
.edit-form textarea {
  margin: 10px 0;
  padding: 12px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  resize: vertical;
  box-sizing: border-box;
}

.edit-form textarea {
  min-height: 100px;
}

.edit-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
}

.edit-actions button {
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 6px;
  transition: background-color 0.3s ease;
}

.edit-actions button:hover {
  background-color: #0056b3;
}

.question-form {
  margin-top: 30px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.question-form input,
.question-form textarea {
  margin: 10px 0;
  padding: 12px;
  font-size: 1rem;
  width: 100%;
  max-width: 600px;
  border: 1px solid #ddd;
  border-radius: 6px;
}

.question-form button {
  padding: 12px 24px;
  background-color: #007BFF;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 6px;
  transition: background-color 0.3s ease;
}

.question-form button:hover {
  background-color: #0056b3;
}

.error-message {
  color: #dc3545;
  font-size: 0.9rem;
  margin-top: 5px;
}

</style>

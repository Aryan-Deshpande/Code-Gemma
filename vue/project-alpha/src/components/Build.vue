<template>
  <div class="build-container">
    <div class="chat">
      <!-- Make a rectangle div where text can be entered from the text prompt below -->
      Hey there, I'm where the answer is supposed to be
      <h3>{{ chatval }}</h3>
    </div>
    <div class="input-wrapper">
      <input type="text" class="input-text" v-model="inputText" placeholder="Try me">
      <button class="btn1" @click="getval">Submit</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const inputText = ref('');
const chatval = ref('');

function getval() {
  chatval.value = inputText.value;
}
</script>

<style>
.build-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.chat {
  text-align: center;
  background-color: grey;
  color: white;
  padding: 10px;
  border-radius: 3px;
  margin: 10px;
  width: 100%;
  max-width: 500px; /* Adjust the maximum width as needed */
  height: 200px; /* Adjust the height as needed */
  overflow-y: scroll;
  scroll-behavior: smooth;
}

.input-wrapper {
  display: flex;
  align-items: center;
}

.input-text {
  flex: 1;
  margin-right: 10px;
}

.btn1 {
  border: 0 solid;
  outline: 1px solid rgba(125, 141, 190, 0.5);
  background-color: #7a0f0f;
  color: rgb(49, 51, 82);
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn1:hover {
  background-color: #5a0909; /* Adjust the hover background color as needed */
}
</style>

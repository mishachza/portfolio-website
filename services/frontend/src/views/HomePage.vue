<template>
    <div class="container">
      <button class="btn" @click="sendData"><h1>ВСЁ ХОРОШО.</h1></button>
      <a href="https://t.me/alrightalright" class="telegram-link">
        <!-- <img src="@/assets/telegram-fill.svg" alt="Telegram" width="48" height="48" class="telegram-icon"> -->
      </a>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    methods: {
      async sendData() {
        try {
          const response = await axios.post('/api/send_data', {
            data: 'Данные отправлены из приложения Vue.js',
          });
          console.log(response.data);
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: 'IBM Plex Sans JP', sans-serif;
  }
  
  .btn {
    border: 0px;
    background-color: transparent;
  }
  
  h1 {
    font-size: 36px;
    color: rgb(22, 22, 22);
    cursor: pointer;
  }
  
  .telegram-icon {
    filter: grayscale(100%);
    transition: filter 0.3s;
  }
  
  .telegram-link {
    cursor: pointer;
  }
  
  .telegram-link:hover .telegram-icon {
    filter: none;
  }
  </style>
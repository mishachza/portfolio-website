<template>
    <div class="button-container-open" @click="onClick">
      <button class="button-open">ПОДРОВНЯТЬСЯ</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      onClick() {
        this.$emit('click');
      }
    }
  };
  </script>
  
  <style scoped>
  .button-container-open {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    flex-grow: 1;
    cursor: pointer;
  }
  
  .button-open {
    border: 2px solid #D0A003;
    background-color: transparent;
    color: #D0A003;
    padding: 15px 30px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
    transition: transform 0.3s ease, color 0.3s ease, border-color 0.3s ease;
  }
  
  .button-open:hover {
    transform: scale(1.1);
  }
  </style>
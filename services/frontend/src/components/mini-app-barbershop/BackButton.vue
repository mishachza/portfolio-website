<template>
    <button class="back-button" @click="onClick">
      <img :src="backLine" alt="Назад" class="back-button-icon">
    </button>
  </template>
  
  <script>
  import backLine from '@/assets/icons/back-line.svg';
  
  export default {
    data() {
      return {
        backLine: backLine
      };
    },
    methods: {
      onClick() {
        this.$emit('click');
      }
    }
  };
  </script>
  
  <style scoped>
  .back-button {
    display: flex;
    background-color: transparent;
    border: 0;
    align-items: center;
    padding: 20px;
    cursor: pointer;
  }
  
  .back-button:hover {
    transform: scale(1.1);
  }
  
  .back-button-icon {
    width: 25px;
    height: 25px;
    filter: invert(100%) sepia(100%) saturate(0%) hue-rotate(0deg);
    transition: transform 0.3s ease, color 0.3s ease, border-color 0.3s ease;
  }
  </style>
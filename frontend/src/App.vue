<template>
  <div class="container">
    <h1>ВСЁ ХОРОШО.</h1>
    <a href="https://t.me/alrightalright" class="telegram-link">
      <!-- <img src="@/assets/telegram-fill.svg" alt="Telegram" width="48" height="48" class="telegram-icon"> -->
    </a>
  </div>
</template>

<script>
export default {
  name: 'App',
}
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

h1 {
  font-size: 48px;
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
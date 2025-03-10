<template>
  <div class="master-details">
    <div class="title-back-container">
      <BackButton @click="closeDetails" />
      <div class="title-page"><h3>ВЫБОР ВРЕМЕНИ:</h3></div>
    </div>

    <div class="master-info">
      <div class="photo">
        <img :src="master.photo" :alt="master.name">
      </div>
      <h3>{{ master.name }}</h3>
      <button class="rating-button"><b>{{ master.rating }}</b> <img src="@/assets/icons/star.png" alt="rating" class="rating-star-icon"></button>
    </div>

    <div v-if="!showCalendar" class="available-times">
      <div class="available-times-text">Свободное время на сегодня:</div>
      <div class="time-buttons">
        <button v-for="time in availableTimes" :key="time" class="time-button"  @click="handleTimeSelected(time)">{{ time }}</button>
      </div>
    </div>

    <button v-if="!showCalendar" class="calendar-button" @click="showCalendar = true">Открыть календарь</button>
    <SimpleCalendar v-if="showCalendar" @time-selected="handleTimeSelected" />
  </div>
</template>

<script>
import BackButton from './BackButton.vue';
import SimpleCalendar from './SimpleCalendar.vue';

export default {
  components: {
    BackButton,
    SimpleCalendar,
  },
  props: {
    master: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      availableTimes: ['10:00', '11:30', '14:00', '16:30'],
      showCalendar: false,
    };
  },
  mounted() {
    // Проверка, что Telegram Web App API доступен
    if (window.Telegram && window.Telegram.WebApp) {
      window.Telegram.WebApp.ready(); // Говорим Telegram, что Web App готов
    } else {
      console.warn('Telegram Web App API не доступен');
    }
  },
  methods: {
    closeDetails() {
      this.$emit('close');
    },
    handleTimeSelected(selectedTime) {
      this.selectTime(selectedTime);
      this.showCalendar = false;
    },
    selectTime(time) {
      let tg = window.Telegram.WebApp;
      let data = JSON.stringify({
        time: time,
        masterName: this.master.name,
      });

      if (window.Telegram && window.Telegram.WebApp) {
        tg.sendData(data);
        tg.answerWebAppQuery(data)
        alert('Время отправлено в бот!');
      } else {
        alert('Telegram Web App API не доступен.');
      }
    },
  },
};
</script>

<style scoped>
.master-details {
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center; /* Выравнивание по центру по горизонтали */
}

.title-back-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 50px;
}

.title-page {
  display: flex;
  flex-direction: row;
  font-family: 'Roboto Flex', sans-serif;
  font-size: 14px;
  color: #ffffff;
  margin-left: 20px;
}

.master-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
  align-items: center;
  justify-content: center;
}

.photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 10px;
}

.photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.rating-button {
  display: flex;
  flex-direction: row;
  background-color: transparent;
  color: #D0A003;
  border: 0px solid #D0A003;
  font-size: 14px;
  align-items: center;
  justify-content: center;
  margin-top: 5px;
}

.rating-star-icon {
  width: 14px;
  height: 14px;
  margin-left: 3px;
  margin-right: 15px;
}

.available-times-text {
  font-family: sans-serif;
  font-size: 16px;
}

.available-times {
  margin-bottom: 20px;
  text-align: center;
}

.time-buttons {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.time-button {
  background-color: #D0A003;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
}

.calendar-button {
  background-color: transparent;
  color: #D0A003;
  border: 2px solid #D0A003;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  margin-bottom: 40px;
}
</style>
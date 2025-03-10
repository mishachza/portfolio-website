<template>
  <div class="simple-calendar">
    <div class="days">
      <button
        v-for="(day, index) in nextFiveDays"
        :key="index"
        class="day-button"
        :class="{ selected: selectedDay === day }"
        :disabled="isPastDate(day)"
        @click="selectDay(day)"
      >
        {{ formatDate(day) }}
      </button>
    </div>

    <div v-if="selectedDay" class="time-slots">
      <div class="date-time-title"><p>Доступное время на {{ formatDate(selectedDay) }}:</p></div>
      <button
        v-for="time in availableTimesForSelectedDay"
        :key="time"
        class="time-button"
        :disabled="isTimeBooked(time)"
        @click="selectTime(time)"
        :class="{ booked: isTimeBooked(time) }"
      >
        {{ time }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedDay: null,
      availableTimes: ["10:00", "12:00", "14:00", "16:00"],
      nextFiveDays: [],
      bookedTimes: {
        "2025-02-12": ["10:00", "12:00"],
        "2025-02-13": ["14:00"],
      },
    };
  },
  mounted() {
    this.generateNextFiveDays();
  },
  methods: {
    generateNextFiveDays() {
      const today = new Date();
      for (let i = 0; i < 5; i++) {
        const nextDay = new Date(today);
        nextDay.setDate(today.getDate() + i);
        this.nextFiveDays.push(nextDay);
      }
    },
    formatDate(date) {
      const options = { weekday: 'short', month: 'long', day: 'numeric' };
      return date.toLocaleDateString("ru-RU", options).replace(/(\sг\.?)/, '');
    },
    selectDay(day) {
      this.selectedDay = day;
    },
    selectTime(time) {
      // Вместо alert, испускаем событие
      this.$emit("time-selected", time);
    },
    isPastDate(date) {
      const today = new Date();
      today.setHours(0, 0, 0, 0); // Обнуляем время для корректного сравнения дат
      return date < today;
    },
    isTimeBooked(time) {
      if (!this.selectedDay) return false; // Если день не выбран, все времена доступны
      const selectedDateString = this.selectedDay.toISOString().slice(0, 10);
      return (this.bookedTimes[selectedDateString] || []).includes(time);
    },
  },
  computed: {
    availableTimesForSelectedDay() {
      if (!this.selectedDay) {
        return this.availableTimes; // Возвращаем все доступные времена, если день не выбран
      }

      const selectedDateString = this.selectedDay.toISOString().slice(0, 10); // Формат YYYY-MM-DD

      if (this.bookedTimes[selectedDateString]) {
        return this.availableTimes.filter(
          (time) => !this.bookedTimes[selectedDateString].includes(time)
        );
      } else {
        return this.availableTimes;
      }
    },
  },
};
</script>

<style scoped>
.simple-calendar {
  margin-bottom: 20px;
}

.days {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.day-button {
  padding: 10px 15px;
  margin: 5px;
  border: 1px solid #D0A003;
  border-radius: 30px;
  background-color: transparent;
  color: #D0A003;
  cursor: pointer;
}

.day-button:disabled {
  background-color: #eee;
  color: #999;
  cursor: not-allowed;
}

.day-button.selected {
  background-color: #D0A003;
  color: #fff;
}

.time-slots {
  margin-top: 20px;
  font-family: sans-serif;
  text-align: center;
}

.time-slots p { 
  text-align: center;
}

.date-time-title {
  display: flex;
  justify-content: center;
  align-items: center;
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

.time-button:disabled {
  background-color: #ccc;
  color: #666;
  cursor: not-allowed;
}

.time-button.booked {
  background-color: #ccc;
  color: #666;
  cursor: not-allowed;
}
</style>
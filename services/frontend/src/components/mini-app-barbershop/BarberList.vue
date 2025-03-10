<template>
  <div class="barber-list">
    <div class="title-back-container" v-if="!selectedMaster">
      <BackButton @click="closeList" />
      <div class="title-page"><h3>ВЫБОР МАСТЕРА:</h3></div>
    </div>

    <MasterDetails v-if="selectedMaster" :master="selectedMaster" @close="showMasterList"/>

    <div v-else v-for="master in masters" :key="master.name" class="master-container" @click="showMasterDetails(master)">
      <div class="photo">
        <img :src="master.photo" alt="">
      </div>
      <div class="master-name"><b>{{ master.name }}</b></div>
      <button class="rating-button">{{ master.rating }} <img src="@/assets/icons/star.png" alt="rating" class="rating-star-icon"></button>
    </div>
  </div>
</template>

<script>
import drovosekov from '@/assets/images/drovosekov.png';
import TatianaPostrigaeva from '@/assets/images/TatianaPostrigaeva.png';
import stigmatamatorev from '@/assets/images/stigmatamatorev.png';
import pivalych from '@/assets/images/pivalych.png';
import star from '@/assets/icons/star.png';
import BackButton from './BackButton.vue';
import MasterDetails from './MasterDetails.vue';

export default {
  components: {
    BackButton,
    MasterDetails
  },
  data() {
    return {
      masters: [
        { name: 'РЕДНЕК ЛАМБЕРДЖЕКОВ', photo: drovosekov, rating: 124 },
        { name: 'ВЕНЕРА КОЗЕРОГОВНА', photo: TatianaPostrigaeva, rating: 358 },
        { name: 'СТИГМАТ АМАТОРЕВ', photo: stigmatamatorev, rating: 99 },
        { name: 'ПИВ АЛЫЧ', photo: pivalych, rating: 999 }
      ],
      star: star,
      selectedMaster: null
    };
  },
  methods: {
    closeList() {
      this.$emit('close'); // Emit event to parent component
    },
    showMasterDetails(master) {
      this.selectedMaster = master;
    },
    showMasterList() {
      this.selectedMaster = null;
    }
  }
};
</script>

<style scoped>
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
  align-items: center;
  font-family: 'Roboto Flex', sans-serif;
  font-size: 14px;
  color: #ffffff;
  margin-left: 20px;
}

.barber-list {
  color: rgb(255, 255, 255);
  border-radius: 5px;
  margin-top: 20px;
  width: 80%;
  z-index: 2;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 15px;
}

.master-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  position: relative;
}

.master-container:hover {
  background-color: #000000d3;
  cursor: pointer;
}

.master-container:hover .master-name,
.master-container:active .master-name,
.master-container:active .photo img,
.master-container:hover .photo img {
  transform: scale(1.1);
}

.master-name {
  margin-right: auto;
  font-family: 'Roboto Flex', serif;
  font-size: 14px;
  transition: transform 0.3s ease;
}

.photo {
  width: 100px;
  height: 100px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.photo img {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 50%;
  transition: transform 0.3s ease;
}

.rating-button {
  display: flex;
  flex-direction: row;
  background-color: transparent;
  color: #D0A003;
  border: 0px solid #D0A003;
  font-family: 'Roboto Flex', serif;
  font-size: 14px;
  align-items: center;
  justify-content: center;
}

.rating-star-icon {
  width: 14px;
  height: 14px;
  margin-left: 10px;
  margin-right: 15px;
}
</style>
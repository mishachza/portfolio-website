<template>
    <div class="barber-shop-list">
      <div v-for="shop in barberShops" :key="shop.address" class="barber-shop-item">
        <h3>{{ shop.name }}</h3>
        <img :src="shop.thumbnail" :alt="shop.name" class="thumbnail" @click="openMap(shop)">
        <p>{{ shop.address }}</p>
        <button @click="openMap(shop)">Открыть на карте</button>
      </div>
    </div>
  </template>
  
  <script>

const barberShops = [
  {
    name: "Барбершоп на Криворожской",
    address: "Криворожская ул., [номер дома]", // Замените на реальный номер дома
    latitude: 55.794531,   // Примерные координаты, нужно уточнить
    longitude: 37.570459,  // Примерные координаты, нужно уточнить
    thumbnail: "/assets/images/krivorozhskaya_thumbnail.jpg" // Путь к миниатюре
  },
  {
    name: "Барбершоп на Кривоколенном",
    address: "Кривоколенный пер., [номер дома]", // Замените на реальный номер дома
    latitude: 55.764258,   // Примерные координаты, нужно уточнить
    longitude: 37.641035,  // Примерные координаты, нужно уточнить
    thumbnail: "/assets/images/krivokolenny_thumbnail.jpg" // Путь к миниатюре
  }
];

  export default {
    data() {
      return {
        barberShops: [
          {
            name: "Барбершоп на Криворожской",
            address: "Криворожская ул., [номер дома]",
            latitude: 55.794531,
            longitude: 37.570459,
            thumbnail: "/assets/images/krivorozhskaya_thumbnail.jpg"
          },
          {
            name: "Барбершоп на Кривоколенном",
            address: "Кривоколенный пер., [номер дома]",
            latitude: 55.764258,
            longitude: 37.641035,
            thumbnail: "/assets/images/krivokolenny_thumbnail.jpg"
          }
        ]
      };
    },
    methods: {
      openMap(shop) {
        const url = `https://yandex.ru/maps/?ll=${shop.longitude},${shop.latitude}&z=17&text=${encodeURIComponent(shop.address)}`;
        window.open(url, '_blank'); // Открывает в новой вкладке
      }
    }
  };
  </script>
  
  <style scoped>
  .barber-shop-list {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .barber-shop-item {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    text-align: center;
  }
  
  .thumbnail {
    width: 150px;
    height: 100px;
    cursor: pointer;
  }
  </style>
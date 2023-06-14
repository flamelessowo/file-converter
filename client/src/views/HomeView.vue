<script setup lang="ts">
</script>
<template>
  <div class="landing-page">
    <div class="hero">
      <h1>Сайт для конвертування файлів</h1>
      <p></p>
    </div>
    <div class="features">
      <div class="feature">
        <img src="/why.jpg" alt="Feature 1" />
        <h3>Навіщо?</h3>
        <p>Сайти для конвертування файлів надають користувачам можливість змінювати формати файлів для забезпечення сумісності між різними програмами та пристроями, а також для зменшення розміру файлу. Вони корисні для широкого кола користувачів, включаючи фотографів, студентів і науковців, які мають потребу у конвертуванні даних у різні формати.</p>
      </div>
      <div class="feature">
        <img src="/problem.jpg" alt="Feature 2" />
        <h3>Які проблеми він вирішує?</h3>
        <p>Сайт для конвертування файлів вирішує проблеми несумісності форматів між програмами та пристроями, а також дозволяє зменшити розмір файлу. Він є зручним та доступним інструментом, який допомагає користувачам швидко та легко конвертувати файли в потрібний їм формат.</p>
      </div>
      <div class="feature">
        <img src="/benefit.jpg" alt="Feature 3" />
        <h3>Яка користь?</h3>
        <p>Сайт для конвертування файлів надає користь у забезпеченні сумісності форматів, зменшенні розміру файлів, зручності використання та універсальності для різних типів файлів.</p>
      </div>
    </div>
  </div>
</template>
<style scoped>
.landing-page {
  text-align: center;
  padding: 50px;
}

.hero {
  margin-bottom: 50px;
   font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

.cta-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 24px;
  cursor: pointer;
}

.features {
  display: flex;
  justify-content: space-between;
  margin-bottom: 50px;
}

.feature {
  width: 30%;
  text-align: center;
  font-size: 24px;
   font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

.feature img {
  width: 100%;
  max-width: 200px;
  height: auto;
  margin-bottom: 20px;
}

footer {
  background-color: #f5f5f5;
  padding: 20px;
  text-align: center;
  font-size: 14px;
}
</style>

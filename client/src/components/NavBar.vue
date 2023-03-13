<script lang="ts">
import { ref } from "vue";
import { generateTabNavigation } from '../core/navigation';

export default {
  setup() {
    const items = ref(generateTabNavigation());
    return { items };
  },
};
</script>

<template>
  <div>
    <MenuBar :model="items">
      <template #start>
        <img
          alt="logo"
          src="https://c4.wallpaperflare.com/wallpaper/206/351/660/anime-girls-black-hair-long-hair-purple-eyes-cute-little-girl-hd-wallpaper-preview.jpg"
          height="40"
          class="mr-2"
        />
      </template>
      <template #end>
        <InputText placeholder="Search" type="text" />
      </template>
    </MenuBar>
  </div>
</template>

<style lang="css">

</style>

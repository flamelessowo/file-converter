<script lang="ts" setup>
import UploadFile from "../components/UploadFile.vue";

const props = defineProps<{ // TODO make usage of own interfaces
  type: string
  fromFormat: string
  fromFormatLabel: string
  toFormat: string
  toFormatLabel: string
  description: string
}>()
</script>
<template>
  <div>
    <div class="text-box">
      <h1 class="">
        Convert files from {{ fromFormatLabel }} to {{ toFormatLabel }}
      </h1>
      <p>{{ description }}</p>
    </div>
    <div class="upload-box">
      <UploadFile/>
    </div> 
  </div>
</template>
<style lang="css" scoped>
.text-box {
  text-align: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";

}

.text-box h1 {
  font-weight: bold;
}

.upload-box {
  max-width: 50rem;
  margin: 0 auto;
}
</style>
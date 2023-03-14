<script lang="js">
import { UPLOAD_URI } from '../constants/server.ts';
import { mapStores } from 'pinia'
import { userStore } from '../stores/userstore.ts'
import axios from 'axios';


export default {
  computed: {
    ...mapStores(userStore)
  },
  data() {
    return {
      UPLOAD_URI: UPLOAD_URI,
      uploadedFiles: [],
      files: [],
      totalSize: 0,
      totalSizePercent: 0,
    };
  },
  methods: {
    uploader(event) {
      const files = event.files;
      const formData = new FormData();
      for (const file of files) {
        formData.append("files", file);
      }
      axios({
        method: 'post',
        url: UPLOAD_URI,
        data: formData,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'multipart/form-data',
          'User-UUID': this.userStore.getUUID
        }
      }).then(response => {
        console.log(response);
        this.$emit('uploadedEvent')
      })
    },

    onRemoveTemplatingFile(file, onFileRemove, index) {
      onFileRemove(index);
      this.totalSize -= parseInt(this.formatSize(file.size));
      this.totalSizePercent = this.totalSize / 10;
    },
    onClearTemplatingUpload(clear) {
      clear();
      this.totalSize = 0;
      this.totalSizePercent = 0;
    },
    onSelectedFiles(event) {
      this.files = event.files;
      this.files.forEach((file) => {
        this.totalSize += parseInt(this.formatSize(file.size));
      });
    },
    onAdvancedUpload() {
      this.$toast.add({
        severity: "info",
        summary: "Success",
        detail: "File Uploaded",
        life: 3000,
      });
    },
    uploadEvent(callback) {
      this.totalSizePercent = this.totalSize / 10;
      callback();
    },
    onTemplatedUpload(event) {
      console.log(event);
      this.totalSize = 0;
      this.totalSizePercent = 0;
      this.$toast.add({
        severity: "info",
        summary: "Success",
        detail: "File Uploaded",
        life: 3000,
      });
    },
    onUpload() {
      this.$toast.add({
        severity: "info",
        summary: "Success",
        detail: "File Uploaded",
        life: 3000,
      });
    },
    formatSize(bytes) {
      if (bytes === 0) {
        return "0 B";
      }

      let k = 1000,
        dm = 3,
        sizes = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
        i = Math.floor(Math.log(bytes) / Math.log(k));

      return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + " " + sizes[i];
    },
  },
};
</script>

<template>
  <Toast />
  <FileUpload
    name="demo[]"
    :customUpload="true"
    :url="UPLOAD_URI"
    :multiple="true"
    accept=""
    :maxFileSize="10000000"
    @uploader="uploader"
    @upload="onTemplatedUpload($event)"
    @select="onSelectedFiles"
  >
    <template
      #header="{ chooseCallback, uploadCallback, clearCallback, files }"
    >
      <div
        class="flex flex-wrap justify-content-between align-items-center flex-1 gap-2"
      >
        <div class="flex gap-2">
          <Button
            @click="chooseCallback()"
            icon="pi pi-download"
            class="p-button-rounded"
          ></Button>
          <Button
            @click="uploadEvent(uploadCallback)"
            icon="pi pi-cloud-upload"
            class="p-button-rounded p-button-success"
            :disabled="!files || files.length === 0"
          ></Button>
          <Button
            @click="clearCallback()"
            icon="pi pi-times"
            class="p-button-rounded p-button-danger"
            :disabled="!files || files.length === 0"
          ></Button>
        </div>
        <ProgressBar
          :value="totalSizePercent"
          :showValue="false"
          :class="[
            'md:w-20rem h-1rem w-full md:ml-auto',
            { 'exceeded-progress-bar': totalSizePercent > 100 },
          ]"
          ><span class="white-space-nowrap"
            >{{ totalSize }}B / 1Mb</span
          ></ProgressBar
        >
      </div>
    </template>
    <template
      #content="{
        files,
        uploadedFiles,
        removeUploadedFileCallback,
        fileRemoveCallback,
      }"
    >
      <div v-if="files.length > 0">
        <h5>Pending</h5>
        <div class="flex flex-wrap p-5 gap-5">
          <div
            v-for="(file, index) of files"
            :key="file.name + file.type + file.size"
            class="card m-0 px-6 flex flex-column border-1 surface-border align-items-center gap-3"
          >
            <div>
              <img
                role="presentation"
                :alt="file.name"
                :src="file.objectURL"
                width="50"
                height="50"
                class="shadow-2"
              />
            </div>
            <span class="font-semibold">{{ file.name }}</span>
            <div>{{ formatSize(file.size) }}</div>
            <Badge value="Pending" severity="warning" />
            <Button
              icon="pi pi-times"
              @click="onRemoveTemplatingFile(file, fileRemoveCallback, index)"
              class="p-button-outlined p-button-danger p-button-rounded"
            />
          </div>
        </div>
      </div>

      <div v-if="uploadedFiles.length > 0">
        <h5>Completed</h5>
        <div class="flex flex-wrap p-0 sm:p-5 sm:p-5 gap-5">
          <div
            v-for="(file, index) of uploadedFiles"
            :key="file.name + file.type + file.size"
            class="card m-0 px-6 flex flex-column border-1 surface-border align-items-center gap-3"
          >
            <div>
              <img
                role="presentation"
                :alt="file.name"
                :src="file.objectURL"
                width="100"
                height="50"
                class="shadow-2"
              />
            </div>
            <span class="font-semibold">{{ file.name }}</span>
            <div>{{ formatSize(file.size) }}</div>
            <Badge value="Completed" class="mt-3" severity="success" />
            <Button
              icon="pi pi-times"
              @click="removeUploadedFileCallback(index)"
              class="p-button-outlined p-button-danger p-button-rounded"
            />
          </div>
        </div>
      </div>
    </template>
    <template #empty>
      <div class="flex align-items-center justify-content-center flex-column">
        <i
          class="pi pi-cloud-upload border-2 border-circle p-5 text-8xl text-400 border-400"
          style="font-size: 20rem"
        ></i>
        <p class="mt-4 mb-0">Drag and drop files to here to upload.</p>
      </div>
    </template>
  </FileUpload>
</template>

<style lang="css" scoped></style>

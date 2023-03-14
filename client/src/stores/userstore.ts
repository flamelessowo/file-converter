import { defineStore } from 'pinia'
import { v4 } from 'uuid'

export const userStore = defineStore('user', {
  state: () => ({ UUID: v4(), userName: null, password: null }),
  getters: {
    getUUID: (state) => state.UUID
  }
})
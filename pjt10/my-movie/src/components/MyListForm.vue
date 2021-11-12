<template>
  <div>
    <input 
      type="text"
      @keyup.enter="createMovie"
      v-model.trim="title"
    >
    <button @click="createMovie">Add</button>
  </div>
</template>

<script>
import {v4 as uuidv4} from 'uuid'
export default {
  name: "MyListForm",
  data() {
    return {
      title: null 
    }
  },
  methods: {
    createMovie(){
      if (!this.title) {
        return  
      }

      const movieItem = {
        id: uuidv4(),
        title: this.title    
      }

      this.$emit('create-movie-item', movieItem)
      this.clearInput()
    },
    clearInput() {
      this.title = null 
    }
  }
}
</script>

<style>

</style>
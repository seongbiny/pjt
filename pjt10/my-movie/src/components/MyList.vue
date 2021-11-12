<template>
  <div>
    <my-list-item v-for="movie in movieList" :key="movie.id" :movie="movie"></my-list-item>
  </div>
</template>

<script>
import MyListItem from './MyListItem.vue'
export default {
  name: "MyList",
  components: {
    MyListItem
  },
  props: {
    movieList: Array 
  }
}
</script>

<style>

</style>
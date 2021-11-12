<template>
  <div>
    <h1>My Movie List</h1>
    <my-list-form @create-movie-item="onCreateMovieItem"></my-list-form>
    <my-list :movieList="movieList"></my-list>
  </div>
</template>

<script>
import MyListForm from "@/components/MyListForm.vue";
import MyList from  "@/components/MyList.vue";

export default {
  name: "MyMovieList",
  components: {
    MyListForm,
    MyList
  }, 
  data() {
    return {
      movieList : null
    }
  },
  created(){
    this.movieList = JSON.parse(localStorage.getItem('movieList')) ?? []
  },
  methods: {
    onCreateMovieItem(movieItem){
      this.movieList.push(movieItem)
      this.saveMovieList()
    },
    saveMovieList(){
      localStorage.setItem('movieList', JSON.stringify(this.movieList))
    }
  },
};
</script>
  
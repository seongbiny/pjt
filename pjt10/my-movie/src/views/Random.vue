<template>
  <div>
    <button @click="getMovie">PICK</button>
    <div v-if="selectedMovie">
      <div class="d-flex justify-content-center">
        <movie-card :movieCard="selectedMovie"></movie-card>
      </div>  
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import _ from "lodash";
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: "Random", 
  components: {
    MovieCard
  },
  data: function () {
    return {
      selectedMovie: null,
    };
  },
  computed: {
    ...mapState(["movieCards"]),
  },
  methods: {
    getMovie: function () {
      this.selectedMovie = _.sample(this.movieCards);
    },
  },
};
</script>

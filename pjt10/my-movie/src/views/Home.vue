<template>
  <div class="text-center">
    <div
      class="row row-cols-3"
      style="padding-left: 300px; padding-right: 300px"
    >
      <movie-card
        v-for="movieCard in movieCards"
        :key="movieCard.id"
        :movieCard="movieCard"
        class="col"
      >
      </movie-card>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import MovieCard from "@/components/MovieCard.vue";
export default {
  name: "Home",
  components: {
    MovieCard,
  },

  computed: {
    ...mapState(["movieCards"]),
  },
};
</script>

<template>
  <div>
    <b-card
      :title="movieCard.title"
      :img-src="posterPath"
      img-alt="Image"
      img-top
      tag="article"
      class="mb-2"
    >
      <b-card-text>
        {{ overview }}
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movieCard: {
      type: Object,
    },
  },
  computed: {
    posterPath() {
      return `https://image.tmdb.org/t/p/w200${this.movieCard.poster_path}`;
    },
    overview() {
      if (this.movieCard.overview.length > 50) {
        return this.movieCard.overview.slice(0, 50) + "...";
      } else {
        return this.movieCard.overview;
      }
    },
  },
};
</script>

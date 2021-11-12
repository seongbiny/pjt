<template>
  <div>
    <b-nav id="nav" align="right" style="background-color: #e3f2fd">
      <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
      <b-nav-item><router-link to="/random">Random</router-link></b-nav-item>
      <b-nav-item
        ><router-link to="/my-movie-list"
          >My Movie List</router-link
        ></b-nav-item
      >
    </b-nav>
    <b-container id="app" style="padding-top: 50px; padding-bottom: 50px">
      <router-view />
    </b-container>
  </div>
</template>

<script>
export default {
  name: "App",
  created() {
    this.$store.dispatch("loadMovieCards");
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

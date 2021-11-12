import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieCards: [],
  },
  mutations: {
    LOAD_MOVIE_CARDS(state, results) {
      state.movieCards = results
    },
  },
  actions: {
    async loadMovieCards({ commit }) {
      const {
        data: { results },
      } = await axios({
        methods: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: process.env.VUE_APP_MOVIE_API,
          language: 'ko-KR',
        },
      })

      commit('LOAD_MOVIE_CARDS', results)
    },
  },
  modules: {},
})

import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todos: []
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      //console.log(state)
      //console.log(todoItem)
      state.todos.push(todoItem) // state 변경
    },
    DELETE_TODO: function(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          return {
            ...todo, // JS spread syntax
            isCompleted: !todo.isCompleted
          }
        } else {
          return todo
        }
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      //console.log(context)
      //console.log(todoItem)
      //console.log(state)
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    }
  },
  modules: {
  }
})

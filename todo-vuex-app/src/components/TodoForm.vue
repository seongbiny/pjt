<template>
  <div>
    <input 
      type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo: function () {
      //console.log('Todo create!!!')
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      //this.$store.commit('CREATE_TODO', todoItem)
      if (todoItem.title) {
        this.$store.dispatch('createTodo', todoItem) // actions 호출
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>
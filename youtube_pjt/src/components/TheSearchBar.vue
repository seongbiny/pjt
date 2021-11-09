<template>
  <div>
    <input type="text" @keyup.enter="onInputKeyword">
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods: {
    onInputKeyword: function (event) {
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>

</style>
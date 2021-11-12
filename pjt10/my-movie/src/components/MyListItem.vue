<template>
  <div>
    {{ movie.title }}
  </div>
</template>

<script>
export default {
  name: "MyListItem",
  props: {
    movie: Object
  }
}
</script>

<style>

</style>
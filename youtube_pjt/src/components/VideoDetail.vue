<template>
  <div v-if="video">
    <div>
      <iframe :src="videoURI" frameborder="0"></iframe>
    </div>
    <h2>{{ videoTitle | stringUnescape }}</h2>
    <hr />
    <p>{{ video.snippet.description | stringUnescape }}</p>
  </div>
</template>

<script>
import _ from "lodash";

export default {
  name: "VideoDetail",
  props: {
    video: {
      type: Object,
    },
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId;
      return `https://www.youtube.com/embed/${videoId}`;
    },
    videoTitle: function (video) {
      return _.unescape(video.snippet.title);
    },
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText);
    },
  },
};
</script>

<style></style>

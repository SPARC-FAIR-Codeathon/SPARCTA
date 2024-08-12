# Minimal vue component for SPARCTA viewer
<template>
  <div id="openseadragon" ref="viewer"></div>
</template>

<script>
export default {
  mounted() {
    const viewer = OpenSeadragon({
      element: this.$refs.viewer,
      prefixUrl: "/openseadragon/images/",
      tileSources: "example.dzi"
    });

    Annotorious(viewer);
  }
}
</script>

<style scoped>
#openseadragon {
  width: 100%;
  height: 500px;
}
</style>
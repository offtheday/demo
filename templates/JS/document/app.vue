<template>
  <div id="app">
    <div id="map" style="width:100%;height:500px"></div>
  </div>
</template>

<script>
import MindElixir, { E } from "mind-elixir";

export default {
  name: "App",
  data() {
    return {
      ME: null
    };
  },
  mounted() {
    this.ME = new MindElixir({
      el: "#map",
      direction: MindElixir.LEFT,
      data: MindElixir.new("new topic"),
      draggable: true, // default true
      contextMenu: true, // default true
      toolBar: true, // default true
      nodeMenu: true, // default true
      keypress: true // default true
    });
    this.ME.init();
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

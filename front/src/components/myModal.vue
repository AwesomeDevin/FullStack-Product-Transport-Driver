<style type="text/css">
    h1{
        color:black;
    }
</style>
<template>
  <div class="page-content padding padding-top">
    <p>
      我有一只小毛驴我从来也不骑。
    </p>

    <button v-if="!showMore" class="button button-assertive button-small" @click="more()">show more</button>
    <p v-if="showMore">
      有一天我心血来潮骑它去赶集。
    </p>

  </div>
</template>
<script>
  export default {
    data() {
      return {
        showMore: false
      }
    },

    methods: {
      more() {
        this.showMore = true
      }
    }
  }
</script>
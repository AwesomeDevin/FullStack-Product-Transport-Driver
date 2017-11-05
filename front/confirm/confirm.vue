<style type="text/css" >

  #layer{
    position: fixed;
    width: 100%;
    height: 100%;
    background: black;
    transition: all 0.3s;
    /*display: none;*/
    top:0;
    left: 0;
    color:white;
    opacity: 0;
    z-index: -1;
    background: rgba(0,0,0,0.9);
  }
  #layer.active{
    /*display: block;*/
    opacity: 1;
    z-index: 10000;
  }
  .icon{
    width: 100%;
    height:1rem;
     text-align: center;
    display: table;
  }
  .icon i.fa
  {
    display: table-cell;
    vertical-align: bottom;
    color:white;
    font-size: 0.5rem;

  }
  #layer h5{
    color:white;
    font-size: 0.16rem;
    text-align: center;
    padding: 0 0.5rem;
    font-family: "黑体";
    margin-bottom: 0.8rem;
  }
   #layer h3{
    color:white;
    font-size: 0.3rem;
    padding: 0 0.5rem;
    text-align: center;
    /*letter-spacing: 0.1rem;*/
    font-family: "黑体";
    margin-bottom: 0.8rem;
  }
  #layer .confirm{
    width: 100%;
    height: 1rem;
    display: flex;
    justify-content: space-around;
  }
  #layer .confirm button{
    border:0;
    background: transparent;
    color:white;
    border:1px solid white;
    width: 0.8rem;
    height: 0.8rem;
    border-radius: 50%;
    font-size: 0.5rem;
  }
  #layer .confirm button:nth-child(1){
    border:1px solid #27ae60;
    color:#2ecc71;
  }
  #layer .confirm button:nth-child(2){
    border:1px solid #e74c3c;
    color:#e74c3c;
  }
</style>
<template>
  <div id="layer" :class="show?'active':''">
    <div class="icon">
    <i class="fa fa-check-circle" aria-hidden="true"></i>
    </div>
    <h5>{{title?title:'Are you sure you want to do this?'}}</h5>
    <h3>{{text?text:'what do you think?'}}</h3>
    <div class="confirm">
      <button @click="ok"> <i class="fa fa-heart" aria-hidden="true"></i></button>
      <button @click="closed"> <i class="fa fa-times" aria-hidden="true"></i></button>

    </div>
  </div>
</template>
<script>
// use bluebird instead
// import $ from 'jquery';
// import { modal } from 'vue-strap';
import eventbus from './eventbus';
export default {
  name: 'vconfirm',
  components: [
    // modal,
  ],
  data() {
    return {
      show: false,
      promise: null,
      title: '',
      text: '',
    };
  },
  methods: {
    open(p) {
      this.title = p.title;
      this.text = p.text;
      // this.promise = $.Deferred();
      // return this.promise;
    },
    ok() {
      // this.promise.resovle(true);
      this.show = false;
      eventbus.$emit('vconfirm-close', true);
    },
    closed() {
      eventbus.$emit('vconfirm-close', false);
      this.show = false;
    },
    cancel() {
      // this.promise.resovle(false);
      this.show = false;
      // eventbus.$emit('close', false);
    },
  },
  created() {
    eventbus.$on('vconfirm-open', (event) => {
      this.open(event);
      this.show = true;
    });
  },
};
</script>
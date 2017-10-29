import Vue from 'vue';
import Vuex from 'vuex';
import io from 'socket.io-client';

Vue.use(Vuex);
const store = new Vuex.Store({
  state: {
    userInfo:{
        userName:'邓大达',
        tel:'13145950323',
        head_img:null,
        car:'粤A0062'
      },
  },
  mutations: {
    
  },
  getters:{
    socketObj(){
        return io('http://localhost:3000');
    }
  },
});

export default store;
import Vue from 'vue';
import Vuex from 'vuex';
import io from 'socket.io-client';

Vue.use(Vuex);
const store = new Vuex.Store({
  state: {
    
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
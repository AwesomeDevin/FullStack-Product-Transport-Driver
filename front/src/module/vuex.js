import Vue from 'vue';
import Vuex from 'vuex';
import io from 'socket.io-client';

Vue.use(Vuex);
const store = new Vuex.Store({
  state: {
    userInfo:{
        name:'未设置',
        tel:null,
        head_img:null,
        car:'未设置',
        money:null,
      },
    imgFile:null,
  },
  mutations: {
    increment(state,data){
      if(!data)
      {
         state.userInfo.tel='';
         state.userInfo.id=null;
         return;
      }
      if(data.name)
      {
        state.userInfo.name=data.name;
      }
      if(data.tel)
      {
        state.userInfo.tel=data.tel;
      }
      if(data.user_img)
      {
        state.userInfo.head_img=data.user_img;
      }
      if(data.car_plate)
      {
      state.userInfo.car=data.car_plate;
      }
      if(data.id)
      {
        state.userInfo.id = data.id;
      }
      if(data.money)
      {
        state.userInfo.money = data.money;
      }
      
      console.log(state.userInfo,data);
    },
    chooseImg(state,data){
      state.imgFile = data;
    },
    modifyImg(state,data)
    {
      state.userInfo.head_img = data;
    }
  },
  getters:{
    socketObj(){
        return io('http://localhost:3000');
    },
  },

});

export default store;
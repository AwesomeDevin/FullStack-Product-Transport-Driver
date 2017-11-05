<template>

  <div class="page ">
    <div class="page-content text-center">
     <div class="main">
        <von-header theme="dark">
    <!-- <button class="button button-icon ion-ios-arrow-back" slot="left"></button> -->
    <p class="action" slot="title">Tohcart</p>
    <!-- <button class="button button-icon ion-navicon" slot="right"></button> -->
  </von-header>
       <ul>
         <router-link to="/order/mine"><li><div><i class="ion-clipboard"></i></div><div><p>订单查看</p></div></li></router-link>
         <router-link to="/customer"><li><div><i class="ion-person-stalker"></i></div><div><p>我的用户</p></div></li></router-link>
         <router-link to="/chart"><li><div><i class="ion-ios-pie-outline"></i></div><div><p>盈收图表</p></div></li></router-link>
         <router-link to="/sidemenu"><li><div><i class="ion-gear-b"></i></div><div><p>账户设置</p></div></li></router-link>
       </ul>
     </div>
    </div>
  </div>
</template>
<script>
import {VonHeader} from 'vonic/src/index.js'
// import io from 'socket.io-client';
  export default {
    data () {
      return {
        msg: 'Hello! Vonic.'
      } 
    },
    components:{
        'von-header':VonHeader,
    },
    created(){
      // const socket = io('http://localhost:3000');
      // socket.on('client-newOrder',(data)=>{
      //   console.log(data);
      // });
    }
  }
</script>
<style scoped lang='less'>
  ul a{
    color:white;
    text-decoration: none;
  }
  h2 {
    font-family: Candara,Calibri,Segoe,Segoe UI,Optima,Arial,sans-serif;
    color: #888;
  }
  .has-navbar{
    background:none;
    background-size: cover;
    /*filter: blur(3px);   */
  }
  .titile{
    line-height:0.44rem;
  }

  h3 {
    font-family: Candara,Calibri,Segoe,Segoe UI,Optima,Arial,sans-serif;
    line-height: 150px;
    color: #fff;
  }
  .main{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction:column;
    background: linear-gradient(-45deg, #f9ad49, #f78e1e, #e84444);

    .bar-header{
      height: 0.44rem;
      position: relative;
      background: rgba(104, 100, 124, 0.2);
    }
  }
  ul{
    width: 100%;
    flex:1;
  }
  ul li{
    width: 100%;
    height: 25%;
    display: block;
    color:white;
    display: flex;
    div:nth-child(1){
      display: flex;
      align-items:center;
      justify-content:center;
    }
     div:nth-child(2){
      display: flex;
      align-items:center;
      justify-content:center;
      p{
        border-bottom: 1px solid white;
      }
    }
    div{
      width: 50%;
      height: 100%;
      i{
        font-size: 0.5rem;

      }
    }
  }
  ul a:nth-child(1) li{
    background-color: #1abc9c;
  }
    ul a:nth-child(2) li{
    background-color: #3498db;
  }
    ul a:nth-child(3) li{
    background-color:rgba(45, 167, 112, 0.91);
  }
    ul a:nth-child(4) li{
    background-color:rgba(67, 67, 89, 0.91);
  }
  .page{
    background: transparent;
  }

.page .page-content, .modal .page-content {
      position: relative;
     background-color: transparent;
     height: 100%;

  }

</style>

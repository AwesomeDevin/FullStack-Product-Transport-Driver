<style type="text/css" scoped lang='less'>
    *{
        font-family: "黑体";
    }
    .order{
        background: linear-gradient(to bottom, rgb(78, 75, 75),#1abc9c);
        // background: rgba(0,0,0,0.1);
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        right: 0;
        header{
            width: 100%;
            line-height: 0.44rem;
            text-align: center;
            font-size: 0.16rem;
            color:white;
            position: relative;
            button{
                position: absolute;
                top: 50%;
                border:0;
                background: none;
                color:white;
                transform:translateY(-50%);
                height: 0.44rem;
                display: flex;
                align-items:center;
                i{
                    font-size: 0.25rem;
                    padding: 0 0.05rem;
                }
            }
        }
    }
    nav {
        width: 3rem;
        height: 0.3rem;
        box-sizing: border-box;
        margin: 0 auto;
        border-radius: 1em;
        overflow: hidden;
        display: flex;
        p{
           
            margin:0;
            height: 0.3rem;
            box-sizing: border-box;
            width: 1rem;
            line-height: 0.3rem;
            text-align: center;
            color: white;
            display: inline-block;
            position: relative;
            span{
                border-width: 0.02rem;
                border-style: solid;
                border-color: rgba(0,0,0,0.3);
                display: block;
                height: 0.3rem;
                line-height: 0.26rem;
                position: relative;
                color:white;
            }
            span i{
                display: block;
                position: absolute;
                background: rgba(0,0,0,0.3);
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
            }
            span.active{
                overflow: hidden;
            }
            span.active i{
                background:transparent;
                border-radius:1em;
                box-shadow: 0 0 0px 10px rgba(0,0,0,0.3);
            }
        }
    }
    hr{
        background:rgba(255,255,255,0.4);
        height: 1px ;
        width: 100%;
        border:0;
    }
    hr:nth-of-type(2){
        margin-top: 0;
    }
   
</style>
<template>
   <div class="order">
     <header><button @click="back"><i class="ion-ios-arrow-back"></i>返回</button>订单</header>
     <nav><p v-for="(item,index) in tab" @click="tabSwitch(index)" ><span :class="tabIndex==index?'active':''">{{item}}<i></i></span></p></nav>
     <hr/>
     <router-view>

    </router-view>
     <hr/>
   </div>
</template>
<script type="text/javascript">
import {VonHeader} from 'vonic/src/index.js'
    export default{
        name:'order',
        data(){
            return{
                tab:['我的订单','挑选订单','Undetermined'],
                tabIndex:null,
                orderList:[{duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes()}],
            }
        },
        components:{
        'von-header':VonHeader,
        },
        methods:{
            tabSwitch(index){
                this.tabIndex = index;
                if(index==0)
                {
                    this.$router.push('/order/mine');
                }
                else if(index==1)
                {
                    this.$router.push('/order/search');
                }
            },
            back(){
                this.$router.push('/Index');
            }
        },
        created(){
            if(this.$route.path=='/order/mine')
            {
                this.tabIndex='0';
            }
            else if(this.$route.path=='/order/search')
            {
                this.tabIndex='1';
            }
            if(!this.$store.state.userInfo.tel||this.$store.state.userInfo.tel.length<1)
            {
                this.$router.push('/intro/welcome');
            }
        }
    }
</script>
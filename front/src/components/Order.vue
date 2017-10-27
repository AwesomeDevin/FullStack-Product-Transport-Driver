<style type="text/css" scoped lang='less'>
    *{
        font-family: "黑体";
    }
    .order{
        background:rgba(0,0,0,0.1);
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
    section{
        width: 100%;
        height: 4.79rem;
        box-sizing: border-box;
        padding-left: 0.37rem;
        position: relative;
        overflow-y: auto;
        .user_box{
            margin-left: -0.27rem;
            width: 100%;
            overflow: hidden;
            padding-top: 0.1rem;
            display: flex;
            align-items:center;
            img{
                width: 0.54rem;
                height: 0.54rem;
                border-radius: 50%;
                margin-right: 0.1rem;
            }
            p{
                margin: 0;
                font-size: 0.14rem;
                color:#ded3d3;
            }
        }
    }
    // section:after{
    //     content: '';
    //     position: absolute;
    //     left: 0.37rem;
    //     width: 1px ;
    //     height: 100%;
    //     top: 0.64rem;
    //     background: rgba(255,255,255,0.4);
    // }
    .order_box{
        width: 100%;
        border-left: 1px solid rgba(255,255,255,0.4);
        border-bottom: 1px solid rgba(255,255,255,0.4);
        padding-bottom: 0.2rem;
    }
    .item:before{
        content: '';
        display: block;
        position: absolute;
        left: -0.12rem;
        top: 0.2rem;
        border:6px solid transparent;
        border-right: 6px solid white;
    }
    .item:after{
        content: '';
        display: block;
        position: absolute;
        left: -0.23rem;
        top: 0.2rem;
        width: 0.1rem;
        height: 0.1rem;
        background: white;
        border-radius: 50%;
        box-shadow: 0 0 0.2rem white;
        
    }
    .item{
        overflow: initial;
        padding: 0;
        position: relative;
        margin:0 0.17rem;
        border-radius: 0.25em;
        margin-bottom: 0.25rem;
        h5{
            padding: 0.1rem 0.05rem 0 0.1rem;
            font-size: 0.13rem;
        }
        .content{
            width: 100%;
            overflow: hidden;
            div{
               
            }
            .place{
                padding: 0.16rem;
                width: 100%;
                border-bottom: 1px solid #e4e4e4;
                p{
                    font-size: 0.12rem;
                    color:#111;
                    margin:0;
                    width: 100%;
                    font-family: "黑体"
                }
                p:nth-of-type(1) i{
                    display: inline-block;
                    width: 0.11rem;
                    height: 0.11rem;
                    border-radius: 50%;
                    border:0.02rem solid #2ecc71;
                    margin-right:0.05rem;
                }
                p:nth-of-type(2) i{
                    display: inline-block;
                    width: 0.11rem;
                    height: 0.11rem;
                    border-radius: 50%;
                    border:0.02rem solid #e74c3c;
                    margin-right:0.05rem;
                }
                hr{
                    background: #e4e4e4;
                }
            }
            .info{
                width: 100%;
                div{
                    width: 50%;
                    height: 0.7rem;
                    float: left;
                    box-sizing: border-box;
                    position: relative;
                }
                div:nth-of-type(1){
                    border-right: 1px solid #e4e4e4;
                    line-height: 0.7rem;
                    text-align: center;
                }
                div:nth-of-type(2){
                    border-right: 1px solid #e4e4e4;
                    padding-top: 0.25rem;
                    text-align: center;
                    p{
                        margin:0.05rem 0;
                    }
                }
                span.icon{
                        position: absolute;
                        left: 0.1rem;
                        top: 0.05rem;
                       line-height: 0.2rem;
                       i{
                        padding-right:0.05rem;
                       }
                    }
            }
        }
    }
</style>
<template>
   <div class="order">
     <header><button @click="back"><i class="ion-ios-arrow-back"></i>返回</button>订单</header>
     <nav><p v-for="(item,index) in tab" @click="tabSwitch(index)" ><span :class="tabIndex==index?'active':''">{{item}}<i></i></span></p></nav>
     <hr/>
     <section>
         <div class="user_box">
             <img src="../static/img/5.jpg"/>
             <div>
                 <p>myName</p>
                 <p>myNumber</p>
             </div>
         </div>
         <div class="order_box">
             <div v-for="item in orderList" class="item">
                <h5>距离:{{item.distance?item.distance+" Km":""}}  耗时:{{item.duration?parseInt(item.duration/60)+" min":""}}</h5>
                 <div class="content">
                     <div class="place">
                         <p><i></i>{{item.startSite}}</p>
                         <hr/>
                         <p><i></i>{{item.endSite}}</p>
                     </div>
                     <div class="info">
                         <div class="time">
                             <span class="icon"><i class="ion-clock"></i>Set Time</span>
                             {{item.date}}
                         </div>
                         <div class="user">
                             <span class="icon"><i class="ion-person"></i>Userinfo</span>
                             <p>{{item.username}}</p>
                             <p>{{item.tel}}</p>
                         </div>
                     </div>
                 </div>
             </div>
         </div>
     </section>
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
                tabIndex:'0',
                orderList:[{duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes()}],
            }
        },
        components:{
        'von-header':VonHeader,
        },
        methods:{
            tabSwitch(index){
                this.tabIndex = index;
            },
            back(){
                this.$router.push('/Index');
            }
        },
        created(){
            var self = this;
            this.$store.getters.socketObj.on('server-newOrder',function(data){
                console.log('new Order',data);
                self.orderList.push(data);
                console.log(self);
            })
        }
    }
</script>
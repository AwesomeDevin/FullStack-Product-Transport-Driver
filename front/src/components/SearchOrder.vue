<style type="text/css" scoped lang='less'>
    section::-webkit-scrollbar  {
        width: 0.01rem;
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
                border:1px solid #736954;
            }
            p{
                margin: 0;
                font-size: 0.14rem;
                color:#ded3d3;
            }
        }
    }
    
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
    .item.accepted:after
    {
        background:linear-gradient(45deg, #5e5858, #19959c, #1d507e);
    }
    .item.accepted .ion-ios-checkmark
    {
        display: none;
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
    hr{
        background:rgba(255,255,255,0.4);
        height: 1px ;
        width: 100%;
        border:0;
    }
    .item{
        overflow: initial;
        padding: 0;
        position: relative;
        margin:0 0.17rem;
        border-radius: 0.25em;
        margin-bottom: 0.2rem;
        h5{
            padding: 0.1rem 0.05rem 0 0.1rem;
            font-size: 0.13rem;
            display: flex;
            align-items:center;
            justify-content: space-between;
            .ion-ios-checkmark{
                font-size: 0.2rem;
                float: right;
                padding: 0 0.05rem;
                color:#e7761d;
            }
        }
        .content{
            width: 100%;
            overflow: hidden;
            div{
               
            }
            .place{
                padding: 0.16rem;
                width: 100%;
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
                    border:0.02rem solid #3498db;
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
                overflow:hidden;
                border-top: 1px solid #e4e4e4;
                background: linear-gradient(45deg, #5e5858, #19959c, #1d507e);
                div{
                    width: 50%;
                    height: 0.7rem;
                    float: left;
                    box-sizing: border-box;
                    position: relative;
                    color:white;
                }
                .user p{
                    color:white;
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
         <section>
         <div class="user_box">
             <img src="../static/img/5.jpg"/>
             <div>
                 <p>myName</p>
                 <p>myNumber</p>
             </div>
         </div>
         <div class="order_box">
             <div v-for="item in orderList" class="item accepted">
                <h5>距离:{{item.distance?item.distance+" Km":""}}  耗时:{{item.duration?parseInt(item.duration/60)+" min":""}} <i class="ion-ios-checkmark"></i></h5>
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
</template>
<script >
    export default{
        name:'order',
        data(){
            return{
                tab:['我的订单','挑选订单','Undetermined'],
                tabIndex:'0',
                orderList:[{duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'30￥',status:'appoint'},{duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'30￥',status:'success'},{duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'30￥',status:'cancel'}],
            }
        },
        methods:{
        },
        created(){
            var self = this;
            this.$store.getters.socketObj.on('server-newOrder',function(data){
                console.log('new Order',data);
                self.orderList.push(data);
            })
        }
    }
</script>
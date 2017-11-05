<style type="text/css" scoped lang="less">
    .box{
        width: 100%;
        overflow: hidden;
        padding: 0 0.2rem;
    }
    .order.success .upper_part{
        background: #27ae60;
        
    }
    .order.success .bottom_part .spot p:nth-child(1){
        color: #27ae60;
    }
    .order.cancel .upper_part{
        background: linear-gradient(45deg, #672828, #ac4949, #e84444);
         
    }
    .order.cancel .bottom_part .spot p:nth-child(1){
        color: #c0392b;
    }
    .order.success .upper_part{
        background: linear-gradient(45deg, #28675c, #49ac96, #44e88f);
        
    }
    .order.success .bottom_part .spot p:nth-child(1){
        color: #27ae60;
    }
    .order.appoint .upper_part{
        background: linear-gradient(45deg, #112533, #076ad5, #1e3559);
         
    }
    .order.appoint .bottom_part .spot p:nth-child(1){
        color: #3498db;
    }
    .order{
        width: 100%;
        overflow: hidden;
        margin:0.1rem 0;
        border-radius: 0.25em;
        // border:1px solid white;
        .upper_part{
             width: 100%;
            height: 0.6rem;
            padding: 0 0.15rem;
            display: flex;
            align-items:center;
            justify-content:space-between;
            p{
                font-family: "微软雅黑";
                color:white;
                margin:0;
            }
            p:nth-child(1){
                font-size: 0.2rem;
            }
            p:nth-child(2){
                font-size: 0.16rem;
                color:#ccc;
                text-align: center;
            }
            span{
                display: block;
                color:white;
            }
        }
        .bottom_part{
             width: 100%;
            height: 0.6rem;
            background: white;
            display: flex;
            align-items:center;
            justify-content:space-between;
            .spot,.user{
                float: left;
            }
            .spot{
                width: 80%;
                height: 100%;
                display: flex;
                flex-direction:column;
                justify-content:center;
                p{
                    margin:0;
                    text-indent: 0.05rem;
                    font-size: 0.13rem;
                    overflow: hidden;
                    text-overflow:ellipsis;
                    white-space: nowrap;
                    // line-height: 0.3rem;
                    i{
                        padding: 0 0.08rem;
                    }
                }
            }
            .user{
                width: 20%;
                height: 100%;
                button{
                    
                    border:0;
                    width: 90%;
                    padding: 0.02rem 0rem;
                    margin-top: 0.05rem;
                    border-radius: 1em;
                   color:white;
                }
                button.cancel{
                    background: linear-gradient(0deg, #672828, #ac4949, #e84444);
                }
                button.success{
                    background:linear-gradient(45deg, #28675c, #49ac96, #44e88f);
                }
            }
        }
    }
     img.herder_img{
                width: 0.46rem;
                height: 0.46rem;
                border-radius: 50%;
                border:1px solid #736954;
            }
    #myorder{
        width: 100%;
        height: 4.79rem;
        overflow-y: auto;
    }
</style>
<template>
    <div id="myorder">
    <div class="box">

        <div v-for="item in orderList" class="order" :class="(item.status=='done'?'success':'')+(item.status=='cancel'?'cancel':'')+(item.status=='doing'?'appoint':'')">
            <div class="upper_part">
                <img class="herder_img" :src="item.head_img"/>
                <div>
                    <span style="font-family: '微软雅黑';font-size:0.18rem;">￥{{item.price}}</span>
                </div>
                <div>
                    <span>{{item.username}}</span>
                    <span>{{item.tel}}</span>
                </div>
                <div>
                    <p>{{item.income}}</p>
                    <p>{{(item.status=='done'?'成功':'')+(item.status=='cancel'?'取消':'')+(item.status=='doing'?'进行中':'')}}</p>
                </div>
            </div>
            <div class="bottom_part">
                <div class="spot">
                    <p><i class="ion-ios-clock-outline"></i>{{item.date}}</p>
                    <p><i class="ion-ios-location-outline"></i>{{item.endSite}}</p>
                </div>
                <div class="user">
                    <button class="success" @click="finish(item)" v-if="item.status=='doing'">完成</button>
                    <button class="cancel"  @click="cancel(item)" v-if="item.status=='doing'">取消</button>
                    <button class="success"   v-if="item.status=='done'">添加</button>
                </div>
            </div>

        </div>
    </div>
    <confirm></confirm>
</div>
</template>
<script type="text/javascript">
    export default{
        name:'myorder',
        data(){
            return{
                // orderList:[{url:'src/static/img/5.jpg',duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'￥30',status:'appoint'},{url:'src/static/img/5.jpg',duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'￥30',status:'success'},{url:'src/static/img/5.jpg',duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'￥30',status:'cancel'}]
                orderList:[],
                userInfo:null,
            }
        },
        mounted(){
            $loading.show();
            this.initOrder();
            this.userInfo = this.$store.state.userInfo;
        },
        methods:{
            initOrder(){
                this.$http.get('http://localhost:4040/api/transport/user/get_user_order/?tel='+this.$store.state.userInfo.tel).then(function(res){
                    console.log(res.data);
                    $loading.hide();
                    this.orderList = res.data;
                },function(res){
                    $loading.hide();
                    console.log(res.status);
                });
            },
            finish(item){
                const params={
                    title:"Are you sure you want to do this?",
                    text:"请求结算?",
                    execute:this.finishOrderInfo,
                    upload:item,
                };
                this.$confirm(params);
            },
            cancel(item){
                const params={
                    title:"Are you sure you want to do this?",
                    text:"确认取消该单吗",
                    execute:this.cancelOrderInfo,
                    upload:item,
                };
                this.$confirm(params);
            },
            finishOrderInfo(item){
                console.log('coming',item._id);
                var self = this;
                var data = {
                    _id:item._id,
                    accept_user:this.userInfo.name,
                    accept_tel:this.userInfo.tel,
                    accept_car:this.userInfo.car,
                    accept_header_img:this.userInfo.head_img,
                    status:'done',
                }
                $loading.show();
                this.$http.post('http://localhost:4040/api/transport/user/update_order/',data).then(function(res){
                    $loading.hide();
                   $toast.show('结算成功',500);
                   for(var index in self.orderList)
                   {
                        if(self.orderList[index]._id==item._id)
                        {
                            self.orderList[index].status='done';
                            break;
                        }
                   }
                },function(res){
                   $toast.show('状态更新失败',500);
                });
            },
            cancelOrderInfo(item){
                console.log('coming',item._id);
                var self = this;
                var data = {
                    _id:item._id,
                    accept_user:this.userInfo.name,
                    accept_tel:this.userInfo.tel,
                    accept_car:this.userInfo.car,
                    accept_header_img:this.userInfo.head_img,
                    status:'cancel',
                }
                $loading.show();
                this.$http.post('http://localhost:4040/api/transport/user/update_order/',data).then(function(res){
                    $loading.hide();
                   $toast.show('状态已更新',500);
                   for(var index in self.orderList)
                   {
                        if(self.orderList[index]._id==item._id)
                        {
                            self.orderList[index].status='cancel';
                            break;
                        }
                   }
                },function(res){
                   $toast.show('状态更新失败',500);
                });
            },
        },
    }
</script>
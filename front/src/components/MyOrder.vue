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
                    padding: 0.03rem 0rem;
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
</style>
<template>
    <div class="box">

        <div v-for="item in orderList" class="order" :class="(item.status=='success'?'success':'')+(item.status=='cancel'?'cancel':'')+(item.status=='appoint'?'appoint':'')">
            <div class="upper_part">
                <img class="herder_img" :src="item.url"/>
                <div>
                    <span>{{item.username}}</span>
                    <span>{{item.tel}}</span>
                </div>
                <div>
                    <p>{{item.income}}</p>
                    <p>{{(item.status=='success'?'成功':'')+(item.status=='cancel'?'取消':'')+(item.status=='appoint'?'进行中':'')}}</p>
                </div>
            </div>
            <div class="bottom_part">
                <div class="spot">
                    <p><i class="ion-ios-clock-outline"></i>{{item.date}}</p>
                    <p><i class="ion-ios-location-outline"></i>{{item.endSite}}</p>
                </div>
                <div class="user">
                    <button class="cancel" v-if="item.status=='cancel'">取消</button>
                    <button class="success" v-if="item.status=='success'">添加</button>
                </div>
            </div>

        </div>
    </div>
</template>
<script type="text/javascript">
    export default{
        name:'myorder',
        data(){
            return{
                orderList:[{url:'src/static/img/5.jpg',duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'￥30',status:'appoint'},{url:'src/static/img/5.jpg',duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'￥30',status:'success'},{url:'src/static/img/5.jpg',duration:100,distance:100,endSite:"广东省广州市天河区恒隆街47号",startSite:"广东省广州市天河区潭村路204号",tel:'13145950323',username:'邓大大',date:new Date().getFullYear()+"/"+new Date().getMonth()+"/"+new Date().getDay()+" "+new Date().getHours()+":"+new Date().getMinutes(),income:'￥30',status:'cancel'}]
            }
        }
    }
</script>
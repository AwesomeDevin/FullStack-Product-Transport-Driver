<style type="text/css" scoped lang='less'>
.sidemenu{
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction:column;
    background: linear-gradient(to bottom, rgb(89, 83, 83),rgba(45, 167, 112, 0.91));
}
.bar-header{
    background: transparent;
    position: relative;
    height: 0.44rem;
    p{
        line-height: 0.44rem;
        height: 0.44rem;
        color:white;
    }
}
.content{
    display: flex;
    flex-direction:column;
    height: 100%;
    flex:1;
    overflow-y: auto;
}
.content img{
    width: 0.4rem;
    height: 0.4rem;
    border-radius: 50%;
    border:1px solid #736954;
    display: block;
}
.content p{
    margin:0;
    color:white;
    
}
.bar-light .button.button-icon{
    color:white;
}
.main{
    flex:1;
    // background: linear-gradient(to bottom, rgba(0, 0, 0, 0),#3498db);
}
.content{
    padding-top: 0.05rem;
    ul li{
        float: left;
        color:white;
        width: 33.3%;
        text-align: center;
        button{
            background: transparent;
            border:1px solid #16a085;
            color:white;
            width: 0.8rem;
            padding: 0.05rem 0.1rem;
            border-radius: 1em;
        }
        button.active{
            background: #1abc9c;
        }
    }
}

</style>
<template>
<div class="sidemenu">
     <von-header >
    <button @click="goBack" class="button button-icon ion-ios-arrow-back" slot="left"></button>
        <p class="action" slot="title">盈收图表</p>
        <!-- <button class="button button-icon ion-navicon" slot="right"></button> -->
      </von-header>
    <div class="content">
        <ul class="nav">
            <li><button class="active">上个月</button></li>
            <li><button>本月</button></li>
            <li><button>选择月份</button></li>

        </ul>
        <div class="chart">
            <echart ref="echart" :auto-resize="true" :options="lineParams"></echart>
        </div>
    </div>
</div>
</template>

<script type="text/javascript">
// import bus from '../module/bus';
// import g from '../module/global';
import Vue from 'vue';
import ECharts from 'vue-echarts/components/ECharts.vue'
import {VonHeader} from 'vonic/src/index.js'
require('echarts/lib/chart/line')
require('echarts/lib/component/tooltip')

export default{
    watch:{
    },
    name:'Chart',
    data(){
        return{
            userInfo:null,
            data:['01','02','03','04','05','06','07','08'],
           
        }
    },
    components:{
        'von-header':VonHeader,
        'echart': ECharts,
        


    },
    computed:{
        width (){
            return 200;
        },
        dateList(){
            var arr=[];
            this.data.map((item)=>{
                arr.push(item[0])
            })
            return arr;
        },
        valueList(){
            var arr=[];
            this.data.map((item)=>{
                arr.push(item[1])
            })
            return arr;
        },
        lineParams(){
            return  {
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        animation: true
                    }
                },
                legend: {
                    data:['流量'],
                    x: 'center'
                },

                
                grid: {
                    left:'10%',
                    height: '80%',
                    top:'15%',
                    width:'80%',
                }, 
                xAxis : [
                    {
                        type : 'category',
                        boundaryGap : false,
                        axisLine: {onZero: true},
                        data: this.data
                    },
                   
                ],
                yAxis : [
                    {
                        name : '收入(￥)',
                        type : 'value',

                        
                    },
                   
                ],

                series : [
                    {
                        name:'流量',
                        type:'line',
                        symbolSize: 8,
                        hoverAnimation: false,
                        data:[
                            0.97,0.96,0.96,0.95,0.95,0.94,0.94,0.94
                        ]
                    },
                ]
            };
        }
    },
    methods:{

        goBack(){
            
            this.$router.push('/Index');
        }
    },
    mounted(){
        this.userInfo = this.$store.state.userInfo;
        console.log(this.$refs.echart.$el.offsetWidth);
        // bus.$on('getUserInfo',function(data){
        //  for(var key in data)
        //  {
        //      Vue.set(this.userInfo,key,data[key]);
        //  }
        //  console.log('sideMenu',this.userInfo);
        // })
        
        // this.userInfo.head_img = 'src/assets/logo.png';
        // this.userInfo.tel='13145950323';
        // this.userInfo.username = 'Tohcart';
    }
}
</script>
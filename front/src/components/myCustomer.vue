<style type="text/css" scoped lang='less'>
.sidemenu{
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction:column;
    background: linear-gradient(to bottom, rgba(122, 119, 119, 0.91), rgba(67, 124, 131, 0.91));
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
.info{
    // background: linear-gradient(to bottom, rgba(0, 0, 0, 0),#3498db);
    ul li{
        width: 33.3%;
        float: left;
        padding:0.15rem 0;

    }

}
.item{
    background: transparent;
    color:white;
    border:0;
}
.hairline-bottom:after{
    background-color: #625e5e;
}
.hairline-bottom:before{
    background-color: #625e5e;
}
ul{
    width: 100%;
    height: 100%;
    padding: 0.15rem 0.25rem 0.15rem 0.25rem;
    li{
        width: 100%;
        height: 0.58rem;
        display: flex;
        // justify-content:space-between;
        align-items:center;
        position: relative;
        overflow: hidden;
        div p{
            text-indent: 0.1rem;
        }
        .badge{
            color:white;
            background: #3498db;
            text-align: center;
            border-radius: 0;
            display: inline-block;
            width: 0.4rem;
            padding: 1px 5px;
        }
        div:nth-of-type(1){
            p:nth-of-type(2){
                color:#ccc;
            }
        }
        div:nth-of-type(2){
            flex:1;
            p:nth-of-type(2){
                text-align: center;
            }
            p:nth-of-type(1){
                color:#ccc;
                text-align: right;
            }
        }
    }
    li:after{
        content: '';
        display: block;
        width: 100%;
        position: absolute;
        height: 1px;
        // left: 0.5rem;
        bottom:0;
        background: #e5e5e5;
        transform:scaleY(0.5);
    }
    li:nth-last-of-type(1):after{
        display: none;
    }
}
</style>
<template>
<div class="sidemenu">
     <von-header >
    <button @click="goBack" class="button button-icon ion-ios-arrow-back" slot="left"></button>
        <p class="action" slot="title">我的用户</p>
        <!-- <button class="button button-icon ion-navicon" slot="right"></button> -->
      </von-header>
    <div class="content">
        <div class="main">
            <ul>
                <li>
                    <img src="../static/img/1.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/2.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/3.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/4.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/5.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/1.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/2.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/3.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/4.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>
                <li>
                    <img src="../static/img/5.jpg"/>
                    <div>
                        <p>13145953244,<span>粤A0062</span></p>
                        <p>邓大达</p>
                    </div>
                    <div>
                        <p>成交量</p>
                        <p><i>1</i></p>
                    </div>
                </li>

            </ul>
        </div>
    </div>
</div>
</template>

<script type="text/javascript">
// import bus from '../module/bus';
// import g from '../module/global';
import Vue from 'vue';
import {VonHeader} from 'vonic/src/index.js'
import {List,Item} from 'vonic/src/index.js'

export default{
    watch:{
    },
    name:'sideMenu',
    data(){
        return{
            userInfo:null,
        }
    },
    components:{
        'von-header':VonHeader,
        'von-list':List,
        'von-item':Item,


    },
    methods:{
        clickBody(){
            
        },
        logout(){
            
        },
        goBack(){
            
            this.$router.push('/Index');
        }
    },
    created(){
        this.userInfo = this.$store.state.userInfo;
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
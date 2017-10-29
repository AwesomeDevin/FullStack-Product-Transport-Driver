<style type="text/css" scoped lang='less'>
.sidemenu{
	position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
}
.bar-header{
	background: transparent;
	position: relative;
	p{
		color:white;
	}
}
.content{
	display: flex;
	flex-direction:column;
	height: 100%;
}
.content img{
	width: 0.54rem;
	height: 0.54rem;
	border-radius: 50%;
	margin:0.15rem auto;
	display: block;
}
.content p{
	margin:0;
	color:white;
	text-align: center;
}
.bar-light .button.button-icon{
	color:white;
}
.main{
	flex:1;
	background: rgba(54, 54, 70, 0.91);
}
.info{
	background: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(54, 54, 70, 0.91));
	ul li{
		width: 33.3%;
		float: left;
		padding:0.15rem 0;

	}
	p i{
		font-size: 0.2rem;
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
</style>
<template>
<div class="sidemenu">
	 <von-header >
    <button @click="goBack" class="button button-icon ion-ios-arrow-back" slot="left"></button>
	    <p class="action" slot="title">Tohcart</p>
	    <!-- <button class="button button-icon ion-navicon" slot="right"></button> -->
	  </von-header>
	<div class="content">
		<div class="info">
			<img src="../static/img/1.jpg" alt="">
			<p>{{userInfo.userName}}</p>
			<p>{{userInfo.car}}</p>
			<p>{{userInfo.tel}}</p>
			<ul>
				<li><p>用户数</p><p><i class="ion-ios-people"></i></p><p>25</p></li>
				<li><p>订单数</p><p><i class="ion-android-list"></i></p><p>200</p></li>
				<li><p>账户余额</p><p><i class="ion-social-yen"></i></p><p>￥4000</p></li>
			</ul>
		</div>
		<div class="main">
			<von-list>
				<von-item>修改昵称</von-item>
				<von-item>修改车牌号</von-item>
				<von-item>修改手机号</von-item>
				<von-item>退出登录</von-item>
			</von-list>
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
		// 	for(var key in data)
		// 	{
		// 		Vue.set(this.userInfo,key,data[key]);
		// 	}
		// 	console.log('sideMenu',this.userInfo);
		// })
		
		// this.userInfo.head_img = 'src/assets/logo.png';
		// this.userInfo.tel='13145950323';
		// this.userInfo.username = 'Tohcart';
	}
}
</script>
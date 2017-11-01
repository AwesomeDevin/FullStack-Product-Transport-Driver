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
	p{
		height: 0.2rem;
		line-height: 0.2rem;
	}
	p i{
		font-size: 0.2rem;
	}
}
.item{
	background: transparent;
	color:white;
	border:0;
	.btn{
		display: inline-block;
	}
}
.hairline-bottom:after{
	background-color: #625e5e;
}
.hairline-bottom:before{
	background-color: #625e5e;
}
h1.title{
	color:black;
}
.info .upload{
	position: relative;
}
.info .upload input{
	position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
	opacity: 0;
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
			<div class="upload">
				<input type="file" name="img" @change="chooseImg" />
				<!-- <img src="../static/img/1.jpg" alt=""> -->
				<img :src="userInfo.head_img" alt="">

			</div>
			<p>{{userInfo.name}}</p>
			<p>{{userInfo.car}}</p>
			<p>{{userInfo.tel}}</p>
			<ul>
				<li><p>用户数</p><p><i class="ion-ios-people"></i></p><p>25</p></li>
				<li><p>订单数</p><p><i class="ion-android-list"></i></p><p>200</p></li>
				<li><p>账户余额</p><p><i class="ion-social-yen"></i></p><p>￥{{userInfo.money}}</p></li>
			</ul>
		</div>
		<div class="main">
			<von-list>
				<von-item><div class="btn" @click="showForm('修改昵称',userInfo.name,'name')">修改昵称</div></von-item>
				<von-item><div class="btn" @click="showForm('修改车牌号',userInfo.car,'car_plate')">修改车牌号</div></von-item>
				<von-item><div class="btn" @click="showForm('修改手机号',userInfo.tel,'tel')">修改手机号</div></von-item>
				<von-item><div class="btn" @click="showModal">关于Tohart</div></von-item>
				<von-item><div class="btn" @click="logout">退出登录</div></von-item>
			</von-list>
		</div>
	</div>
	<define-form @tohide="tohide" :userInfo="userInfo" :valuekey="valuekey" :value="value" :hideForm="hideForm" :title="formtitle"></define-form>
</div>
</template>

<script type="text/javascript">
// import bus from '../module/bus';
// import g from '../module/global';
import Vue from 'vue';
import {VonHeader} from 'vonic/src/index.js'
import {List,Item} from 'vonic/src/index.js'
import MyModal from './MyModal.vue'
import Form from './Form.vue'

export default{
	watch:{
	},
	name:'sideMenu',
	data(){
		return{
			userInfo:null,
			modal: undefined,
			formtitle:null,
			hideForm:true,
			value:null,
			valuekey:null,
		}
	},
	components:{
        'von-header':VonHeader,
        'von-list':List,
        'von-item':Item,
        'define-form':Form,


    },
	methods:{
		showForm(txt,val,k){
			this.formtitle = txt;
			this.hideForm = false;
			if (val)
			{
				this.value=val;
				this.valuekey=k;
			}
		},
		showModal() {
	         this.modal.show()
	      },
		logout(){
			this.$store.commit('increment',null);
			$toast.show('已退出',1000);
			this.$router.push('/intro/login');
		},
		goBack(){
			
			this.$router.push('/Index');
		},
		tohide(data){
			this.hideForm = data;
		},
		chooseImg(e){
				if(!this.userInfo.tel)
				{
					this.$router.push('/intro/welcome');
					return;
				}
				console.log('>>>>',parseInt(e.target.files[0]).size/1024>300,e.target.files[0].size/1024);
				if( parseInt(e.target.files[0].size)/1024>300)
				{
					$toast.show('错误,请传入图片小于300kb的图片');
					return;
				}
				this.$store.commit('chooseImg',e.target.files[0]);
				this.$router.push('/screenshot');

			},
	},
	mounted() {
      $modal.fromComponent(MyModal, {
        title: 'Tohart信息',
        theme: 'default'
      }).then((modal) => {
        this.modal = modal
      })
    },
    destroyed() {
      if (this.modal)
        $modal.destroy(this.modal)
    },
	created(){
		this.userInfo = this.$store.state.userInfo;
		console.log(this.userInfo);
		if(!this.$store.state.userInfo.tel||this.$store.state.userInfo.tel.length<1||!this.$store.state.userInfo.id)
        {
            this.$router.push('/intro/welcome');
        }
		// bus.$on('getUserInfo',function(data){
		// 	for(var key in data)
		// 	{
		// 		Vue.set(this.userInfo,key,data[key]);
		// 	}
		// 	console.log('sideMenu',this.userInfo);
		// })
		
		// this.userInfo.head_img = 'src/assets/logo.png';
		// this.userInfo.tel='13145950323';
		// this.userInfo.name = 'Tohcart';
	}
}
</script>
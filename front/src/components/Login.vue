<style type="text/css" scoped lang='less'>
    div.login{
        color:white;
        height: 100%;
        display: flex;
        flex-direction:column;
    }
     h2{
        padding-top: 1rem;
            color:white;
            font-size: 0.3rem;
            text-align: center;
            font-family: "黑体";
        }
        p.title{
             color:white;
            font-size: 0.2rem;
            text-align: center;
            font-family: "黑体";
        }
        .interface{
            width: 100%;
            flex:1;

            .patch{
                width: 100%;
                height: 20%;
                background: linear-gradient(to bottom, rgba(0,0,0,0),#262525);
            }
            .main{
                width: 100%;
                height: 80%;
                background:#262525;
                padding-top: 0.4rem;
                position: relative;
            }
            label{
                margin:0.1rem 0;
                display: block;
                button{
                    display: block;
                    margin:0 auto;
                    width: 2rem;
                    background:#2c3e50;
                    border:0;
                    line-height: 0.34rem;
                    color:white;
                }
                 button:disabled{
                    background: #262525;
                    color:#ccc;
                }
            }
            input{
                line-height: 0.34rem;
                display: block;
                margin:0 auto;
                width: 2rem;
                text-indent: 0.1rem;
                font-family: "黑体";
                color:white;
                background: #2e343e;
            }
            input::-webkit-input-placeholder{text-align: center;color:#848080;}
            
        }
        button.toregister{
            color:white;
            position: absolute;
            width: 2rem;
            line-height: 0.3rem;
            left: 50%;
            transform:translateX(-50%);
            bottom:0.5rem;
            border:1px solid white;
            background: none;
            box-shadow: 0 0 10px white;
            border-radius: 4em;
        }
        a{
            text-decoration: none;
        }
</style>
<template>
  <div class="login">
      <h2 class="padding" v-text="msg"></h2>
      <p class="title" >Tohcart</p>
      <div class="interface">
            <div class="patch">
                
            </div>
            <div class="main">
                <label for="tel">
                    <input type="text" id="tel" v-model="tel" name="" placeholder="手机号" />
                </label>
                <label for="pwd">
                    <input type="password" id="pwd" v-model="pwd" name="" placeholder="密 码" />
                </label>
                <label>
                    <button :disabled="!isMobileNumber" @click="login">登录</button>
                </label>
                <router-link   to="/intro/register"><button  class="toregister">注  册</button></router-link>
            </div>
        
        </div>
  </div>
</template>
<script>
import {VonInput} from 'vonic/src/index.js'
  export default {
    data () {
      return {
        msg: 'Log In ',
        tel:'',
        pwd:'',  
        }   
    },
    components:{
        'v-input':VonInput,
    },
    computed:{
        isMobileNumber(){
                return this.tel.match(/^1[34578]\d{9}$/)&&this.pwd?true:false;
            }
    },
    methods:{
        login(){
            $loading.show();
            var self = this;
            this.$http.get('http://localhost:4040/api/v1/transport/user/?tel='+this.tel+'&pwd='+this.pwd,{
                emulateJSON:true
            }).then(function(res){
              $loading.hide();
                if(res.data.results.length>0)
                {
                    self.$store.commit('increment',res.data.results[0]);
                    $toast.show('登录成功',500);
                    self.$router.push('/Index');
                }
                else
                {
                    $toast.show('账号或密码错误',1000);
                }
            },function(res){
                $loading.hide();
                $toast.show('网络错误',1000);
                
            });
        }
    },
    mounted(){
        
    }
  }
</script>


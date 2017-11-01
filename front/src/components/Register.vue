<style type="text/css" scoped lang='less'>
    div.register{
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

        .register{
            position: absolute;
            left: 0;
            top:0;
            width: 100%;
            height: 100%;
        }
        a{
            text-decoration: none;
        }
</style>
<template>
  <div class="register">
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
                    <button :disabled="!isMobileNumber"  @click="register">注册</button>
                </label>
                <!-- <router-link  to="/intro/register"> <button class="toregister">注  册</button></router-link> -->
            </div>
        
        </div>
  </div>
</template>
<script>
import {VonInput} from 'vonic/src/index.js'
  export default {
    data () {
      return {
        msg: 'Sign Up ',
        tel:'',
        pwd:'',
      }
    },
    methods:{
        register(){
            var self = this;
            console.log(this.tel,this.pwd);
            var create_time = parseInt(new Date().getTime()/1000);

            // var fd = new FormData();
            // fd.append('image',blob,'default.jpg');
            this.$http.post('http://localhost:4040/api/v1/transport/user/',{
                pwd:1,
                tel:20,
                create_time:create_time,
                name:'asd',
                user_img:'src/static/img/1.jpg',
                car_plate:'',
            },{
                emulateJSON:true
            }).then(function(res){
                if(res)
                {
                    self.$store.commit('increment',res);
                    $toast.show('注册成功',500);
                    self.$router.push('/Index');
                }
                else
                {
                    $toast.show('注册失败',1000);
                }
            },function(res){
                $toast.show('注册失败',1000);
                alert(res.status);
            });
        },
        dataURLtoBlob(dataurl){
             var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
                bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
            while(n--){
                u8arr[n] = bstr.charCodeAt(n);
            }
            return new Blob([u8arr], {type:mime});
        },
    },
    computed:{
        isMobileNumber(){
                return this.tel.match(/^1[34578]\d{9}$/)&&this.pwd?true:false;
            }
    },
    components:{
        'v-input':VonInput,
    }
  }
</script>


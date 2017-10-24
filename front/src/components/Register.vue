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
                    <input type="text" id="tel" name="" placeholder="手机号" />
                </label>
                <label for="pwd">
                    <input type="password" id="pwd" name="" placeholder="密 码" />
                </label>
                <label>
                    <router-link  to="/Index"><button>注册</button></router-link>
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
      }
    },
    components:{
        'v-input':VonInput,
    }
  }
</script>


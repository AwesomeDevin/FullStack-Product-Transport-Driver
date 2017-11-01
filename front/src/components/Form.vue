<style type="text/css" scoped>
    h5{
        color:white;
        text-align: center;
        line-height: 0.44rem;
        margin: 0;
        position: relative;
        /*display: flex;*/
        padding: 0 0.1rem;
        justify-content: space-between;
    }
    .form{
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background: rgba(67, 67, 89, 1);
        /*background-size: cover;*/
        z-index: 100;
        transition:all 0.3s;
    }
    .form.hidden{
        top: 100%;
    }
    div label{
        /*padding: 0 0.1rem;*/
        box-sizing: border-box;
        width: 100%;
        height: 0.4rem;
        background:transparent;
    }
    button.button{
        color:white;
        background: transparent;

    }
    button.button-icon{
        font-size:0.32rem;
        float: left;
        position: absolute;
        left: 0.1rem;
        top: 0;
    }
    button.confirm{
        font-size: 0.13rem;
        position: absolute;
         right: 0.1rem;
        top: 0;
    }
    div label input{
        background:hsla(240, 13%, 22%, 0.89);
        width: 100%;
        line-height: 0.4rem;
        height: 0.4rem;
        padding: 0 0.1rem;
        color:white;
       
    }
</style>
<template>
  <div class="form" :class="hideForm?' hidden':''">
    <h5><button @click="goBack" class="button button-icon ion-ios-arrow-back" ></button><p>{{title}}</p><button @click="confirm" class="button confirm" >确认</button></h5>
    <div style="padding:0 0.2rem;"><label for="txt"><input v-model="val" type="text" id="txt" placeholder="请输入修改内容" /></label></div>
   

  </div>
</template>
<script>
  export default {
    props:{
        title:{default:'设置'},
        hideForm:{default:true},
        value:{default:''},
        valuekey:{default:null},
        userInfo:{default:null},
    },
    data() {
      return {
       val:null,
      }
    },
    computed:{
        
    },

    methods: {
      goBack(){
        this.$emit('tohide',true);
      },
      confirm(){
        var self = this;
        var data={};
        data[this.valuekey]=this.val;
        console.log(data);
        this.$http.put('http://localhost:4040/api/v1/transport/user/'+this.$store.state.userInfo.id+'/',data,{
            emulateJSON:true
        }).then(function(res){
            $toast.show('修改成功',500);
            self.$store.commit('increment',data);
            this.$emit('tohide',true);
        },function(res){
            alert(res.status);
        });
      }
    },
    watch:{
        valuekey(){
            console.log(this.value);
            this.val = this.value;
        }
    },
  }
</script>
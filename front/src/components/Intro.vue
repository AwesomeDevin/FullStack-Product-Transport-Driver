<style type="text/css" scoped lang='less'>
.bg{
    width: 100%;
    height: 5.68rem;
    background: url('../static/img/1.jpg');
    background-size: cover;
    position: relative;
    .intro{
        position: absolute;
        height: 5.68rem;
        width: 100%;
        background: rgba(0,0,0,0.5); 
        h2{
            color:white;
            font-size: 0.3rem;
            text-align: center;
            font-family: '-webkit-pictograph';
        }
        .des{
            position: absolute;
            left: 50%;
            top: 50%;
            transform:translate(-50%,-50%);
        }
        .des p{
            color:white;
            text-align: center;
            font-size: 0.14rem;
        }
        button{
            position: absolute;
            left: 50%;
            bottom: 0.5rem;
            color:white;
            transform:translateX(-50%);
            width: 1rem;
            line-height: 0.3rem;
            border:1px solid white;
            background: 0;
            box-shadow: 0 0 10px white;
            padding:0;
            a{
                font-family: '-webkit-pictograph';
                color:white;
                text-decoration: none;
                display: block;
            }
        }
    }
}
.page-content{
    padding-top: 0 !important;
}
        .fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-to /* .fade-leave-active in below version 2.1.8 */ {
  opacity: 0
}
</style>
<template>
  
    <div class="page has-navbar" v-nav="{ title: 'About', hideNavbar: true }">
        <div class="page-content text-center">
        <div class="bg" >
            <div class="intro">
                <transition name="custom-classes-transition"  enter-active-class="animated fadeIn" leave-active-class="animated fadeOut">
                    <router-view ></router-view>
                </transition>
            </div>
        </div>
    
        </div>

    </div>
</template>

<script type="text/javascript">
    export default{
        name:'intro',
    }
</script>
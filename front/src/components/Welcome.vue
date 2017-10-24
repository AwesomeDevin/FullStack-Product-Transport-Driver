<style type="text/css" scoped lang='less'>
    h2{
            color:white;
            font-size: 0.3rem;
            text-align: center;
            font-family: "黑体";
        }
        .des{
            position: absolute;
            left: 50%;
            top: 50%;
            transform:translate(-50%,-100%);
        }
        .des p{
            color:white;
            text-align: center;
            font-size: 0.14rem;
            margin-top: 0.2rem;
            font-family: "黑体";
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
            background: none;
            box-shadow: 0 0 10px white;
            padding:0;

            a{
                font-family: "黑体";
                color:white;
                text-decoration: none;
                display: block;
            }
        }
        .welcome{
            position: absolute;
            left: 0;
            top:0;
            width: 100%;
            height: 100%;
        }
</style>
<template>
    <div class="welcome">
        <div class="des">
            <h2>Welcome to Tohcart</h2>
            <p>托运 就得上托卡</p>
        </div>
        <button><router-link  to="/intro/login">Next</router-link></button>
    </div>
</template>
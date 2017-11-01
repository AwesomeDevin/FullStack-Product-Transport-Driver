<style type="text/css" scoped lang="less">
		.showimg{
			
			width: 100%;
			height: 100%;
			background-color: #222;
			position: absolute;
			left: 0;
			top: 0;
			
			/*top:6rem;*/
			
		}
		#toshow_img{
			max-height: 5.68rem;
			max-width: 3.2rem;
		}

		.showimg .btn-bar{
			position: absolute;
			bottom:0;
			left: 0;
			background-color:white;
			display: block;
		    width: 100%;
		    height: 0.4rem;
		    display: flex;
    		align-items: center;
    		justify-content: space-between;
		}
		.showimg .btn-bar .back{
			color:white;
			background-color: #ec3838;
			height: 30px;
		    line-height: 30px;
		    padding: 0;
		    width: 60px;
		    margin-left: 10px;
		    border:0;
		}
		.showimg .btn-bar .ok{
			color:white;
			background-color: #22bdbd;
			height: 30px;
		    line-height: 30px;
		    padding: 0;
		    width: 60px;
		    margin-right: 10px;
		    border:0;
		}
		.cropper-container{
			top: 50%;
			transform: translateY(-50%);
		}

		.cropper-face{
		  background-color: transparent;
		}
		// .showimg .cropper-container {
		//     font-size: 0;
		//     line-height: 0;
		//     position: absolute;
		//     -webkit-user-select: none;
		//     -moz-user-select: none;
		//     -ms-user-select: none;
		//     user-select: none;
		//     direction: ltr;
		//     top: 50%;
		//     /* top: 100%; */
		//     transform: translateY(-50%);
		// }
		// .showimg .cropper-view-box{
		// 	border-radius: 50%;
		// 	outline: none;
		// }
		// .showimg .cropper-face, .cropper-line, .cropper-point{
		// 	opacity: 0;
		// }
</style>
<template>
	<div class="showimg">
			<div >
				<img src="" id="toshow_img">
			</div>
						
			<div class="btn-bar" >
			<button @click="toBack()" class="back" >返回</button>
			<button @click="toUpload()" class="ok">确定</button>
			</div>
	</div>
</template>
<script type="text/javascript">
import EXIF from 'exif-js';
import Cropper from 'cropperjs';
// import { Toast } from 'mint-ui';
	export default{
		name:'screenShot',
		data(){
			return{
				userInfo:{},
				files:null,
				Orientation:null,
				cropperObj:null,
			}
		},
		methods:{
			toUpload(){
				function dataURLtoBlob(dataurl) {
					    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
					        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
					    while(n--){
					        u8arr[n] = bstr.charCodeAt(n);
					    }
					    return new Blob([u8arr], {type:mime});
					}
				var blob = dataURLtoBlob(this.cropperObj.getCroppedCanvas().toDataURL());
				var formData = new FormData();
				console.log(blob);
				var fileName = parseInt(Math.random()*1000000) + '.png';
				var file = new window.File([blob], fileName, {type: blob.type});
				console.log(file);
				formData.append('head_img',file);
				formData.append('user_id', this.$store.state.userInfo.id);
				console.log(blob);
				this.$http.post('http://localhost:4040/api/v1/transport/file/', formData).then(function(res){
					if(res.status==200)
					{
						console.log(res);
						this.$store.commit('modifyImg',res.data.url);
						this.$router.push('/sidemenu');
						$toast.show('修改成功');
					}
				}, function(res){
					
				});

			},
			toBack(){
				if(this.cropperObj)
				{
					this.cropperObj.destroy();
				}
				this.cropperObj=null;
				this.$router.push('/sidemenu');
			}
		},
		mounted(){

			this.files = this.$store.state.imgFile;
			const self =this;
			EXIF.getData(this.files, function() {
					this.Orientation = EXIF.getTag(this, 'Orientation'); //去获取拍照时的信息，解决拍出来的照片旋转问题  
				})
				// 看支持不支持FileReader  
				if(!this.files || !window.FileReader) return;
				if(/^image/.test(this.files.type)) {
					var reader = null;
					reader = new FileReader();
					console.log('screenShot2',reader);
					reader.readAsDataURL(this.files);
					reader.onload = function(e) {

						var oimg = document.getElementById("toshow_img");
						console.log('screenShot3',e);
						oimg.setAttribute("src", e.target.result);
						console.log('screenShot4',oimg);
						$(".showimg").addClass('active');
						self.cropperObj = new Cropper(oimg, {
							  aspectRatio: 1 / 1,
							  dragMode:'none',
							  dragCrop:false,
							  background:false,
							  cropBoxResizable:false,
							  guides:false,
							  aspectRatio: 1,  
      						  viewMode: 1, 
      						  center:false,
      						  scalable:true,
							  crop: function(e) {
							    console.log('screenShot5',e)
							  }
						});
						// self.toCropper(oimg);
					}
				} else {
					alert('不支持该图片格式');
				}




		}
	}
</script>
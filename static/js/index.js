let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");
let result = document.getElementById('result')

let stream

camera_button.addEventListener('click', async function() {
	video.style.cssText = 'opacity: 1; visibility: visible;'
	canvas.style.cssText = 'opacity: 0; visibility: hidden;'
	stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
	video.srcObject = stream;
});

click_button.addEventListener('click', function() {
	video.style.cssText = 'opacity: 0; visibility: hidden;'
	canvas.style.cssText = 'opacity: 1; visibility: visible;'
	canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
	var img_base64 = canvas.toDataURL('image/jpeg').replace(/^.*,/, '')
	captureImg(img_base64);
	stream.getTracks().forEach(function(track) {
		track.stop();
	});
});

var xhr = new XMLHttpRequest();

//Captured image data(base64) POST
function captureImg(img_base64) {
	const body = new FormData();
	body.append('img', img_base64);
	xhr.open('POST', 'http://localhost:8000/emotion', true);
	xhr.onload = () => {
		emotion = xhr.responseText
		console.log(emotion)
		result.innerText = "You seem to be " + emotion
	};
	xhr.send(body);
}
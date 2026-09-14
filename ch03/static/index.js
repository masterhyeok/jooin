let a = 0;
document.querySelector('.aa').addEventListener('click', function(){
	a += 1;
	document.querySelector('.aaa').innerHTML = a;
})

document.querySelector('.su').addEventListener('click', function(){
	location.href='http://10.150.0.254:5001/'+a
    	a = 0;
    	document.querySelector('.aaa').innerHTML = a;
})

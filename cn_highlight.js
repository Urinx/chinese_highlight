/*-----------------Author:Eular-----------------*/
var tag={'10':8,'20':6,'30':8,'31':4,'32':8,'40':6,
'41':2,'42':7,'50':4,'60':7,'61':9,'62':0,'63':5,
'64':4,'70':4,'71':9,'72':7,'73':5,'74':9,'80':2,
'81':9,'82':3,'83':6,'84':5,'85':6,'86':4,'87':0,
'90':8,'95':5,'96':0,'97':3,'98':6,'99':7,'100':0,
'101':2,'102':0,'103':1,'104':7,'107':4,'108':8,
'110':7,'111':9,'112':8,'113':0,'120':7,'121':0,
'122':2,'123':9,'124':5,'125':4,'126':3,'127':9,
'130':7,'131':2,'132':3,'133':9,'140':6,'141':4,
'142':6,'143':2,'144':9,'145':7,'146':2,'150':2,
'151':9,'152':9,'153':3,'154':1,'155':1,'156':5,
'160':5,'170':0,'171':6,'172':2,'173':9,'174':6,
'175':9,'176':7,'180':6,'190':6,'191':6,'192':7,
'193':6,'194':7,'195':2,'196':5,'200':3,'201':2,
'202':9,'210':2,'211':1,'212':8,'213':2,'230':7};

var cn_highlight=function(){
	var chinese=document.querySelector('chinese');
	var css=document.createElement('link');
	css.setAttribute('rel','stylesheet');
	css.setAttribute('type','text/css');
	css.setAttribute('href','cn_highlight.css');
	document.querySelector('head').appendChild(css);
	ajax('http://we4test.sinaapp.com/segment.php',chinese.innerHTML,highlightEngine);
}

var highlightEngine=function(response){
	var chinese=document.querySelector('chinese');
	var content=chinese.innerHTML;
	json=JSON.parse(response);
	for (var i = 0; i < json.length; i++) {
		n=tag[json[i].word_tag];
		content=content.replace(json[i].word,'<c'+n+'>'+json[i].word+'</c'+n+'>');
	};
	chinese.innerHTML=content;
}

function ajax(url,data,foo){
	var xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			foo(xmlhttp.responseText);
		};
	};
	xmlhttp.open('POST',url,true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send('words='+data);
}

window.addEventListener('load',cn_highlight);
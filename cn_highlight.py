#! usr/bin/env python
# coding=utf-8
import urllib,json
import urllib2,sys
reload(sys)
sys.setdefaultencoding('utf8')

tag={'10':8,'20':6,'30':8,'31':4,'32':8,'40':6,
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
'202':9,'210':2,'211':1,'212':8,'213':2,'230':7}

html="""
<html>
<!--
	Date:2014.2.7
	Author:Eular
	Github:http://github.com/urinx
-->
<head>
<meta charset="utf-8">
<title>Chinese Segment--Eular</title>
<style type="text/css">
chinese{
	display: block;
	width: 30em;
	height: 20em;
	background-color: rgb(39,40,34);
	border-radius: 1px;
	box-shadow: 3px 3px 4px rgb(39,40,34),-3px 3px 4px rgb(39,40,34),3px -3px 4px rgb(39,40,34),-3px -3px 4px rgb(39,40,34);
	padding: 10px;
	overflow: hidden;
	word-wrap:break-word;
	color: white;
	font-size: 20px;
	/*居中*/
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	margin: auto;
}
chinese c0{
	color: cyan;
}
chinese c1{
	color: deeppink;
}
chinese c2{
	color: gold;
}
chinese c3{
	color: silver;
}
chinese c4{
	color: darkviolet;
}
chinese c5{
	color: lawngreen;
}
chinese c6{
	color: sandybrown;
}
chinese c7{
	color: mediumblue;
}
chinese c8{
	color: red;
}
chinese c9{
	color: sienna;
}
</style>
</head>
<body>
	<chinese>
		<br>
		<br>
		<br>
		<center>
		<!-- Insert here -->
		</center>
	</chinese>
	<footer style="position:absolute;bottom:0;right:10px"><a href="http://github.com/urinx"><img src="http://github.com/urinx/chinese_highlight/img/gitimg.jpg" width="50px" height="50px"></a><p style="font-size:12px;font-weight:bold">Follow Me</p></footer>
</body>
</html>
"""

def segment(chinese,fname='chinese_highlight.html'):
	fsegment_url='http://we4test.sinaapp.com/segment.php?'
	param=urllib.urlencode({'words':chinese})
	req=urllib2.Request(fsegment_url, param)
	response=urllib2.urlopen(req)
	result=response.read()
	j=json.loads(result)

	a=[]
	for i in j:
		n=str(tag[i['word_tag']])
		chinese=chinese.replace(i['word'].decode('utf-8'),'<c'+n+'>'+i['word']+'</c'+n+'>')

	html=html.replace('<!-- Insert here -->',chinese)
	f=open(fname,'w')
	f.write(html)
	f.close()

def usage():
	print '='*80
	print 'Author:Eular'
	print '='*80
	print 'Usage:'
	print '     %s [-w words | -f file] [output file]' % sys.argv[0]
	print 'eg:'
	print '     %s -w \'blablablabla...\' segment.html' % sys.argv[0]
	print '     %s -f words.txt segment.html' % sys.argv[0]
	print '='*80

if __name__=='__main__':
	if len(sys.argv)<4:
		usage()
	else:
		if sys.argv[1]=='-w':
			segment(sys.argv[2],sys.argv[3])
		elif sys.argv[1]=='-f':
			segment(open(sys.argv[2],'r').read(),sys.argv[3])
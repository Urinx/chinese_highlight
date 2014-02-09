chinese_highlight
=================
中文语法高亮
----------
![chinese_highlight.html](img/jietu.png)

###Usage:
<pre>
&lt;script type="text/javascript" src="http://paiplace.5gbfree.com/github/cn_highlight.js"&gt;&lt;/script&gt;
&lt;chinese&gt;将要语法高亮的中文放到该标签里即可&lt;/chinese&gt;
</pre>

##cn_highlight.py
###用python写的脚本，结合SAE的分词服务，将中文文本转成语法高亮的html。
![python usage](img/jietu2.png)

##中文语法高亮颜色对应表
<pre>
0     未知
10  8 形容词
20  6 区别词
30  8 连词
31  4 体词连接
32  8 分句连接
40  6 副词
41  2 副词("不")
42  7 副词("没")
50  4 叹词
60  7 方位词
61  9 方位短语(处所词+方位词)
62  0 方位短语(名词+方位词“地上”)
63  5 方位短语(动词+方位词“取前”)
64  4 方位短语(动词+方位词“取前”)
70  4 前接成分
71  9 数词前缀(“数”---数十)
72  7 时间词前缀(“公元”“明永乐”)
73  5 姓氏
74  9 姓氏
80  2 后接成分
81  9 数词后缀(“来”--,十来个)
82  3 时间词后缀(“初”“末”“时”)
83  6 名词后缀(“们”)
84  5 处所词后缀(“苑”“里”)
85  6 状态词后缀(“然”)
86  4 状态词后缀(“然”)
87  0 状态词后缀(“然”)
90  8 数词
95  5 名词
96  0 人名(“毛泽东”)
97  3 机构团体(“团”的声母为t，名词代码n和t并在一起。“公司”)
98  6 ....
99  7 机构团体名("北大")
100 0 其他专名(“专”的声母的第1个字母为z，名词代码n和z并在一起。)
101 2 名处词
102 0 地名(名处词专指：“中国”)
103 1 n-m,数词开头的名词(三个学生)
104 7 n-rb,以区别词/代词开头的名词(该学校，该生)
107 4 拟声词
108 8 介词
110 7 量词
111 9 动量词(“趟”“遍”)
112 8 时间量词(“年”“月”“期”)
113 0 货币量词(“元”“美元”“英镑”)
120 7 代词
121 0 副词性代词(“怎么”)
122 2 数词性代词(“多少”)
123 9 名词性代词(“什么”“谁”)
124 5 处所词性代词(“哪儿”)
125 4 时间词性代词(“何时”)
126 3 谓词性代词(“怎么样”)
127 9 区别词性代词(“某”“每”)
130 7 处所词(取英语space的第1个字母。“东部”)
131 2 处所词(取英语space的第1个字母。“东部”)
132 3 时间词(取英语time的第1个字母)
133 9 时间专指(“唐代”“西周”)
140 6 助词
141 4 定语助词(“的”)
142 6 状语助词(“地”)
143 2 补语助词(“得”)
144 9 谓词后助词(“了、着、过”)
145 7 体词后助词(“等、等等”)
146 2 助词(“所”)
150 2 标点符号
151 9 顿号(“、”)
152 9 句号(“。”)
153 3 分句尾标点(“，”“；”)
154 1 搭配型标点左部
155 1 搭配型标点右部(“》”“]”“）”)
156 5 中缀型符号
160 5 语气词(取汉字“语”的声母。“吗”“吧”“啦”)
170 0 及物动词(取英语动词verb的第一个字母。)
171 6 不及物谓词(谓宾结构“剃头”)
172 2 动补结构动词(“取出”“放到”)
173 9 动词“是”
174 6 动词“有”
175 9 趋向动词(“来”“去”“进来”)
176 7 助动词(“应该”“能够”)
180 6 状态词(不及物动词,v-o、sp之外的不及物动词)
190 6 语素字
191 6 名词语素(“琥”)
192 7 动词语素(“酹”)
193 6 处所词语素(“中”“日”“美”)
194 7 时间词语素(“唐”“宋”“元”)
195 2 状态词语素(“伟”“芳”)
196 5 状态词语素(“伟”“芳”)
200 3 不及物谓词(主谓结构“腰酸”“头疼”)
201 2 数量短语(“叁个”)
202 9 代量短语(“这个”)
210 2 副形词(直接作状语的形容词)
211 1 名形词(具有名词功能的形容词)
212 8 副动词(直接作状语的动词)
213 2 名动词(指具有名词功能的动词)
230 7 空格
</pre>
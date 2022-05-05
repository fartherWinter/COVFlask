var ec_center = echarts.init(document.getElementById('c2'),'dark');

// var mydata = [{'name':'上海','value':318}]

var ec_center_option = {
	backgroundColor:'#8080C0',
	title:{
		text:"全国现有确诊",
		subtext:"",
		x:'left'
	},
	tooltip:{
		trigger:'item'
	},
	//导航图标
	visualMap:{
		show:true,
		x:'left',
		y:'bottom',
		textStyle:{
			fontSize:8,
		},
		splitlist:[{start: 0,end:0},
			{start: 1,end: 9},
			{start: 10,end:99},
			{start: 100,end: 499},
			{start: 500,end: 999},
			{start: 1000,end:9999},
			{start: 10000}],
		color:['#8A3310','#C64918','#E55B25','#FA8072','#F2AD92','#FFDAB9','#F8F8FF']
	},
	//配置属性
	series:[{
		name:'现有确诊人数',
		type:'map',
		mapType:'china',
		roam:false,//拖动和缩放
		itemStyle:{
			normal:{
				borderWidth: .5,//区域边框宽度
				borderColor:'#009fe8',//区域边框颜色
				areColor:'#ffefd5',//区域颜色
			},
			emphasis:{ //鼠标滑过地图高亮的相关设置
				borderWidth: .5,
				borderColor:'#4b0082',
				areColor:'#fff',
			}
		},
		label:{
			normal:{
				show:true,//省份名称
				fontSize:8,
			},
			emphasis:{
				show:true,
				fontSize:8,
			}
		},
		data:[]
	}]
};
ec_center.setOption(ec_center_option)
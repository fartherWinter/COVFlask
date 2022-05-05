var ec_left2 = echarts.init(document.getElementById('l2'), 'dark');

var ec_left2_Option = {
	backgroundColor:'#8080C0',
	title: {
		text: '全国累计趋势',
		textStyle:{
			
		},
		left: 'left',
	},
	tooltip: {
		trigger: 'axis',
		axisPointer:{
			type:'line',
			lineStyle:{
				color:'#7171C6'
			}
		}
	},
	legend: {
		data: ['累计确诊', '现有无症状', '累计治愈', '累计死亡'],
		left: "right"
	},
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top:50,
		containLabel: true
	},
	// toolbox: {
	// 	feature: {
	// 		saveAsImage: {
	//
	// 		}
	// 	}
	// },
	xAxis: [{
		type: 'category',
		boundaryGap: false,
		data: []
	}],
	yAxis: [{
		type: 'value',
		
		axisLabel:{
			show:true,
			color:'white',
			fontSize:12,
			formatter:function(value){
				if(value >= 1000){
					value = value/1000 + "k"
				}
				return value;
			}
		},
		axisLine:{
			show:true
		},
		splitLine:{
			show:true,
			lineStyle:{
				color: '#17273B',
				width:1,
				type:'solid',
			}
		}
	}],
	series: [{
		name :'累计确诊',
		type:"line",
		smooth:true,
		data:[]
	},{
		name :'现有无症状',
		type:"line",
		smooth:true,
		data:[]
	},{
		name :'累计治愈',
		type:"line",
		smooth:true,
		data:[]
	},{
		name :'累计死亡',
		type:"line",
		smooth:true,
		data:[]
	}]
};

ec_left2.setOption(ec_left2_Option)
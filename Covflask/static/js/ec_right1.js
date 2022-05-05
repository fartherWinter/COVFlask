var ec_right1 = echarts.init(document.getElementById('r1'),'dark');

var ec_right1_Option = {
	backgroundColor:'#8080C0',
	title:{
		text:"全国现有确诊TOP5",
		subtext:"",
		x:'left'
	},
	tooltip:{
		trigger:'item'
	},
	dataset: [{
			dimensions: ['name', 'score'],
			source: [
			]
		},
		{
			transform: {
				type: 'sort',
				config: {
					dimension: 'score',
					order: 'desc'
				}
			}
		}
	],
	xAxis: {
		type: 'category',
		axisLabel: {
			interval: 0,
			rotate: 30
		}
	},
	yAxis: {},
	series: {
		type: 'bar',
		encode: {
			x: 'name',
			y: 'score'
		},
		datasetIndex: 1
	}
};

ec_right1.getOption(ec_right1_Option)

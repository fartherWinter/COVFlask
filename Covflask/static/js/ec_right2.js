var ec_right2 = echarts.init(document.getElementById('r2'), 'dark');

//var data = [{'name':'肺炎','value':'23123'},{'name':'实时','value':'23123123'}]

var ec_right2_Option = {
	backgroundColor: '#8080C0',
	title: {
		text: '今日资讯',
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
	tooltip: {
		show: false
	},
	series: [{
		type: 'wordCloud',
		gridSize: 1,
		sizeRange: [12, 55],
		rotationRange: [-45, 0, 45, 90],
		textStyle: {

			color: function() {
				return 'rgb(' + Math.round(Math.random() * 256) + "," + Math.round(Math.random() *
					256) + "," + Math.round(Math.random() * 256) + ')'
				// var colors = ['#fda67e', '#81cacc', '#cca8ba', "#88cc81", "#82a0c5", '#fddb7e', '#735ba1', '#bda29a', '#6e7074', '#546570', '#c4ccd3'];
				// return colors[parseInt(Math.random() * 10)];


			}
		},

		right: null,
		bottom: null,
		data: []

	}]

};

ec_right2.setOption(ec_right2_Option);

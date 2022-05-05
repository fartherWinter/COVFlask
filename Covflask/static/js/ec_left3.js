var ec_left3 = echarts.init(document.getElementById('l3'), 'dark');

var ec_left3_Option = {
	backgroundColor:'#8080C0',
    title: {
        text: '全国新增趋势',
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
        data: ['新增确诊', '新增无症状', '新增治愈', '新增死亡'],
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
        name :'新增确诊',
        type:"line",
        smooth:true,
        data:[]
    },{
        name :'新增无症状',
        type:"line",
        smooth:true,
        data:[]
    }]
};

ec_left3.setOption(ec_left3_Option)
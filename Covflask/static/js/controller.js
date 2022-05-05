function gettime() {
	$.ajax({
		url: '/time',
		timeout: 10000,
		success: function(data) {
			$("#tim").html(data)
		},
		error: function(xhr, type, errorThrown) {

		}

	});


}

function get_c1_data() {
	$.ajax({
		url: '/c1',
		success: function(data) {
			$(".num h1").eq(0).text(data.confirm);
			$(".num h1").eq(1).text(data.noInfect);
			$(".num h1").eq(2).text(data.heal);
			$(".num h1").eq(3).text(data.dead);
		},
		error: function(xhr, type, errorThrown) {

		}

	});
}
function get_c2_data() {
	$.ajax({
		url: "/c2",
		success: function(data) {
			ec_center_option.series[0].data=data.data
			ec_center.setOption(ec_center_option)
		},
		error: function(xhr, type, errorThrown) {

		}

	});
}
function get_l1_data(){
	$.ajax({
		url:'/l1',
		success: function(data) {
			var region = data.region
			var risk = data.risk
			var s=''
			for(var i in region){
				if(risk[i]=='高风险'){
					s +='<li><span class="high_risk">高风险\t\t</span>'+region[i]+'</li>'

				}
				else{
					s +='<li><span class="middle_risk">中风险\t\t</span>'+region[i]+'</li>'

				}

			}
			$("#risk_warpper_li1").html(s)

		},
		error: function(xhr, type, errorThrown) {

		}
	})
}
function get_l2_data() {
	$.ajax({
		url: "/l2",
		success: function(data) {
			ec_left2_Option.xAxis[0].data=data.day
			ec_left2_Option.series[0].data=data.confirm
			ec_left2_Option.series[1].data=data.noInfect
			ec_left2_Option.series[2].data=data.heal
			ec_left2_Option.series[3].data=data.dead
			ec_left2.setOption(ec_left2_Option)
		},
		error: function(xhr, type, errorThrown) {

		}

	});
}
function get_l3_data() {
	$.ajax({
		url: "/l3",
		success: function(data) {
			ec_left3_Option.xAxis[0].data=data.day
			ec_left3_Option.series[0].data=data.confirm_add
			ec_left3_Option.series[1].data=data.noInfect_add
			ec_left3.setOption(ec_left3_Option)
		},
		error: function(xhr, type, errorThrown) {

		}

	});
}
function get_r1_data() {
	$.ajax({
		url: "/r1",
		success: function(data) {
			ec_right1_Option.dataset[0].source=data.data
			ec_right1.setOption(ec_right1_Option)
		},
		error: function(xhr, type, errorThrown) {

		}

	});
}
function get_r2_data() {
	$.ajax({
		url: "/r2",
		success: function(data) {
			ec_right2_Option.series[0].data=data.kws
			ec_right2.setOption(ec_right2_Option)
		}
		// error: function(xhr, type, errorThrown) {
		//
		// }

	});
}

function refreshPage(){
    window.location.reload()
}

get_c2_data()
gettime()
get_c1_data()
get_l1_data()
get_l2_data()
get_l3_data()
get_r1_data()
get_r2_data()
setInterval(gettime,1000)
setInterval(get_c1_data,10000)
setInterval(get_c2_data,10000)
setInterval(get_l1_data,10000)
setInterval(get_l2_data,10000)
setInterval(get_l3_data,10000)
setInterval(get_r1_data,10000)
setInterval(get_r2_data,10000)
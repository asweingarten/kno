
ApiHost="http://kno.ccl.io:6001";

function xtnsLeftToday() {
    var url = ApiHost+"/xtnsLeftToday";
    $.ajax({
	url: url,
	dataType: "json",
    }).done(function(a,b,c,d) {
	console.log('xS',a,b,c,d);
	var display = (a.results.consumedDailyTransactions + "/" +
		       a.results.dailyTransactionLimit);
	$("#xtns").html( display );

    }).fail(function(a,b,c,d) {
	console.log('xF',a,b,c,d);
    }).always(function(a,b,c,d) {
	//console.log('xA',a,b,c,d);
    });
}
function knoAbout(what) {
    console.log("KNO ABOUT:", what);
    $.ajax({
	url: ApiHost+"/top?term=" + what,
    }).done(function(a,b,c,d) {
	console.log('S',a,b,c,d);
    }).fail(function(a,b,c,d) {
	console.log('F',a,b,c,d);
    }).always(function(a,b,c,d) {
	//console.log('A',a,b,c,d);
	xtnsLeftToday();
    });
}
function kno(elt) {
    var what = elt.value;
    elt.value = "";
    knoAbout(what);
    $('#transactions').html(-1);
}
function main() {
    xtnsLeftToday();
}

function showDiv(list,name) {
    for (var n=0; n<list.length; n++) {
	var item = list[n];
	elt = $('#'+item);
	if (item==name) {
	    elt.show();	   
	} else {
	    elt.hide();
	}
    }
}

// let's make the actual app object
App = new function() {
    this.log = console.log.bind(console);
    this.clog = console.log.bind(console);

//    this.log = function(x) {
//	$('#logsDiv').append("SDGDSFG");
//    }
    
}();

App.log("log test");

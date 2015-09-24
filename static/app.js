
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

	App.log("DONE",a);
	App.raw("DONE",'<pre>'+a+'</pre>');

	var j = JSON.parse(a);

	$.each(j, function(int, val) {
	    console.log("LNK",
			val.url,
			val.title,
			val.id
		       );

	    var txt = ('<div id="news.' + val.id + '">' +
		       (val.image ? 
			'<img style="height:60px;width:80px" src="' + val.image + '">'
			: '') +
		       '<a href="' + val.url + '">' + val.title + '</a>' +
		       '</div><p/>');

	    console.log(txt);
	    
	    App.addMain(txt);

	});

    }).fail(function(a,b,c,d) {
	console.log('F',a,b,c,d);

	App.log("FAIL",2);

    }).always(function(a,b,c,d) {
	//console.log('A',a,b,c,d);
	xtnsLeftToday();

	App.log("ALWAYS",3);

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

    this.log = function(x,y,z,w) {
	// yeah this is wierd, but it works more or less
	if (w)
	    $('#logsDiv').append("<li>" + x + y + z + w);
	else if (z)
	    $('#logsDiv').append("<li>" + x + y + z);
	else if (y)
	    $('#logsDiv').append("<li>" + x + y);
	else
	    $('#logsDiv').append("<li>" + x);
    }
    this.raw = function(x,y,z,w) {
	// yeah this is wierd, but it works more or less
	if (w)
	    $('#rawDiv').append("<li>" + x + y + z + w);
	else if (z)
	    $('#rawDiv').append("<li>" + x + y + z);
	else if (y)
	    $('#rawDiv').append("<li>" + x + y);
	else
	    $('#rawDiv').append("<li>" + x);
    }

    this.addMain = function(txt) {
	$('#mainDiv').append(txt);
    }
    
}();

App.log("log test");

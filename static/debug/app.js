if(!window.G){ // for globals
    window.G={}
}

if(!window.ApiHost){
    window.ApiHost= "http://" + location.host
}

function xtnsLeftToday() {
    var url = ApiHost+"/xtnsLeftToday";
    return $.ajax({
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
	    console.log('xA',a,b,c,d);
    });
}

function knoAbout(what) {
    console.log("KNO ABOUT:", what);
    return $.ajax({
	url: ApiHost+"/top?prefetch=true&term=" + what,
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

	    var template = G.NewsItemTemplate;
	    console.log("VAL", val);
	    var html     = template(val);
	    console.log("HTML", html);
	    App.addMain(html);
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
    $('#xtns').html("<i>Loading...</i>");
}
function main() {
    console.log("1");
    xtnsLeftToday();
    console.log("9");
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
    this.clog = console.log.bind(console);

    this.log = function(x,y,z,w) {
	// yeah this is wierd, but it works more or less
	if (w)	    $('#logsDiv').append("<li>" + x + y + z + w);
	else if (z) $('#logsDiv').append("<li>" + x + y + z);
	else if (y) $('#logsDiv').append("<li>" + x + y);
	else	    $('#logsDiv').append("<li>" + x);
    }
    this.raw = function(x,y,z,w) {
	// yeah this is wierd, but it works more or less
	if (w)	    $('#rawDiv').append("<li>" + x + y + z + w);
	else if (z) $('#rawDiv').append("<li>" + x + y + z);
	else if (y) $('#rawDiv').append("<li>" + x + y);
	else	    $('#rawDiv').append("<li>" + x);
    }

    this.addMain = function(txt) {
	$('#mainDiv').append(txt);
    }
}();

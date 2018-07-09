function x() {
    return "Second";
}

var data = new Object();
data.complete = new Array();
data.incomplete = new Array();

function checkReqId(currentValue) {
	return (currentValue == this);
}

function req(req_id) {
	var chkbox = document.getElementById(req_id);

	if (chkbox.checked) {
		// remove from incomplete
		if (data.incomplete.includes(req_id)) {
			var x = data.incomplete.findIndex(checkReqId,req_id);
			data.incomplete.splice(x,1);
			// delete data.incomplete[x];
		}

		data.complete.push(req_id);
	}
	else {
		// remove from complete
		if (data.complete.includes(req_id)) {
			var x = data.complete.findIndex(checkReqId,req_id);
			data.complete.splice(x,1);
			// delete data.complete[x];
		}
		data.incomplete.push(req_id);
	}

	console.log(JSON.stringify(data));
}

function save() {
	/*var data = new Object();*/
	var url = "http://localhost/completions?";

	data.merit_badge = "Programming";
	data.scout_name = document.getElementById("ScoutName").value;
	//data.complete = ["1a","1b"];

	console.log(JSON.stringify(data));

	var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", url, false); // send synchronously
    xmlhttp.setRequestHeader("Content-Type","application/json");
	xmlhttp.send(JSON.stringify(data));
}

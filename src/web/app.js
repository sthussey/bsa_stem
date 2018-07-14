/*      <script type="text/javascript" language="javascript">
            var versionUpdate = (new Date()).getTime();
            var script = document.createElement("script");
            script.type = "text/javascript";
            script.src = "app.js?v=" + versionUpdate;
            document.head.appendChild(script);
        </script>

*/

var data = new Object();
data.complete = new Array();
data.incomplete = new Array();

function checkReqId(currentValue) {
	return (currentValue == this);
}

function save() {

	var url = "http://localhost/completions?";

	data.merit_badge = document.getElementById("MeritBadge").value;
	data.scout_name = document.getElementById("ScoutName").value;
	//data.complete = ["1a","1b"];

	console.log(JSON.stringify(data));

	var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", url, false); // send synchronously
    xmlhttp.setRequestHeader("Content-Type","application/json");
	xmlhttp.send(JSON.stringify(data));
}

function load() {

	var url = "http://localhost/requirements?merit_badge=";

	url += document.getElementById("MeritBadge").value;;

	var xmlhttp = new XMLHttpRequest();
    xmlhttp.overrideMimeType("application/json");
    xmlhttp.open("GET", url, false); // send synchronously
    xmlhttp.onload = function() {
        console.log(xmlhttp.responseText);

        var jsonResponse = JSON.parse(xmlhttp.responseText);

        console.log(jsonResponse);
        populateReq(jsonResponse);
    }
    xmlhttp.send(null);

}

function populateReq(jsonResponse) {
    var div = document.getElementById("reqs");
    var ele = div;

    // <p><input type="checkbox" id="1a" name="1a" onclick="req('1a');"></p>
    // \u00a0 is equivalent to &nbsp;

    for (var i = 0; i < jsonResponse.length; i++) {
        var req = jsonResponse[i];
        var regex1 = /a$/;
        var regex2 = /[0-9]$/;

        if (regex1.test(req.req_id)) {
            var ul = document.createElement("ul");
            div.appendChild(ul);
            ele = ul;
        }

        if (regex2.test(req.req_id)) {
            ele = div;
        }

        var para = document.createElement("li");
        var chkbox = document.createElement("input");
        chkbox.type = "checkbox";
        chkbox.id = req.req_id;
        chkbox.name = req.req_id;
        chkbox.onclick = function req() {

            if (this.checked) {
                // remove from incomplete
                if (data.incomplete.includes(this.id)) {
                    var x = data.incomplete.findIndex(checkReqId,this.id);
                    data.incomplete.splice(x,1);
                }

                data.complete.push(this.id);
            }
            else {
                // remove from complete
                if (data.complete.includes(this.id)) {
                    var x = data.complete.findIndex(checkReqId,this.id);
                    data.complete.splice(x,1);
                }
                data.incomplete.push(this.id);
            }

            console.log(JSON.stringify(data));
        }

        para.appendChild(chkbox);

        var text = document.createTextNode(req.req_id + '\u00a0' + req.req_desc);
        para.appendChild(text);

        ele.appendChild(para);
        console.log(req.req_id);
    }
}

// let api_key = "WYT2LPVWmsL6X47SJz9K"
// let user_name = "Mavuso"
// let plotly = require('plotly')(user_name,api_key);


$(document).ready(function(){
    let request = new XMLHttpRequest();    
    alert("TESTING click");
    $("#plot_button").click(function() {
        alert("TESTING click");
        request.open('GET','/wits_energy/get_data', true);

        request.onload = function(){
            let data = JSON.parse(request.responseText);
            alert(data.x.length)
        
        
        let graphObject = [{
            x:data.x,
            y:data.y,
            type:'line'
        }];
        
        Plotly.newPlot('graph',graphObject);
        alert("DONE")
        }
        request.send();
    });

});
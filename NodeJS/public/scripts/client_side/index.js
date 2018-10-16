// let api_key = "WYT2LPVWmsL6X47SJz9K"
// let user_name = "Mavuso"
// let plotly = require('plotly')(user_name,api_key);


$(document).ready(function(){
    let graph_query = {'building_name':"",'month':"",'year':"",'type':""}
    $("#plot_button").click(function() {
        let request = new XMLHttpRequest();
        alert(document.getElementById('date_start').value);
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

    // Close the dropdown menu if the user clicks outside of it
    
    $("#building_menu").on("click", "a", function() {
        //let request = new XMLHttpRequest();
        alert(this.id);
        graph_query.building_name = this.id;
    });

    $("#graph_menu").on("click", "a", function() {
        //let request = new XMLHttpRequest();
        alert(this.id);
        graph_query.building_name = this.id;
    });


    $("#buildings_menu").change(function(){
        graph_query.building_name = (this.value);
    });


    $("#plot_menu").change(function(){
        graph_query.type = (this.value);
    });

    $("#plot").click(function(){
        //Validation
        alert(graph_query.type)

        $.post("/wits_energy/create",
        graph_query,
        function(data, status){
            alert(status)
        });
    });
    
});
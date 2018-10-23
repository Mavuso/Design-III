// let api_key = "WYT2LPVWmsL6X47SJz9K"
// let user_name = "Mavuso"
// let plotly = require('plotly')(user_name,api_key);


$(document).ready(function(){
    let graph_query = {'building_name':"",'start':"",'end':"",'type':""}
    
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


    $("#plot").click(function(){
        //Validation
        
        graph_query.start = ($('#date_start').val());
       graph_query.end = ($("#date_end").val());
       graph_query.type = $('#plot_menu').val();
       graph_query.building_name = $('#buildings_menu').val();

       let layout = {
        autosize: false,
        width: 700,
        height: 350,
        
      
        title: "Junction "+graph_query.building_name+" energy consumption plot",
        xaxis: {
          title: "Time",
          titlefont: {
            family: "Courier New, monospace",
            size: 12,
            color: "#7f7f7f"
          }
        },
        yaxis: {
          title: "Energy used(kWh)",
          titlefont: {
            family: "Courier New, monospace",
            size: 12,
            color: "#7f7f7f"
          }
        }
      };

       $.ajax({
        type:"POST",
        async: false,
        cache:false,
        url:"/wits_energy/create",
        data:graph_query,    // multiple data sent using ajax
        success: function (data) {
            let graphObject = [{
            x:data.x,
            y:data.y,
            type:'line'
            }];
            Plotly.newPlot('graph',graphObject,layout);      
        }
      });
      return false; //stoping page resfreshes 
    //    $.post("/wits_energy/create",
    //     graph_query,
    //     function(data,status){
            
    //         if(status == 'success'){
    //             alert("Ibuyile")
                
    //             alert(data.x)
        
        // let graphObject = [{
        //     x:data.x,
        //     y:data.y,
        //     type:'line'
        // }];
                
        //         Plotly.newPlot('graph',graphObject);
        //         alert("DONE");
    //         } 
               
    //         else{alert(status)}

    //     });
            
    });
    
});
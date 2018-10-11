"use strict"

let api_key = "WYT2LPVWmsL6X47SJz9K"
let user_name = "Mavuso"

let plotly = require('plotly')(user_name,api_key);

let data = [{x:[0,1,2,3],y:[7,5,6,10],type:'bar'}];


plotly.plot('graph_div',data)
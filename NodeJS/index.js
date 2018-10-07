let path = require("path");
let express = require("express");
let app = express();

let mainRouter = require('./mainRoutes.js');
let todoRouter = require('./todoRoutes.js');


//mounting
app.use("/cdn",express.static(path.join(__dirname+"/public")));
app.use("/", mainRouter);
app.use("/todo", todoRouter);

app.listen(5000);
console.log("Running");
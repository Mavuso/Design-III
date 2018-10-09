let path = require("path");
let express = require("express");
let app = express();

let mainRouter = require('./mainRoutes.js');
let projectRouter = require('./projectRoutes.js');


//mounting
app.use("/cdn",express.static(path.join(__dirname+"/public")));
app.use("/", mainRouter);
app.use("/wits_energy", projectRouter);

app.listen(5000);
console.log("Running");
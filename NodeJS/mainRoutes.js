let express = require("express")
let path = require("path");

let mainRouter = express.Router()


var app = express()

mainRouter.get('/',function(req,res){
    res.send("Hellow world");
});


mainRouter.get('/about',function(req,res){
    res.sendFile(path.join(__dirname + '/pages/about.html'));
});

module.exports = mainRouter;
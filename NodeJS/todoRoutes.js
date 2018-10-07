let todoList = [];
let express = require("express")
let todoRouter = express.Router();
let path = require("path")

todoRouter.get('/',function(req,res){
    console.log("FUCK!")
    res.sendFile(path.join(__dirname,'/pages/todo','index.html'));
});


todoRouter.get('/create',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','create.html'));
});

todoRouter.get('/delete',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','delete.html'));
});

todoRouter.get('/edit',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','edit.html'));
});

module.exports = todoRouter;
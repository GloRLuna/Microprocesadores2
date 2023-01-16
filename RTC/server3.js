var http = require('http').createServer(handler); //require http server, and create server with function handler()
var fs = require('fs'); //require filesystem module
var io = require('socket.io')(http) //require socket.io module and pass the http object (server)

http.listen(8080); //listen to port 8080

function handler (req, res) { //create server
  fs.readFile(__dirname + '/public/index.html', function(err, data) { //read file index.html in public folder
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
      return res.end("404 Not Found");
    }
    res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
    res.write(data); //write data from index.html
    return res.end();
  });
}

const { SerialPort, ReadlineParser } = require('serialport')
const port = new SerialPort({
    path: '/dev/ttyACM0',
    baudRate: 115200 })
const parser = port.pipe(new ReadlineParser({ delimiter: '\r\n' }))
//parser.on('data', (data) => {
//    console.log(data)
//})

io.sockets.on('connection', function (socket) {// WebSocket Connection
var secs=0;
    parser.on('data', (data) => {
    //    secs=data
        //console.log(data)
        process.stdout.write(data + "\r");
        socket.emit('time', data); //send button status to client
    }) 
    });